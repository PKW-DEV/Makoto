import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import (
    ComponentContext,
    create_actionrow,
    create_button,
)

from database.database_handler import DatabaseHandler

database_handler = DatabaseHandler()


class genshin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Créez votre Profile Genshin Impact")
    async def gprofilecreate(self, ctx, username, ar, uid):
        discord_user_id = [str(ctx.author.id)]
        c = database_handler.check_if_user_exit(discord_user_id)
        if c == False:
            await ctx.send("🔍 Ton compte est en cours de création ...")
            discord_user_id = str(ctx.author.id)
            database_handler.add_user(str(username), int(ar), int(uid), discord_user_id)
            await ctx.send("🔮 Ton compte a été fait avec succès")
        else:
            embed = discord.Embed(title="🤖⚠[ERREUR] ton compte existe déjà", color=0xAD0DE4)
            await ctx.send(embed=embed)

    @commands.command(brief="Votre profil Genshin Impact")
    async def gprofile(self, ctx, user: discord.User):
        discord_user_id = [str(user.id)]
        c = database_handler.check_if_user_exit(discord_user_id)

        if c == False:
            embed = discord.Embed(title="🤖⚠[ERREUR] Le compte que tu as essayé de chercher n'existe pas",
                                  color=0xAD0DE4)
            await ctx.send(embed=embed)
        else:
            p = database_handler.check_profil_user(discord_user_id)
            embed = discord.Embed(title=f"Profile Genshin Impact de {user}", color=0xAD0DE4)
            embed.set_thumbnail(url=str(user.avatar_url))
            embed.add_field(name=f"__Les informations de son compte genshin :__",
                            value=f"🦲 Le nom = `{p[0][0]}`\n💯 Niveau d'aventure `{p[0][3]}`\n👾UID = `{p[0][2]}`")
            embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)

    @gprofile.error
    async def errorgprofile(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="🤖⚠️ [ERREUR] Il manque un Argument ! Recommence avec `!gprofile @quelqu'un`",
                                  color=0xCF1600)
            await ctx.send(embed=embed)

    @gprofilecreate.error
    async def errorgprofilecreate(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="🤖⚠️ [ERREUR] Il manque un Argument ! Recommence avec `!gprofilecreate <pseudo> <ar> <uid>`",
                color=0xCF1600)
            await ctx.send(embed=embed)

    @commands.command(brief="Mets à jours ton niveau d'aventure")
    async def updatear(self, ctx, ar):
        print(ar)
        discord_user_id = str(ctx.author.id)
        database_handler.update_ar(str(ar), discord_user_id)
        embed = discord.Embed(
            title="✅ - Ton niveau d'aventure à été mis à jours sur ton profile genshin impact, !gprofile @toi -> pour voir",
            color=0xAD0DE4)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @updatear.error
    async def errorar(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="🤖⚠️ [ERREUR] Il manque un Argument ! Recommence avec `!updatear <ar>`",
                                  color=0xCF1600)
            await ctx.send(embed=embed)

    @commands.command(brief="Demande D'aide Genshin Impact")
    @commands.has_role("🏯​・Genshin")
    async def helpgenshin(self, ctx):
        user_id = ctx.author.id
        exist = database_handler.check_if_user_need_help([str(user_id)])
        print(exist)
        if exist is False:
            await ctx.send("Tu as déjà une demande d'aide en cours.")
            return
        await ctx.author.send("Bonjour ! Pour ta demande d'aide genshin impact, pourrait-tu me renseigner, ton niveau d'aventure ?")
        await ctx.send(f"{ctx.author.mention} tu as reçu un message privée pour ta demande d'aide genshin impact")

        try:
            ar = await self.bot.wait_for("message", timeout=20)
        except:
            await ctx.author.send("Tu as été trop long à repondre, il faudra refaire la commande")
            return

        await ctx.author.send("Super ! Donne moi ton UID s'il te plaît ^^ !")

        try:
            uid = await self.bot.wait_for("message", timeout=20)
        except:
            await ctx.author.send("Tu as été trop long à repondre, il faudra refaire la commande")
            return

        await ctx.author.send("Très bien ! Maintenant envoie moi la raison de ta demande (boss, donjons, jouer, papoter.. ecris ce que tu veux)")

        try:
            desc = await self.bot.wait_for("message", timeout=30)
        except:
            await ctx.author.send("Tu as été trop long à repondre, il faudra refaire la commande")
            return

        await ctx.author.send("D'accord ! Nous y sommes presque maintenant dis si oui ou non tu veux parler en vocal ?(oui/non)")

        try:
            voc = await self.bot.wait_for("message", timeout=20)
        except:
            await ctx.author.send("Tu as été trop long à repondre, il faudra refaire la commande")
            return

        embed = discord.Embed(title=f"🐣 - Demande d'aide de {ctx.author}", color=0x31DD19)
        embed.add_field(name=f"__Les informations de sa demande :__",
                        value=f"⛩ Niveau d'aventure = `{ar.content}`\n👔 UID `{uid.content}`\n📢 Description = `{desc.content}`\n👄​ Souhaite Vocal ? = `{voc.content}`")
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_author(name="🎁​ - Demande d'aide sur Genshin Impact ! DISPONIBLE")
        m = await ctx.author.send("Dois-je envoyer la demande ?",embed=embed)
        await m.add_reaction("✅")
        await m.add_reaction("❌")

        def checkEmoji(reaction, user):
            return ctx.message.author == user and m.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=20, check=checkEmoji)
            if reaction.emoji == "✅":
                await ctx.author.send("La demande d'aide va être envoyé")
            else:
                print("b")
                await ctx.author.send("La demande d'aide a bien été annulé.")
                return
        except:
            print("a")
            await ctx.author.send("La demande d'aide a bien été annulé.")
            return

        etat = "DISPO"
        user_id = str(ctx.author.id)
        ar = str(ar.content)
        uid = str(uid.content)
        why = str(desc.content)
        voc = str(voc.content)
        database_handler.add_help_genshin(ar, uid, user_id, why, voc, etat)

        c = self.bot.get_channel(998174966841360404)

        await c.send(embed=embed)
        await m.add_reaction("✅")

    @commands.Cog.listener('on_raw_reaction_add')
    async def on_raw_reaction_add(self, payload):
        if payload.channel_id == 998174966841360404:
            embed = discord.Embed(title=f"🐣 - Demande d'aide de ", color=0xDD1919)
            embed.add_field(name=f"__Les informations de sa demande :__",
                            value=f"⛩ Niveau d'aventure = ``\n👔 UID ``\n📢 Description = ``\n👄​ Souhaite Vocal ? = ``")
            embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            embed.set_author(name=f"🎁​ - Demande d'aide sur Genshin Impact ! CLAIM BY {payload.member}")
            c = self.bot.get_channel(998174966841360404)
            m = await c.fetch_message(payload.message_id)

            await m.edit(embed=embed)
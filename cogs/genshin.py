import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *

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
    async def gprofile(self, ctx, user : discord.User):
        discord_user_id = [str(user.id)]
        c = database_handler.check_if_user_exit(discord_user_id)

        if c == False:
            embed = discord.Embed(title="🤖⚠[ERREUR] Le compte que tu as essayé de chercher n'existe pas",
                                  color=0xAD0DE4)
            await ctx.send(embed=embed)
        else:
            p = database_handler.check_profil_user(discord_user_id)
            embed = discord.Embed(title=f"Profile Genshin Impact de {user}", color=0xAD0DE4)
            embed.set_thumbnail(url=str(ctx.author.avatar_url))
            embed.add_field(name=f"__Les informations de son compte genshin :__",
                            value=f"🦲 Le nom = `{p[0][0]}`\n💯 Niveau d'aventure `{p[0][3]}`\n👾UID = `{p[0][2]}`")
            embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)

    @gprofile.error
    async def errorgprofile(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="🤖⚠️ [ERREUR] Il manque un Argument ! Recommence avec `!gprofile @quelqu'un`",
            color=0xAD0DE4)
            await ctx.send(embed=embed)

    @gprofilecreate.error
    async def errorgprofilecreate(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="🤖⚠️ [ERREUR] Il manque un Argument ! Recommence avec `!gprofilecreate <pseudo> <ar> <uid>`",
            color=0xAD0DE4)
            await ctx.send(embed=embed)
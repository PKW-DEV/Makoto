import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *

from database.database_handler import DatabaseHandler
database_handler = DatabaseHandler()

role = ("🏝️​・Raft","🏯​・Genshin","🟦​​・Gmod","​🪖​・R6S","🟣​・osu","🚗・Rocket League","⭐️・Apex Legends")

class role_button(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        user = ctx.author
        identifiant = user.id
        return identifiant == 264335766216376320

    @commands.Cog.listener('on_ready')
    async def on_ready(self):
        c = self.bot.get_channel(992129409857368124)
        m = await c.fetch_message(995395438083584020)
        embed = discord.Embed(
            title="__Hello, choisi un ou des jeux que tu as ! 💜​__",
            color=0xAD0DE4)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        for r in role:
            e,rl= r.split("・")
            embed.add_field(name=f"> Role __{rl}__"  ,value=f"> Appuye sur {e}")
        await m.edit(embed=embed)
        for r in role:
            e,rl= r.split("・")
            em = e.strip("​")
            await m.add_reaction(em)

    @commands.Cog.listener('on_raw_reaction_add')
    async def on_raw_reaction_add(self, payload):
        if payload.channel_id == 992129409857368124:
            for r in role:
                e,rl= r.split("・")
                em = e.strip("​")
                if payload.emoji.name == em:
                    g = payload.guild_id
                    guild = self.bot.get_guild(g)
                    a = discord.utils.get(guild.roles, name=r)
                    await payload.member.add_roles(a)
                    await payload.member.send(f"Le role **{r}** t'a été ajouté avec succès !")

    @commands.Cog.listener('on_component')
    async def on_component(self, ctx):
        await ctx.defer(
            ignore=True
        )
        ide = ctx.component["custom_id"]
        ro = ctx.author.roles
        for r in role:
            a = discord.utils.get(ctx.author.guild.roles, name=r)

            #for g in ro:
            #    if str(g) == r:
            #        await ctx.send("Tu as déjà le role !", hidden=True)
            #        await ctx.author.remove_roles(a)
            #        print("a")
            #        return

            e,rl = r.split("・")
            if ide == rl.lower():
                await ctx.author.add_roles(a)
                await ctx.send(f"Le role **{r}** t'a été ajouté avec succès !", hidden=True)
                print("b")

    @commands.command()
    async def createrolebutton(self,ctx):
        servname = str(ctx.guild)
        servid = str(ctx.guild.id)
        chanid = str(ctx.channel.id)
        embed = discord.Embed(
            title="Hello, choisi un ou des jeux que tu as ! 💜​",
            color=0xAD0DE4)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        msg = await ctx.send(embed=embed)
        messid = str(msg.id)
        database_handler.add_message(servname, servid, messid, chanid)

    @commands.command()
    async def addrole(self, ctx, role : discord.Role, e):
        servid = (str(ctx.guild.id),)
        msg = database_handler.get_message(servid)
        c = database_handler.get_channel(servid)
        chan = self.bot.get_channel(int(c[0][0]))
        m = await chan.fetch_message(int(msg[0][0]))
        embed = discord.Embed(
            title="Hello, choisi un ou des jeux que tu as ! 💜​",
            color=0xAD0DE4)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.add_field(name=f"Pour choisir le jeu {role} ", value=f"utilise l'émojie {e}.",
                        inline=True)
        await m.edit(embed=embed)
        print(role)
        print(role.id)
        print(e)

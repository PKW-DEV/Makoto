import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *

from database.database_handler import DatabaseHandler
database_handler = DatabaseHandler()

role = ("🏝️​・Raft","🏯​・  Genshin","🟦​​・Gmod")

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
        m = await c.fetch_message(992794698043379824)
        embed = discord.Embed(
            title="Hello, choisi un ou des jeux que tu as ! 💜​",
            color=0xAD0DE4)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        for r in role:
            rl,e= r.split("・")
            embed.add_field(name=f"Pour choisir le role __{rl}__"  ,value=f"Appuyez sur le bouton {e}")
        m.edit(embed=embed)

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

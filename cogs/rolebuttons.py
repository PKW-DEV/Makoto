import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *

from database.database_handler import DatabaseHandler
database_handler = DatabaseHandler()

class role_button(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        user = ctx.author
        identifiant = user.id
        return identifiant == 264335766216376320

    @commands.command()
    async def createrolebutton(self,ctx):
        servname = str(ctx.guild)
        servid = str(ctx.guild.id)
        embed = discord.Embed(
            title="Hello, choisi un ou des jeux que tu as ! 💜​",
            color=0xAD0DE4)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        msg = await ctx.send(embed=embed)
        messid = str(msg.id)
        database_handler.add_message(servname, servid, messid)

    @commands.command()
    async def addrole(self, ctx, role : discord.Role, e):
        embed = discord.Embed(
            title="Pour choisir le  ",
            color=0xAD0DE4)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        print(role)
        print(role.id)
        print(e)

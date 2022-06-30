import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *

adminid = (264335766216376320)


class role_button(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        user = ctx.author
        identifiant = user.id
        return identifiant in adminid

    @commands.command()
    async def createrolebutton(self,ctx):
        embed = discord.Embed(
            title="Hello, veuilliez choisir les jeux auquelles vous jouez ! 💜​",
            color=0xAD0DE4)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def addrole(self, ctx, role : discord.Role, e):
        embed = discord.Embed(
            title="Pour choisir le  ",
            color=0xAD0DE4)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)

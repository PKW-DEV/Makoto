import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *

class role_button(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def createrolebutton(self,ctx):
        embed = discord.Embed(
            title="Ci-dessous un menu déroulant vous permettant de faire un ticket dans la catégorie de votre choix.",
            color=0xB90000)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)
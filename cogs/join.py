import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *

intents=discord.Intents.all()

class member_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_member_join')
    async def join(self, member):
        @bot.event
        async def on_member_join(member):
            role = discord.utils.get(member.guild.roles, name='✈️ | Membre')
            await member.add_roles(role)


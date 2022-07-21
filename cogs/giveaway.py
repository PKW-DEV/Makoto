import discord
from discord.ext import commands
from database.database_handler import DatabaseHandler
import random
database_handler = DatabaseHandler()

class event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)

    async def TAS(self, ctx):
        pass

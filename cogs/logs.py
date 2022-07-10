import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *

from database.database_handler import DatabaseHandler
database_handler = DatabaseHandler()

class logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


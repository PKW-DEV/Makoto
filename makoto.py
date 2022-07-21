import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *

import cogs.logs
import cogs.rolebuttons
import cogs.join
import cogs.genshin
import cogs.bestie
import cogs.giveaway

import os
from dotenv import load_dotenv
load_dotenv('.env')
load_dotenv(verbose=True)
TOKEN = os.getenv('TOKEN')


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", description="Makoto", intents=intents)
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print("MAKOTO started successfully !")

class MyHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Aide aux commandes Makoto.", color=0xAD0DE4)
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
        for cog, commands in mapping.items():
           command_signatures = [self.get_command_signature(c) for c in commands]
           if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

bot.help_command = MyHelp()

bot.add_cog(cogs.bestie.bestie(bot))
bot.add_cog(cogs.logs.logs(bot))
bot.add_cog(cogs.rolebuttons.role_button(bot))
bot.add_cog(cogs.join.member_join(bot))
bot.add_cog(cogs.genshin.genshin(bot))
bot.add_cog(cogs.giveaway.event(bot))

bot.run(TOKEN)
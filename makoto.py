import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *

import cogs.join

import os
from dotenv import load_dotenv
load_dotenv('.env')
load_dotenv(verbose=True)
TOKEN = os.getenv('TOKEN')


intents=discord.Intents.all()
bot = commands.Bot(command_prefix ="!", description ="Makoto", intents=intents)
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    guild = bot.get_guild(880887626205380618)
    r = discord.utils.get(guild.roles, name="Non vérifié")
    for c in guild.channels:
        await c.set_permissions(r, read_message=False)
        print(f"{c} add non verifié read_message in false")

    c = bot.get_channel(990927066377617439)
    await c.send("```MAKOTO STARTED SUCCESSFULLY```")
    print("MAKOTO started successfully !")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        if message.content in ("@here","@everyone"):
            return
        else:
            await message.channel.send(f"Hello ! Je suis plein developpement, certaines fonctionnalités ne sont donc pas disponible, regarde le channel {chan.mention} pour suivre mon developpement !")


bot.add_cog(cogs.join.member_join(bot))
bot.run(TOKEN)
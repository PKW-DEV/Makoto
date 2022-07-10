import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *

import cogs.logs
import cogs.rolebuttons
import cogs.join

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
    c = bot.get_channel(990927066377617439)
    u = await bot.fetch_user(264335766216376320)
    #await u.send("Makoto est de retour sur le web")
    #await c.send("```MAKOTO STARTED SUCCESSFULLY```")
    print("MAKOTO started successfully !")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if "PKW" or "ksar" or "pierre" or "pkw" in message.content :
        if 944936702143778879 == message.author.id :
            return
        else:
            u = await bot.fetch_user(264335766216376320)
            author = message.author
            chan = message.channel
            s = message.guild
            await u.send(f"WORD DETECTION | **{author.mention}** t'a mentionné dans {chan.mention} sur le serveur **{s}**. Contenu du message ```{message.content}```")

    if bot.user.mentioned_in(message):
        if "@here" or "@everyone" in message.content:
            return
        else:
            chan = bot.get_channel(990909559906377729)
            await message.channel.send(f"Hello ! Je suis plein developpement, certaines fonctionnalités ne sont donc pas disponible, regarde le channel {chan.mention} pour suivre mon developpement !")

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

bot.add_cog(cogs.logs.logs(bot))
bot.add_cog(cogs.rolebuttons.role_button(bot))
bot.add_cog(cogs.join.member_join(bot))
bot.run(TOKEN)
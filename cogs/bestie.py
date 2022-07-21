from discord.ext import commands
from discord_slash.utils.manage_components import *

from database.database_handler import DatabaseHandler
database_handler = DatabaseHandler()

logo = "https://i.imgur.com/ClhgJ8r.png" #logo I de information

class bestie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role('❣️ | Besties GANG  |❣️')
    async def bestie(self, ctx):
        embed = discord.Embed(title="🤖⚠️ [ERREUR] Tu es déjà une Bestie !!", description="", color=0xC10000)
        embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)


    @bestie.error
    async def bestie_error(self, ctx, error):
        channel = self.bot.get_channel(970225864807698432)
        member = ctx.author
        select = create_select(
            options=[
                create_select_option("PKW <3", value="1"),
                create_select_option("OKW", value="2"),
                create_select_option("DKW", value="3"),
                create_select_option("HKW", value="4")
            ],
            placeholder="Choix en cours ​⚡",
            min_values="1",
            max_values="1"
        )
        await ctx.send("✅ Message envoyé au joueur avec succès !")
        await member.send(">> Qui est à la fois le **créateur des __BESTIES__ et des __KSAR__ ?**",
                          components=[create_actionrow(select)])
        choice = await wait_for_component(self.bot, components=select)

        if choice.values[0] == "1":
            await choice.send(
                "✅ Bravo vous êtes devenu une Bestie ! **Vous avez le grade associé sur le serveur discord KSAR**")
            embed = discord.Embed(title=f"❣️ - Bienvenue à {member} dans le club des Besties !", description="",
                                  color=0xAD0DE4)
            embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            embed.set_author(name="❣️ Nouvelles Bestie !", icon_url=logo)
            await channel.send(embed=embed)
            role = discord.utils.get(member.guild.roles, name='❣️ | Besties GANG  |❣️')
            await member.add_roles(role)
        else:
            await choice.send("❌​ La réponse que tu as fournies est fausse.")


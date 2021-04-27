from discord.ext import commands
from jedit import *
import discord
import bot
from bot import Bot_is_Lock


lock = Bot_is_Lock

class admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="Permet de avertir un membre")
    async def warn(self, ctx, user: discord.Member, *, raison=None):
        global lock
        if lock:
            return

        UserId = str(user.id)

        warns = reader("/home/rix56/pycharm/BOT/jsondata/warn.json")
        listeKeys = list(warns.keys())
        if UserId not in listeKeys:
            print('Warned user')
            warns[UserId] = 0

        warns[UserId] += 1

        if warns[UserId] >= 3:
            warns[UserId] = 0
            try:
                await user.kick()
            except:
                await ctx.send("Bot as ")
            await user.send("Vous avez été kick du serveur {}".format(ctx.guild.name))

        print(f"{warns[UserId]} \n {user.display_name}")

        with open("/home/rix56/pycharm/BOT/jsondata/warn.json", 'w', encoding='utf8') as jsonFile:
            json.dump(warns, jsonFile, indent=4)

        await user.send(f"Vous avez eu un avertissement ! Raison : {raison}")
        await ctx.send(f"Le membre {user.mention} a été averti sur {ctx.guild.name} pour la raison suivante : {raison}")

    @commands.command(description="Kick un membre (pas fini , ne pas utiliser !)")
    async def kick(self, ctx):
        global lock
        if lock:
            return
        ctx.send("En développement.Merci !")

    @commands.command(description="Discord logs")
    async def discord_logs(self, ctx, user: discord.Member):
        global lock
        if lock:
            return
        if ctx.message.author.id in bot.admin:
            await ctx.send(f"Le message à été envoyé à {user.mention}")
            await user.send("Upload en cours...Veuillez patienter s'il vous plaît.")
            await user.send(file=discord.File("../rixybot.log", filename="logs.txt"))
        else:
            await ctx.send("Vous ne pouvez pas exécuter cette commande , elle est réservé aux administrateurs du bot.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        global lock
        if lock:
            return
        print(str(error))
        if "is not found" in str(error):
            await ctx.send(
                'MDR ta cru que cette commande existait ? Petite astuce : met +help pour les commandes :wink:')

    @commands.Cog.listener()
    async def on_ready(self):
        global lock
        if lock:
            return
        print(
            f'Connecté à Discord : depuis votre token , je suis connecté en tant que {self.client.user.name} - {self.client.user.id}.')
        print(f'Le tag discord : {self.client.user}.')
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game("FoxAPI v3 JSON release - Tapez +help ou -help pour les commandes - T'a plus de vie mec dsl."))
        channel = self.client.get_channel(719960333749452863)
        await channel.send(":green_circle: Bot connecté !")
    @commands.Cog.listener()
    async def on_command(self, message):
        premium = reader("/home/rix56/pycharm/BOT/jsondata/premium.json")
        anonymous = reader("/home/rix56/pycharm/BOT/jsondata/anonymous.json")
        UserID = str(message.author.id)
        if premium[UserID] == ":white_check_mark:":
            if anonymous[UserID]:
                await discord.Message.delete(message.message)
    @commands.command(description="Uniquement administrateur du bot - Éteindre le bot")
    async def shutdown(self, ctx):
        userid = ctx.message.author.id
        if userid in bot.admin:
            channel = self.client.get_channel(719960333749452863)
            await ctx.send("Je m'éteint ! Au revoir !")
            await channel.send(":red_circle: Je m'éteint !")
            await bot.client.close()
        else:
            await ctx.send("Vous n'êtes pas un administrateur du bot !")
    @commands.command(description="Pour les développeurs du bot.")
    async def cache_game(self, ctx):
        if ctx.message.author.id in bot.admin:
            await ctx.send("Cela a été envoyé dans vos messages privés.")
            await ctx.author.send(f"Voici le cache du jeu : ```json\n{reader('/home/rix56/pycharm/BOT/jsondata/game.json')}```")
        else:
            await ctx.send("Vous ne pouvez pas exécuter cette commande , elle est réservé aux administrateurs du bot.")

def setup(client):
    client.add_cog(admin(client))

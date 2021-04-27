from discord.ext import commands
from jedit import *
import bot
import random
import asyncio
import discord


class Rank(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description="Ton rank")
    async def rank(self, ctx, user=None):
        global member
        if user is not None:
            for x in ['<', '@', '>', '!']:
                user = user.split(x)
                user = ' '.join(user)
            try:
                member = ctx.guild.get_member(int(user))
            except:
                member = ctx.guild.get_member(user)
        try:
            UserId = str(member.id)
            coins = reader("/home/rix56/pycharm/BOT/jsondata/money.json")
            animals = reader("/home/rix56/pycharm/BOT/jsondata/animals.json")
            levels = reader("/home/rix56/pycharm/BOT/jsondata/levels.json")
            xp = reader("/home/rix56/pycharm/BOT/jsondata/xp.json")
            premium = reader("/home/rix56/pycharm/BOT/jsondata/premium.json")
            listeKeys = list(coins.keys())
            listeKeys2 = list(animals.keys())

            if UserId not in listeKeys:
                print("Created profile")
                coins[UserId] = 50
                await ctx.send("Vous faites rank pour la première fois; Vous avez reçu 50 € !")
                with open("/home/rix56/pycharm/BOT/jsondata/money.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(coins, jsonFile, indent=4)
            if UserId not in listeKeys2:
                print("Created profile")
                animals[UserId] = 0
                with open("/home/rix56/pycharm/BOT/jsondata/animals.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(animals, jsonFile, indent=4)

            help_embed = discord.Embed(
                title=f'Rank de {member.name}',
                color=0xE91E63
            )
            help_embed.set_footer(
                text=f'En réponse à {ctx.message.author.name} - Créé par Rix56',
                icon_url=ctx.message.author.avatar_url
            )

            help_embed.set_thumbnail(url=member.avatar_url)

            print(
                f"Id :{member.id}\n{coins[UserId]} €\n{animals[UserId]} animals\nLevel: {levels[UserId]}\nXp: {xp[UserId]}\nAvatar: {member.avatar_url}")

            if animals[UserId] == 1 or animals[UserId] == 0:
                if ctx.message.author.id == 475215232961085440:
                    await ctx.send("Bonjour , mon créateur !")
                help_embed.add_field(name="Son argent", value=f"{coins[UserId]} €", inline=True)
                help_embed.add_field(name="Ses animaux", value=f"{animals[UserId]} animal", inline=True)
                help_embed.add_field(name="Son niveau", value=f"{levels[UserId]}", inline=True)
                help_embed.add_field(name="XP", value=f"{xp[UserId]}/50", inline=True)
                help_embed.add_field(name="Compte Premium ?", value=f"{premium[UserId]}")
                await ctx.send(embed=help_embed)
            else:
                help_embed.add_field(name="Votre argent", value=f"{coins[UserId]} €", inline=True)
                help_embed.add_field(name="Vos animaux", value=f"{animals[UserId]} animaux", inline=True)
                help_embed.add_field(name="Votre niveau", value=f"{levels[UserId]}", inline=True)
                help_embed.add_field(name="XP", value=f"{xp[UserId]}/50", inline=True)
                help_embed.add_field(name="Compte Premium ?", value=f"{premium[UserId]}", inline=True)
                await ctx.send(embed=help_embed)
        except:
            UserId = str(ctx.message.author.id)
            coins = reader("/home/rix56/pycharm/BOT/jsondata/money.json")
            animals = reader("/home/rix56/pycharm/BOT/jsondata/animals.json")
            levels = reader("/home/rix56/pycharm/BOT/jsondata/levels.json")
            xp = reader("/home/rix56/pycharm/BOT/jsondata/xp.json")
            premium = reader("/home/rix56/pycharm/BOT/jsondata/premium.json")
            listeKeys = list(coins.keys())
            listeKeys2 = list(animals.keys())
            if UserId not in listeKeys:
                print("Created profile")
                coins[UserId] = 50
                await ctx.send("Vous faites rank pour la première fois; Vous avez reçu 50 € !")
                with open("/home/rix56/pycharm/BOT/jsondata/money.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(coins, jsonFile, indent=4)
            if UserId not in listeKeys2:
                print("Created profile")
                animals[UserId] = 0
                with open("/home/rix56/pycharm/BOT/jsondata/animals.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(animals, jsonFile, indent=4)

            help_embed = discord.Embed(
                title=f'Rank de {ctx.message.author.name}',
                color=0xE91E63
            )
            help_embed.set_footer(
                text=f'En réponse à {ctx.message.author.name} - Créé par Rix56',
                icon_url=ctx.message.author.avatar_url
            )

            help_embed.set_thumbnail(url=ctx.message.author.avatar_url)

            print(
                f"Id :{ctx.message.author.id}\n{coins[UserId]} €\n{animals[UserId]} animals\nLevel: {levels[UserId]}\nXp: {xp[UserId]}\nAvatar: {ctx.message.author.avatar_url}")

            if animals[UserId] == 1 or animals[UserId] == 0:
                if ctx.message.author.id == 475215232961085440:
                    await ctx.send("Bonjour , mon créateur !")
                help_embed.add_field(name="Votre argent", value=f"{coins[UserId]} €", inline=True)
                help_embed.add_field(name="Vos animaux", value=f"{animals[UserId]} animal", inline=True)
                help_embed.add_field(name="Votre niveau", value=f"{levels[UserId]}", inline=True)
                help_embed.add_field(name="XP", value=f"{xp[UserId]}/50", inline=True)
                help_embed.add_field(name="Compte Premium ?", value=f"{premium[UserId]}", inline=True)
                await ctx.send(embed=help_embed)
            else:
                help_embed.add_field(name="Votre argent", value=f"{coins[UserId]} €", inline=True)
                help_embed.add_field(name="Vos animaux", value=f"{animals[UserId]} animaux", inline=True)
                help_embed.add_field(name="Votre niveau", value=f"{levels[UserId]}", inline=True)
                help_embed.add_field(name="XP", value=f"{xp[UserId]}/50", inline=True)
                help_embed.add_field(name="Compte Premium ?", value=f"{premium[UserId]}", inline=True)
                await ctx.send(embed=help_embed)

    @commands.command(description="Quand il y a un giveaway , on peut utiliser cette commande !")
    async def money_recup(self, ctx):
        try:
            if money >> 0:
                UserId = str(ctx.message.author.id)
                coins = reader("/home/rix56/pycharm/BOT/jsondata/money.json")
                listeKeys = list(coins.keys())
                if UserId not in listeKeys:
                    await ctx.send(
                        "Vous n'avez pas de compte utilisateur.Faites +rank et il sera automatiquement créé !")
                    return
                coins[UserId] += money
                with open("/home/rix56/pycharm/BOT/jsondata/money.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(coins, jsonFile, indent=4)

                money_embed = discord.Embed(
                    title="Il y a une personne qui a gagné de l'argent !",
                    color=0x7289DA
                )
                money_embed.set_footer(
                    text=f'En réponse à {ctx.message.author.name} - Créé par Rix56',
                    icon_url=ctx.message.author.avatar_url
                )
                money_embed.add_field(name="Message :", value=f"{ctx.message.author.name} a gagné {money} € !",
                                      inline=False)
                await ctx.send(embed=money_embed)
                print(f"{ctx.message.author.name} a gagné {money} € !")
            else:
                error1_embed = discord.Embed(
                    title='Erreur',
                    color=0xE74C3C
                )
                error1_embed.set_footer(
                    text=f'En réponse à {ctx.message.author.name} - Créé par Rix56',
                    icon_url=ctx.message.author.avatar_url
                )
                error1_embed.add_field(name="Erreur:",
                                       value=f"Il n'y a pas actuellement d'argent mis en jeu , {ctx.message.author.name}.",
                                       inline=False)
                await ctx.send(embed=error1_embed)
        except:
            error2_embed = discord.Embed(
                title='Erreur',
                color=0xE74C3C
            )
            error2_embed.set_footer(
                text=f'En réponse à {ctx.message.author.name} - Créé par Rix56',
                icon_url=ctx.message.author.avatar_url
            )
            error2_embed.add_field(name="Erreur:",
                                   value=f"Il n'y a pas actuellement d'argent mis en jeu , {ctx.message.author.name}.",
                                   inline=False)
            await ctx.send(embed=error2_embed)

    @commands.command(description="Payer un animal")
    async def pay_animal(self, ctx):
        UserId = str(ctx.message.author.id)
        coins = reader("/home/rix56/pycharm/BOT/jsondata/money.json")
        animals = reader("/home/rix56/pycharm/BOT/jsondata/animals.json")
        listeKeys = list(coins.keys())
        listeKeys2 = list(animals.keys())
        if UserId not in listeKeys:
            await ctx.send("Vous n'avez pas de compte utilisateur.Faites +rank et il sera automatiquement créé !")
        if UserId not in listeKeys2:
            await ctx.send("Vous n'avez pas de compte utilisateur.Faites +rank et il sera automatiquement créé !")
        else:
            if coins[UserId] >= 20:
                coins[UserId] -= 20
                animals[UserId] += 1
                with open("/home/rix56/pycharm/BOT/jsondata/money.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(coins, jsonFile, indent=4)
                with open("/home/rix56/pycharm/BOT/jsondata/animals.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(animals, jsonFile, indent=4)
                await ctx.send("Vous avez payé un animal !")
            else:
                await ctx.send("Vous n'avez pas assez d'argent !")

    @commands.command(description="Passer à un compte Premium")
    async def buy_premium(self, ctx):
        UserId = str(ctx.message.author.id)
        coins = reader("/home/rix56/pycharm/BOT/jsondata/money.json")
        premium = reader("/home/rix56/pycharm/BOT/jsondata/premium.json")
        listeKeys = list(coins.keys())
        listeKeys2 = list(premium.keys())
        if UserId not in listeKeys:
            await ctx.send("Vous n'avez pas de compte utilisateur.Faites +rank et il sera automatiquement créé !")
            return
        else:
            if premium[UserId] == ":white_check_mark:":
                await ctx.send("Vous êtes déjà premium !")
                return
            if coins[UserId] >= 2500:
                coins[UserId] -= 2500
                premium[UserId] = ":white_check_mark:"
                with open("/home/rix56/pycharm/BOT/jsondata/money.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(coins, jsonFile, indent=4)
                with open("/home/rix56/pycharm/BOT/jsondata/premium.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(premium, jsonFile, indent=4)
                help_embed = discord.Embed(
                    title=f'UNE PERSONNE VIENT DE PASSER PREMIUM !',
                    description=f"La personne {ctx.message.author.name} est passé **PREMIUM !** Un gros gg à lui :heart:",
                    color=0xC27C0E
                )
                await ctx.send(embed=help_embed)

            else:
                await ctx.send("Vous n'avez pas assez d'argent pour payer Premium !")
    @commands.command(description="Pourquoi passer à Premium ?")
    async def premium(self, ctx):
        embed = discord.Embed(title=":gem:Pourquoi passer à Premium ?:gem:", color=0x1ABC9C)
        embed.add_field(name=":gift: 1er avantage : les commandes uniquement Premium :gift:", value="La première , et la plus fun , ce sont les commandes **Premium !**\nElles rajoutent une nouvelle dimension au Bot !", inline=False)
        embed.add_field(name=":gift: 2ème avantage : les messages envoyés par vous pour les commandes automatiquement supprimés pour l'anonymat :gift:", value="La deuxième , est très utile ! Contrairement aux compte normaux , si vous avez **Premium**, le bot effacera le message que vous avez envoyé pour exécuter une commande ! Utile pour l'anonymat ! Vous pouvez, bien sûr , désactiver/activeratt cette fonctionnalité simplement en fesant +anonymousmode.", inline=False)
        embed.add_field(name=":question: C'est bien beau tout ça , mais ça coute combien ? :question:", value="J'étais sûr que vous allez vous posez cette question ! Déjà , on paye en argent vrtuel le compte Premium.\nOn ne le paye qu'une seule fois.\nEt ça coute 2500 € ! (Argent virtuel du coup)", inline=False)
        await ctx.send(embed=embed)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == bot.client.user:
            return
        if not message.guild:
            return
        UserId = str(message.author.id)
        levels = reader("/home/rix56/pycharm/BOT/jsondata/levels.json")
        xp = reader("/home/rix56/pycharm/BOT/jsondata/xp.json")
        premium = reader("/home/rix56/pycharm/BOT/jsondata/premium.json")
        coins = reader("/home/rix56/pycharm/BOT/jsondata/money.json")
        anonymous = reader("/home/rix56/pycharm/BOT/jsondata/anonymous.json")
        listeKeys = list(levels.keys())
        listeKeys2 = list(xp.keys())
        listeKeys3 = list(premium.keys())
        listeKeys4 = list(anonymous.keys())
        listeKeys5 = list(anonymous.keys())
        if UserId not in listeKeys:
            print('Created profile')
            levels[UserId] = 0
        if UserId not in listeKeys2:
            print('Created profile')
            xp[UserId] = 0
        if UserId not in listeKeys3:
            print('Created profile')
            premium[UserId] = ":x:"
        if UserId not in listeKeys4:
            print('Created profile')
            anonymous[UserId] = True
        if UserId not in listeKeys5:
            print('Created profile')
            coins[UserId] = 50
        xp[UserId] += 1
        with open("/home/rix56/pycharm/BOT/jsondata/xp.json", 'w', encoding='utf8') as jsonFile:
            json.dump(xp, jsonFile, indent=4)
        with open("/home/rix56/pycharm/BOT/jsondata/levels.json", 'w', encoding='utf8') as jsonFile:
            json.dump(levels, jsonFile, indent=4)
        with open("/home/rix56/pycharm/BOT/jsondata/premium.json", 'w', encoding='utf8') as jsonFile:
            json.dump(premium, jsonFile, indent=4)
        with open("/home/rix56/pycharm/BOT/jsondata/anonymous.json", 'w', encoding='utf8') as jsonFile:
            json.dump(anonymous, jsonFile, indent=4)
        with open("/home/rix56/pycharm/BOT/jsondata/money.json", 'w', encoding='utf8') as jsonFile:
            json.dump(coins, jsonFile, indent=4)

        if xp[UserId] == 50:
            xp[UserId] = 0
            with open("/home/rix56/pycharm/BOT/jsondata/xp.json", 'w', encoding='utf8') as jsonFile:
                json.dump(xp, jsonFile, indent=4)
            levels[UserId] += 1
            with open("/home/rix56/pycharm/BOT/jsondata/levels.json", 'w', encoding='utf8') as jsonFile:
                json.dump(levels, jsonFile, indent=4)
            coins[UserId] += 25
            with open("/home/rix56/pycharm/BOT/jsondata/money.json", 'w', encoding='utf8') as jsonFile:
                json.dump(coins, jsonFile, indent=4)
            level_up_embed = discord.Embed(
                title="Une personne est monté de niveau !",
                color=0xC27C0E
            )
            level_up_embed.add_field(name="Message:",
                                     value=f"{message.author.name} a gagné un niveau ! Il est maintenant niveau {levels[UserId]} ! Il vient de gagner 25 € ! Il a maintenant {coins[UserId]} € !",
                                     inline=False)
            await message.channel.send(embed=level_up_embed)

        message_random = random.randint(1, 30)

        if message_random == 30:
            money_giveaway_embed = discord.Embed(
                title="Giveaway d'argent ! Faites +money_recup pour les avoir !",
                color=0xC27C0E
            )
            global money
            money = random.randint(1, 50)
            money_giveaway_embed.add_field(name="Argent à gagner :", value=f"{money} € ")
            await message.channel.send(embed=money_giveaway_embed)
            print(f"Giveaway en cours : {money} € est à gagner !")
            await asyncio.sleep(20)
            money = 0
            await message.channel.send("Trop tard , le giveaway est terminé !")
            print("Giveaway terminé !")

    @commands.command(description="Donner de l'argent à quelqu'un (Ne pas mettre à la fin du nombre d'argent '€'.)")
    async def transfert(self, ctx, argent,
                        user=None):  # L'étoile sert à récup tous ce qui est saisie après dans une variable
        global member
        try:
            argent = int(argent)
        except ValueError:
            raise ('Is it a valid number ?')
        if user is not None:
            for x in ['<', '@', '>', '!']:
                user = user.split(x)
                user = ' '.join(user)
            try:
                member = ctx.guild.get_member(int(user))
            except:
                member = ctx.guild.get_member(user)
        MO_userid = str(ctx.message.author.id)
        d_userid = str(member.id)
        coins = reader("/home/rix56/pycharm/BOT/jsondata/money.json")
        listeKeys = list(coins.keys())

        argent_int = { True: argent, False: 0 }[
            0 < argent <= 10000]  # on utilise un ternary opérateur pour vérifié que argent est supérieur à 0 et inférieur ou égale à 10 000
        if argent_int == 0:
            await ctx.send("Je ne sais pas faire ça '_'")
            return

        if MO_userid not in listeKeys:
            await ctx.send("Vous n'avez pas de profil utilisateur !")
            return
        if d_userid not in listeKeys:
            await ctx.send("Cet utilisateur n'a pas de profil utilisateur !")
            return
        if argent_int > coins[MO_userid]:
            await ctx.send("Vous n'avez pas assez d'argent !")
            return
        coins[MO_userid] -= argent_int
        coins[d_userid] += argent_int
        await ctx.send(f"Vous avez donné {argent} € à {member.name} !")
        with open("/home/rix56/pycharm/BOT/jsondata/money.json", 'w', encoding='utf8') as jsonFile:
            json.dump(coins, jsonFile, indent=4)

    @commands.command(description="Une commande pour tester si vous avez premium")
    async def premium_test(self, ctx):
        UserId = str(ctx.message.author.id)
        premium = reader("/home/rix56/pycharm/BOT/jsondata/premium.json")
        if premium[UserId] == ":white_check_mark:":
            await ctx.send("Vous êtes premium ! GG !")
        else:
            await ctx.send("Vous n'êtes pas premium...Vous pouvez essayer de l'acheter avec +buy_premium...")
    @commands.command(description="Passer en mode anonyme **(UNIQUEMENT PREMIUM)**")
    async def anonymousmode(self, ctx):
        premium = reader("/home/rix56/pycharm/BOT/jsondata/premium.json")
        anonymous = reader("/home/rix56/pycharm/BOT/jsondata/anonymous.json")
        UserID = str(ctx.message.author.id)
        if premium[UserID] == ":white_check_mark:":
            if anonymous[UserID]:
                anonymous[UserID] = False
                with open("/home/rix56/pycharm/BOT/jsondata/anonymous.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(anonymous, jsonFile, indent=4)
                await ctx.send(f"Le mode Anonyme a été désactivé, {ctx.message.author.name}.")
                return
            if not anonymous[UserID]:
                anonymous[UserID] = True
                with open("/home/rix56/pycharm/BOT/jsondata/anonymous.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(anonymous, jsonFile, indent=4)
                await ctx.send(f"Le mode Anonyme a été activé, {ctx.message.author.name}.")
                return
        else:
            error1_embed = discord.Embed(
                title='Erreur',
                color=0xE74C3C
            )
            error1_embed.set_footer(
                text=f'En réponse à {ctx.message.author.name} - Créé par Rix56',
                icon_url=ctx.message.author.avatar_url
            )
            error1_embed.add_field(name="Erreur:",
                                   value="Cette commande est réservé aux gens ayant un compte **__Premium.__**",
                                   inline=False)
            await ctx.send(embed=error1_embed)


def setup(client):
    client.add_cog(Rank(client))

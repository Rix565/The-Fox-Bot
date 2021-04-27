from discord.ext import commands
import discord
from jedit import *
import random
import asyncio


class Jeu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="Pour démarrer une nouvelle partie")
    async def start_game(self, ctx):
        game = reader("/home/rix56/pycharm/BOT/jsondata/game.json")
        userid = str(ctx.message.author.id)
        listkeys = game.keys()
        if userid not in listkeys:
            game_start_embed = discord.Embed(title="Création de votre partie en cours...",
                                             description="Votre partie est en cours de création , veuillez patientez...")
            await ctx.send(embed=game_start_embed)
            game[userid] = { "introduction?": True, "habitants": 0, "maisons": 1, "argent_du_village": 50,
                             "modes": "blank", "claim_money?": False, "max_villager_capacity": 10, "metal": 100,
                             "bois": 125, "villa": 0, "type_village": "village", "immeuble": 0 }
            with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                json.dump(game, jsonFile, indent=4)
            await ctx.send("Partie créé ! Commencez votre aventure avec +village...")
        else:
            await ctx.send("Vous avez déjà une partie en cours !")

    @commands.command(description="Pour voir les stats de votre village")
    async def village(self, ctx):
        game = reader("/home/rix56/pycharm/BOT/jsondata/game.json")
        userid = str(ctx.message.author.id)
        listkeys = game.keys()
        if userid not in listkeys:
            await ctx.send("Vous n'avez aucune partie en cours.Commencez-la maintenant avec +start_game !")
            return
        if game[userid]["introduction?"]:
            game_introduction_embed = discord.Embed(title="Introduction",
                                                    description="Au fin fond du monde, vit un très récent village puisque il a été fondé **aujourd'hui.**Vous en êtes le maire.Décidez les bonnes actions, faites venir vos habitants et ayez le village le plus développé !\nSur ce , commençons ! Pour le départ , vous avez 1 maison et 50 € !",
                                                    color=0x1ABC9C)
            await ctx.send(embed=game_introduction_embed)
            game[userid]["introduction?"] = False
            with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                json.dump(game, jsonFile, indent=4)
        if game[userid]["type_village"] == "village":
            game_embed = discord.Embed(title=f"Village de {ctx.message.author.name}", color=0x1ABC9C)
            game_embed.set_thumbnail(url=ctx.message.author.avatar_url)
            game_embed.add_field(name="Habitants", value=f"`{game[userid]['habitants']}` habitant(s)")
            game_embed.add_field(name="Maisons", value=f"`{game[userid]['maisons']}` maison(s)")
            game_embed.add_field(name="Villa", value=f"`{game[userid]['villa']}` villa")
            game_embed.add_field(name="Immeubles", value=f"`{game[userid]['immeuble']}` immeubles")
            game_embed.add_field(name="Capacité du village",
                                 value=f"`{game[userid]['habitants']}/{game[userid]['max_villager_capacity']}` habitant(s)")
            game_embed.add_field(name="Argent du village", value=f"`{game[userid]['argent_du_village']}` €")
            game_embed.add_field(name="Bûches de bois", value=f"`{game[userid]['bois']}` bûches de bois")
            game_embed.add_field(name="Bouts de métaux", value=f"`{game[userid]['metal']}` bouts de métaux")
            game_embed.set_footer(
                text=f'En réponse à {ctx.message.author.name} - Créé par Rix56',
                icon_url=ctx.message.author.avatar_url
            )
            await ctx.send(embed=game_embed)
        if game[userid]["type_village"] == "commune":
            game_embed = discord.Embed(title=f"Commune de {ctx.message.author.name}", color=0x1ABC9C)
            game_embed.set_thumbnail(url=ctx.message.author.avatar_url)
            game_embed.add_field(name="Habitants", value=f"`{game[userid]['habitants']}` habitant(s)")
            game_embed.add_field(name="Maisons", value=f"`{game[userid]['maisons']}` maison(s)")
            game_embed.add_field(name="Villa", value=f"`{game[userid]['villa']}` villa")
            game_embed.add_field(name="Immeubles", value=f"`{game[userid]['immeuble']}` immeubles")
            game_embed.add_field(name="Capacité de la commune",
                                 value=f"`{game[userid]['habitants']}/{game[userid]['max_villager_capacity']}` habitant(s)")
            game_embed.add_field(name="Argent de la commune", value=f"`{game[userid]['argent_du_village']}` €")
            game_embed.add_field(name="Bûches de bois", value=f"`{game[userid]['bois']}` bûches de bois")
            game_embed.add_field(name="Bouts de métaux", value=f"`{game[userid]['metal']}` bouts de métaux")
            game_embed.set_footer(
                text=f'En réponse à {ctx.message.author.name} - Créé par Rix56',
                icon_url=ctx.message.author.avatar_url
            )
            await ctx.send(embed=game_embed)

    @commands.command(description="Pour récupérer de l'argent grâce aux villageois - Cooldown 1 jour")
    async def claim_ressources(self, ctx):
        game = reader("/home/rix56/pycharm/BOT/jsondata/game.json")
        userid = str(ctx.message.author.id)
        listkeys = game.keys()
        if userid not in listkeys:
            await ctx.send("Vous n'avez aucune partie en cours.Commencez-la maintenant avec +start_game !")
            return
        if game[userid]["habitants"] == 0:
            await ctx.send("Vous n'avez aucun villageois !")
            return
        if game[userid]["claim_money?"] == True:
            claimed_money = game[userid]["habitants"] * random.randint(1, 10)
            claimed_bois = game[userid]["habitants"] * random.randint(1, 20)
            claimed_metal = game[userid]["habitants"] * random.randint(1, 15)
            game[userid]["argent_du_village"] += claimed_money
            game[userid]["bois"] += claimed_bois
            game[userid]["metal"] += claimed_metal
            game[userid]["claim_money?"] = False
            with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                json.dump(game, jsonFile, indent=4)
            claim_embed = discord.Embed(title="Ressources récupérés",
                                        description=f"Vous avez récupéré `{claimed_money} €`, `{claimed_bois} bûches de bois`, `{claimed_metal} bouts de métaux` grâce à vos villageois !",
                                        color=0xF1C40F)
            await ctx.send(embed=claim_embed)
        else:
            await ctx.send("Vous ne pouvez pour l'instant pas récupérer de ressources !")

    @commands.command(description="Construire une nouvelle maison pour acceuilir de nouveaux villageois")
    async def buy_house(self, ctx):
        game = reader("/home/rix56/pycharm/BOT/jsondata/game.json")
        userid = str(ctx.message.author.id)
        listkeys = game.keys()
        if userid not in listkeys:
            await ctx.send("Vous n'avez aucune partie en cours.Commencez-la maintenant avec +start_game !")
            return
        if game[userid]["argent_du_village"] >= 25 and game[userid]["bois"] >= 45 and game[userid]["metal"] >= 35:
            game[userid]["argent_du_village"] -= 20
            game[userid]["bois"] -= 45
            game[userid]["metal"] -= 35
            game[userid]["maisons"] += 1
            game[userid]["max_villager_capacity"] += 10
            with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                json.dump(game, jsonFile, indent=4)
            await ctx.send(
                f"Vous avez construit une maison ! Vous avez maintenant {game[userid]['maisons']} maisons ! Vous avez maintenant {game[userid]['max_villager_capacity']} en capacité maximale d'habitants !")
        else:
            await ctx.send(
                "Vous n'avez pas assez de ressources ! Il vous faut `25 €`, `45 bûches de bois`, `35 bouts de métaux` !")

    @commands.command(description="Construire une nouvelle villa pour acceuilir de nouveaux villageois")
    async def buy_villa(self, ctx):
        game = reader("/home/rix56/pycharm/BOT/jsondata/game.json")
        userid = str(ctx.message.author.id)
        listkeys = game.keys()
        if userid not in listkeys:
            await ctx.send("Vous n'avez aucune partie en cours.Commencez-la maintenant avec +start_game !")
            return
        if game[userid]["argent_du_village"] >= 45 and game[userid]["bois"] >= 70 and game[userid]["metal"] >= 55:
            game[userid]["argent_du_village"] -= 45
            game[userid]["bois"] -= 70
            game[userid]["metal"] -= 55
            game[userid]["villa"] += 1
            game[userid]["max_villager_capacity"] += 20
            with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                json.dump(game, jsonFile, indent=4)
            await ctx.send(
                f"Vous avez construit une villa ! Vous avez maintenant {game[userid]['villa']} villa ! Vous avez maintenant {game[userid]['max_villager_capacity']} en capacité maximale d'habitants !")
        else:
            await ctx.send(
                "Vous n'avez pas assez de ressources ! Il vous faut `45 €`, `70 bûches de bois`, `55 bouts de métaux` !")

    @commands.command(description="Construire un nouveau immeuble pour acceuilir de nouveaux villageois")
    async def buy_building(self, ctx):
        game = reader("/home/rix56/pycharm/BOT/jsondata/game.json")
        userid = str(ctx.message.author.id)
        listkeys = game.keys()
        if userid not in listkeys:
            await ctx.send("Vous n'avez aucune partie en cours.Commencez-la maintenant avec +start_game !")
            return
        if game[userid]["argent_du_village"] >= 65 and game[userid]["bois"] >= 95 and game[userid]["metal"] >= 110:
            game[userid]["argent_du_village"] -= 65
            game[userid]["bois"] -= 95
            game[userid]["metal"] -= 110
            game[userid]["immeuble"] += 1
            game[userid]["max_villager_capacity"] += 40
            with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                json.dump(game, jsonFile, indent=4)
            await ctx.send(
                f"Vous avez construit un immeuble ! Vous avez maintenant {game[userid]['immeuble']} immeubles ! Vous avez maintenant {game[userid]['max_villager_capacity']} en capacité maximale d'habitants !")
        else:
            await ctx.send(
                "Vous n'avez pas assez de ressources ! Il vous faut `65 €`, `95 bûches de bois`, `110 bouts de métaux` !")

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)
        game = reader("/home/rix56/pycharm/BOT/jsondata/game.json")
        userid = str(message.author.id)
        listkeys = game.keys()
        if userid not in listkeys:
            return
        if game[userid]["habitants"] >= 1:
            luck = random.randint(1, 60)
            if luck == 60:
                modes = [
                    "le sport",
                    "l'informatique",
                    "la danse",
                    "les jeux vidéos",
                    "les jeux de sociétés",
                    "le troc",
                    "la mode",
                    "la beauté",
                    "le trucage",
                ]
                game[userid]["modes"] = random.choice(modes)
                with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(game, jsonFile, indent=4)
                if game[userid]["type_village"] == "village":
                    await message.channel.send(
                        f"{message.author.name}, apparament, dans votre village, il y a une nouvelle tendance...")
                if game[userid]["type_village"] == "commune":
                    await message.channel.send(
                        f"{message.author.name}, apparament, dans votre commune, il y a une nouvelle tendance...")
        chances = random.randint(1, 50)
        if chances == 50:
            if game[userid]["max_villager_capacity"] == game[userid]["habitants"]:
                if game[userid]["type_village"] == "village":
                    await message.channel.send(
                        f"{message.author.name}, votre village a failli acceuilir un villageois , mais celui-ci était plein.")
                    return
                if game[userid]["type_village"] == "commune":
                    await message.channel.send(
                        f"{message.author.name}, votre commune a failli acceuilir un villageois , mais celui-ci était plein.")
                    return
            game[userid]["habitants"] += 1
            with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                json.dump(game, jsonFile, indent=4)
            if game[userid]["type_village"] == "village":
                await message.channel.send(f"{message.author.name}, votre village a acceuili un nouveau villageois !")
            if game[userid]["type_village"] == "commune":
                await message.channel.send(f"{message.author.name}, votre commune a acceuili un nouveau villageois !")
            if game[userid]["habitants"] == 500:
                game[userid]["type_village"] = "commune"
                with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(game, jsonFile, indent=4)
                up_embed = discord.Embed(title=f"BRAVO {message.author.name} !",
                                         description=f"FÉLICITATIONS {message.author.name} ! Votre village a évolué est il est devenu une commune !",
                                         color=0x11806A)
                await message.channel.send(embed=up_embed)

        chances2 = random.randint(1, 75)
        if chances2 == 75:
            game[userid]["claim_money?"] = True
            with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                json.dump(game, jsonFile, indent=4)
            if game[userid]["type_village"] == "village":
                await message.channel.send(
                    f"{message.author.name}, votre village est prêt à vous donner des ressources ! Faites +claim_ressources !")
            if game[userid]["type_village"] == "commune":
                await message.channel.send(
                    f"{message.author.name}, votre commune est prêt à vous donner des ressources ! Faites +claim_ressources !")

    @commands.command(description="Pour savoir ce qui est actuellement à la mode dans votre village")
    async def a_la_mode(self, ctx):
        game = reader("/home/rix56/pycharm/BOT/jsondata/game.json")
        userid = str(ctx.message.author.id)
        listkeys = game.keys()
        if userid not in listkeys:
            await ctx.send("Vous n'avez aucune partie en cours.Commencez-la maintenant avec +start_game !")
            return
        if game[userid]["habitants"] >= 1:
            if game[userid]["modes"] == "blank":
                await ctx.send("Il n'y a actuellement aucune chose à la mode.")
                return
            if game[userid]["type_village"] == "village":
                embed = discord.Embed(
                    title=f"Ce qui est actuellement à la mode dans le village de {ctx.message.author.name}...",
                    description=f"Voici ce qui est actuellement à la mode : {game[userid]['modes']}.", color=0x11806A)
                await ctx.send(embed=embed)
            if game[userid]["type_village"] == "commune":
                embed = discord.Embed(
                    title=f"Ce qui est actuellement à la mode dans la commune de {ctx.message.author.name}...",
                    description=f"Voici ce qui est actuellement à la mode : {game[userid]['modes']}.", color=0x11806A)
                await ctx.send(embed=embed)
        else:
            await ctx.send("Vous n'avez encore aucun habitant !")

    @commands.command(description="Supprimer votre partie en cours")
    async def delete_game(self, ctx):
        game = reader("/home/rix56/pycharm/BOT/jsondata/game.json")
        userid = str(ctx.message.author.id)
        listkeys = game.keys()
        if userid not in listkeys:
            await ctx.send("Vous n'avez aucune partie en cours !")
            return
        await ctx.send(
            "Pour confirmer la suppression de votre partie , ajoutez la réaction ✅ à ce message.Vous avez 10 secondes.")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "✅"

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Partie non supprimée !")
        else:
            del game[userid]
            with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                json.dump(game, jsonFile, indent=4)
            await ctx.send("Votre partie en cours a bel et bien été supprimée ! :sob:")

    @commands.command(
        description="Donner des ressources de votre village à quelqu'un. Options possibles : metal, wood, money. Ex : +transfer 40 money MENTION OU ID UTILISATEUR")
    async def transfer(self, ctx, argent, transfermethod=None, user=None):  # L'étoile sert à récup tous ce qui est saisie après dans une variable
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
        if transfermethod is None:
            await ctx.send(
                "Vous n'avez pas indiqué ce que vous voulez transférer à un utilisateur ! Faites +transfer NOMBRE metal, wood ou money MENTION OU ID UTILISATEUR!")
        if transfermethod == "metal":
            MO_userid = str(ctx.message.author.id)
            d_userid = str(member.id)
            game = reader("/home/rix56/pycharm/BOT/jsondata/game.json")
            listeKeys = list(game.keys())

            argent_int = { True: argent, False: 0 }[
                0 < argent <= 10000]  # on utilise un ternary opérateur pour vérifié que argent est supérieur à 0 et inférieur ou égale à 10 000
            if argent_int == 0:
                await ctx.send("Je ne sais pas faire ça '_'")
                return

            if MO_userid not in listeKeys:
                await ctx.send("Vous n'avez pas de partie en cours !")
                return
            if d_userid not in listeKeys:
                await ctx.send("Cet utilisateur n'a pas de partie en cours !")
                return
            if argent_int > game[MO_userid]["metal"]:
                await ctx.send("Vous n'avez pas assez de bouts de métaux!")
                return
            game[MO_userid]["metal"] -= argent_int
            game[d_userid]["metal"] += argent_int
            await ctx.send(f"Vous avez donné {argent} bouts de métaux à {member.name} !")
            with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                json.dump(game, jsonFile, indent=4)
        if transfermethod == "wood":
            MO_userid = str(ctx.message.author.id)
            d_userid = str(member.id)
            game = reader("/home/rix56/pycharm/BOT/jsondata/game.json")
            listeKeys = list(game.keys())

            argent_int = { True: argent, False: 0 }[
                0 < argent <= 10000]  # on utilise un ternary opérateur pour vérifié que argent est supérieur à 0 et inférieur ou égale à 10 000
            if argent_int == 0:
                await ctx.send("Je ne sais pas faire ça '_'")
                return

            if MO_userid not in listeKeys:
                await ctx.send("Vous n'avez pas de partie en cours !")
                return
            if d_userid not in listeKeys:
                await ctx.send("Cet utilisateur n'a pas de partie en cours !")
                return
            if argent_int > game[MO_userid]["bois"]:
                await ctx.send("Vous n'avez pas assez de bûches de bois !")
                return
            game[MO_userid]["bois"] -= argent_int
            game[d_userid]["bois"] += argent_int
            await ctx.send(f"Vous avez donné {argent} bûches de bois à {member.name} !")
            with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                json.dump(game, jsonFile, indent=4)
        if transfermethod == "money":
            MO_userid = str(ctx.message.author.id)
            d_userid = str(member.id)
            game = reader("/home/rix56/pycharm/BOT/jsondata/game.json")
            listeKeys = list(game.keys())

            argent_int = { True: argent, False: 0 }[
                0 < argent <= 10000]  # on utilise un ternary opérateur pour vérifié que argent est supérieur à 0 et inférieur ou égale à 10 000
            if argent_int == 0:
                await ctx.send("Je ne sais pas faire ça '_'")
                return

            if MO_userid not in listeKeys:
                await ctx.send("Vous n'avez pas de partie en cours !")
                return
            if d_userid not in listeKeys:
                await ctx.send("Cet utilisateur n'a pas de partie en cours !")
                return
            if argent_int > game[MO_userid]["argent_du_village"]:
                await ctx.send("Vous n'avez pas assez d'argent !")
                return
            game[MO_userid]["argent_du_village"] -= argent_int
            game[d_userid]["argent_du_village"] += argent_int
            await ctx.send(f"Vous avez donné {argent} € à {member.name} !")
            with open("/home/rix56/pycharm/BOT/jsondata/game.json", 'w', encoding='utf8') as jsonFile:
                json.dump(game, jsonFile, indent=4)



def setup(client):
    client.add_cog(Jeu(client))

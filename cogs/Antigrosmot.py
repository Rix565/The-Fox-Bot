# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from jedit import *
import bot

actived = False

class Anti_gros_mots(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="Information sur ce module")
    async def infoantigrosmots(self, ctx):
        await ctx.send("Ce module permet d'éliminer les gros mots connu par le développeur.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == bot.client.user:
            return
        if actived == True:
            global serverid
            serverslist = reader("/home/rix56/pycharm/BOT/jsondata/servers.json")
            chances = reader("/home/rix56/pycharm/BOT/jsondata/grosmots.json")
            userid = str(message.author.id)
            try:
                serverid = str(message.guild.id)
            except:
                pass
            try:
                if serverid not in [k for k in serverslist.keys()]:
                    print("Enresgistred server")
                    serverslist[serverid] = { "activedantigrosmots?": "Désactivé" }
                    with open("/home/rix56/pycharm/BOT/jsondata/servers.json", 'w', encoding='utf8') as jsonFile:
                        json.dump(serverslist, jsonFile, indent=4)
            except:
                pass
            print(f"{[k for k in serverslist.keys()]}\n{[k for k in chances.keys()]}")
            if serverid and userid not in [k for k in chances.keys()]:
                print("Enregistred user")
                chances[serverid][userid] = 5
                with open("/home/rix56/pycharm/BOT/jsondata/grosmots.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(chances, jsonFile, indent=4)
            global member
            member = message.author
            try:
                if serverslist[serverid]["activedantigrosmots?"] == "Activé":
                    for m in ["con", "tg", "ftg", "conard", "connase", "bordel", "conne", "salo", "pokecon", "pd",
                              "pute",
                              "putain", "salopard", "CON", "TG", "FTG", "CONARD", "CONNASSE", "BORDEL", "CONNE", "SALO",
                              "POKECON", "PD", "PUTE", "PUTAIN", "SALOPARD"]:
                        if m in message.content:
                            if message.guild.id == 595218682670481418:
                                await message.channel.send("Ce serveur à été banni de l'anti-gros mots.Merci !")
                                return
                            chances[serverid][userid] -= 1
                            with open("/home/rix56/pycharm/BOT/jsondata/grosmots.json", 'w',
                                      encoding='utf8') as jsonFile:
                                json.dump(chances, jsonFile, indent=4)
                            if chances[serverid][userid] == 0:
                                try:
                                    await message.channel.send(
                                        f"Le membre {member} a été kick car il a mis 5 gros mots sur ce serveur !")
                                    await member.send(
                                        f"Tu as été kick du serveur {message.guild.name} pour avoir mis 5 gros mots sur celui-ci !")
                                    await member.kick
                                    return
                                except:
                                    await message.channel.send(
                                        f"Je n'ai pas pu kick {member} pour avoir mis 5 gros mots sur ce serveur car je n'ai pas les permissions nécessaires ou que cette personne est le propriétaire de ce serveur !")
                                    return
                            await discord.Message.delete(message)
                            await member.send(
                                f"<@!{message.author.id}>, tu n'as pas le droit de mettre ce **gros mot !** :rage: ! Il te reste encore **{chances[serverid][userid]}** chances pour ne plus mettre de mots de ce gerre !")
            except:
                await message.channel.send("Je n'ai pas pu utiliser mon anti-gros mots !")


def setup(client):
    client.add_cog(Anti_gros_mots(client))

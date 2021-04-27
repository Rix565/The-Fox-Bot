import discord
from discord.ext import commands
from jedit import *

class Module_Manager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="Menu de activation/désactivation de fonctions")
    async def options(self, ctx):
        if not ctx.guild:
            return
        serverslist = reader("/home/rix56/pycharm/BOT/jsondata/servers.json")
        serverid = str(ctx.guild.id)
        listkeys = serverslist.keys()
        if serverid not in listkeys:
            print("Enresgistred server")
            serverslist[serverid] = {"activedantigrosmots?": "Désactivé"}
            with open("/home/rix56/pycharm/BOT/jsondata/servers.json", 'w', encoding='utf8') as jsonFile:
                json.dump(serverslist, jsonFile, indent=4)
        options_embed = discord.Embed(title="Options de The Fox Bot", color=0x23272A)
        options_embed.add_field(name="Fonction anti-gros mots **[INDISPONIBLE]**", value=f"État : **__{serverslist[serverid]['activedantigrosmots?']}__**\n(Faites +antigrosmots pour activer/désactiver cette fonction, mais il faut être administrateur pour cela.)", inline=False)
        await ctx.send(embed=options_embed)

    @commands.command(description="Activer/Désactiver la fonction anti-gros mots")
    @commands.has_permissions(administrator=True)
    async def antigrosmots(self, ctx):
        serverslist = reader("/home/rix56/pycharm/BOT/jsondata/servers.json")
        serverid = str(ctx.guild.id)
        listkeys = serverslist.keys()
        if serverid not in listkeys:
            print("Enresgistred server")
            serverslist[serverid] = { "activedantigrosmots?": "Désactivé","activednocommands": "Désactivé"}
            with open("/home/rix56/pycharm/BOT/jsondata/servers.json", 'w', encoding='utf8') as jsonFile:
                json.dump(serverslist, jsonFile, indent=4)
        if serverslist[serverid]['activedantigrosmots?'] == "Désactivé":
            serverslist[serverid]['activedantigrosmots?'] = "Activé"
            with open("/home/rix56/pycharm/BOT/jsondata/servers.json", 'w', encoding='utf8') as jsonFile:
                json.dump(serverslist, jsonFile, indent=4)
            await ctx.send("La fonction anti-gros mots à été activé")
            return
        if serverslist[serverid]['activedantigrosmots?'] == "Activé":
            serverslist[serverid]['activedantigrosmots?'] = "Désactivé"
            with open("/home/rix56/pycharm/BOT/jsondata/servers.json", 'w', encoding='utf8') as jsonFile:
                json.dump(serverslist, jsonFile, indent=4)
            await ctx.send("La fonction anti-gros mots à été désactivé")
            returnadministrator

    @commands.command(description="Activer/Désactiver la fonction commande invalide")
    @commands.has_permissions(administrator=True)
    async def commandeinvalide(self, ctx):
        serverslist = reader("/home/rix56/pycharm/BOT/jsondata/servers.json")
        serverid = str(ctx.guild.id)
        listkeys = serverslist.keys()
        if serverid not in listkeys:
            print("Enresgistred server")
            serverslist[serverid] = { "activedantigrosmots?": "Désactivé","activednocommands": "Désactivé"}
            with open("/home/rix56/pycharm/BOT/jsondata/servers.json", 'w', encoding='utf8') as jsonFile:
                json.dump(serverslist, jsonFile, indent=4)
        if serverslist[serverid]['activednocommands'] == "Désactivé":
            serverslist[serverid]['activednocommands'] = "Activé"
            with open("/home/rix56/pycharm/BOT/jsondata/servers.json", 'w', encoding='utf8') as jsonFile:
                json.dump(serverslist, jsonFile, indent=4)
            await ctx.send("La fonction anti-gros mots à été activé")
            return
        if serverslist[serverid]['activednocommands'] == "Activé":
            serverslist[serverid]['activednocommands'] = "Désactivé"
            with open("/home/rix56/pycharm/BOT/jsondata/servers.json", 'w', encoding='utf8') as jsonFile:
                json.dump(serverslist, jsonFile, indent=4)
            await ctx.send("La fonction anti-gros mots à été désactivé")
            return
    @commands.Cog.listener()
    async def on_message(self, message):
        global serverid
        serverslist = reader("/home/rix56/pycharm/BOT/jsondata/servers.json")
        listkeys = serverslist.keys()
        try:
            serverid = str(message.guild.id)
        except:
            pass
        try:
            if serverid not in listkeys:
                print("Enresgistred server")
                serverslist[serverid] = { "activedantigrosmots?": "Désactivé", "activednocommands": "Désactivé"}
                with open("/home/rix56/pycharm/BOT/jsondata/servers.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(serverslist, jsonFile, indent=4)
        except:
            pass


def setup(client):
    client.add_cog(Module_Manager(client))
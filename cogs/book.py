from discord.ext import commands
import discord, os
from jedit import *
import mkdir, asyncio, random

class Book(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(description="Lire/Écrire/Télécharger des bouquins")
    async def book(self, ctx, choice=None, *, data=None):
        booksdb = reader("/home/rix56/pycharm/BOT/jsondata/books.json")
        if choice is None:
            await ctx.send("Séléctionnez un de ces modes : read(lire dans un bouquin à l'aide de son id), write(pour écrire un bouquin, vous obtiendrez son id), download(pour télécharger un bouquin à l'aide de son id, il sera envoyé sur le serveur).")
            return
        if choice == "write":
            if data is None:
                await ctx.send("Vous n'avez pas mis quoi écrire !")
                return
            id = str(os.urandom(random.randint(4, 12)))
            for x in ["b", "'", '"', "/", '\\']:
                id = id.split(x)
                id = ''.join(id)
            member = ctx.message.author
            booksdb[id] = {"content": data, "author": f"{member}", "id": f"{id}"}
            with open("/home/rix56/pycharm/BOT/jsondata/books.json", 'w', encoding='utf8') as jsonFile:
                json.dump(booksdb, jsonFile, indent=4)
            await ctx.send(f"Vous avez écrit dans un bouquin ! ID du bouquin : {id}")
        if choice == "read":
            if data is None:
                await ctx.send("Vous n'avez pas mis une ID !")
                return
            id = data
            listkeys = booksdb.keys()
            if id not in listkeys:
                await ctx.send("ID non trouvée !")
                return
            embed = discord.Embed(title=f"Lecteur de livre", color=0xF1C40F)
            embed.add_field(name="ID du bouquin", value=booksdb[id]["id"])
            embed.add_field(name="Auteur du bouquin", value=booksdb[id]["author"])
            embed.add_field(name="Contenu du bouquin", value=booksdb[id]["content"])
            embed.set_footer(
                text=f'En réponse à {ctx.message.author.name} - Créé par Rix56',
                icon_url=ctx.message.author.avatar_url
            )
            await ctx.send(embed=embed)
        if choice == "download":
            if data is None:
                await ctx.send("Vous n'avez pas mis une ID !")
                return
            id = data
            listkeys = booksdb.keys()
            if id not in listkeys:
                await ctx.send("ID non trouvée !")
                return
            mkdir.mkdir("tmp-book")
            with open("/home/rix56/pycharm/BOT/tmp-book/tmp.txt", "x") as fichier:
                fichier.write(f"ID du bouquin : {booksdb[id]['id']}\n\nAuteur du bouquin : {booksdb[id]['author']}\n\nContenu du bouquin : {booksdb[id]['content']}\n\n\nFichier généré par The Fox Bot Books.")
                fichier.close()
            await asyncio.sleep(0.2)
            await ctx.send("Le livre est en train d'être envoyé...")
            await ctx.send(file=discord.File("/home/rix56/pycharm/BOT/tmp-book/tmp.txt", filename="book.txt"))
            os.remove("/home/rix56/pycharm/BOT/tmp-book/tmp.txt")
            os.removedirs("/home/rix56/pycharm/BOT/tmp-book")
def setup(client):
    client.add_cog(Book(client))
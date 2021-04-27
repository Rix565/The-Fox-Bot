from discord.ext import commands
import discord
import mkdir, os
import asyncio
from jedit import *

class Autres_commandes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description="Le bot répète ce que vous dites")
    async def repete(self, ctx, *, arg1):
        repete_embed = discord.Embed(title="Répété", color=0x3498DB)
        repete_embed.set_footer(text=f'En réponse à {ctx.message.author.name} - Créé par Rix56', icon_url=ctx.message.author.avatar_url)
        repete_embed.add_field(name="Texte :", value=arg1, inline=False)
        await ctx.send(embed=repete_embed)

    @commands.command(description="Comment créer un bot avec Discord.py")
    async def how_2_build_a_bot_with_discord_py(self, ctx):
        embed = discord.Embed(title="Comment créer un bot en discord.py", color=0x11806A)
        embed.set_footer(text=f'En réponse à {ctx.message.author.name} - Créé par Rix56', icon_url=ctx.message.author.avatar_url)
        embed.add_field(name="Voici ce que je te dit :", value="Oh , alors comme ça on veut faire un **bot** en **Discord.py ?** Alors je te conseille ce **lien :** https://discordpy.readthedocs.io/en/latest/api.html (par contre le guide est en anglais)",inline=False)
        await ctx.send(embed=embed)
    @commands.command(description="Pour envoyer un texte en mp à quelqu'un...")
    async def envoyer_un_texte(self, ctx, user: discord.Member, *, message):
        if user.id == 700046053029838878:
            await ctx.send("Vous ne pouvez pas faire ça sur moi !")
            return
        if not ctx.message.guild:
            await ctx.send("Vous ne pouvez pas faire ça dans les messages privés.")
        else:
            await ctx.send(f"{ctx.message.author.name}, le message a été envoyé à {user.mention}")
            await user.send(f"Voici un message pour vous...{message}")

    @commands.command(description="Pour envoyer un texte en fichier en mp à quelqu'un... **(UNIQUEMENT PREMIUM)**")
    async def envoyer_un_texte_dans_un_fichier(self, ctx, user: discord.Member, *, message):
        UserId = str(ctx.message.author.id)
        premium = reader("/home/rix56/pycharm/BOT/jsondata/premium.json")
        if premium[UserId] == ":white_check_mark:":
            if user.id == 700046053029838878:
                await ctx.send("Vous ne pouvez pas faire ça sur moi !")
                return
            if not ctx.message.guild:
                await ctx.send("Vous ne pouvez pas faire ça dans les messages privés.")
            else:
                await ctx.send(f"{ctx.message.author.name}, le message a été envoyé à {user.mention}")
                await user.send(f"Voici un message pour vous...Il est en train d'être envoyé...")
                mkdir.mkdir("tmp")
                with open("/home/rix56/pycharm/BOT/tmp/tmp.txt", "x") as fichier:
                    fichier.write(message)
                    fichier.close()
                await asyncio.sleep(0.2)
                await user.send(file=discord.File("/home/rix56/pycharm/BOT/tmp/tmp.txt", filename="message.txt"))
                os.remove("/home/rix56/pycharm/BOT/tmp/tmp.txt")
                os.removedirs("/home/rix56/pycharm/BOT/tmp")
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

    @commands.command(description="Faire en sorte que le bot envoie un message que tu as défini et supprime le message lorsque tu as exécuté la commande **(UNIQUEMENT PREMIUM)**")
    async def say_anonyme(self, ctx, *, msg):
        UserId = str(ctx.message.author.id)
        premium = reader("/home/rix56/pycharm/BOT/jsondata/premium.json")
        if premium[UserId] == ":white_check_mark:":
            await ctx.send(msg)
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
    @commands.command(description="Faire en sorte que le bot dise quelque chose")
    async def say(self, ctx, *, msg):
        await ctx.send(f"Voici un message de {ctx.message.author.name} : {msg}")

def setup(client):
    client.add_cog(Autres_commandes(client))

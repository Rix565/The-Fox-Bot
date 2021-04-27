from discord.ext import commands
import discord


class Commandes_utiles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description="La version du bot")
    async def ver(self, ctx):
        ver_embed = discord.Embed(title="Fox API version information", color=0xE67E22)
        ver_embed.set_footer(text=f'En réponse à {ctx.message.author.name} - Créé par Rix56',
                             icon_url=ctx.message.author.avatar_url)
        ver_embed.add_field(name="Version :",
                            value=f"**Fox API v3 JSON release** \nVersion de discord.py : {discord.__version__}\nLien pour inviter le bot : https://discordapp.com/api/oauth2/authorize?client_id=700046053029838878&permissions=8&scope=bot",
                            inline=False)
        ver_embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=ver_embed)

    @commands.command(description="La présentation du bot")
    async def presentation(self, ctx):
        pre_embed = discord.Embed(title="La présentation de Fox API", color=0xE74C3C)
        pre_embed.set_footer(text=f'En réponse à {ctx.message.author.name} - Créé par Rix56',
                             icon_url=ctx.message.author.avatar_url)
        pre_embed.add_field(name="Présentation :",
                            value="Bonjour ! Je suis FoxAPI , un bot créé en python.py et fait avec amouuurrr ! UwU !\nMon prefix : + et ~\nRix56 dit merci à ՇՎρԵ de l'avoir aider à faire une refonte générale de ce Bot pour le rendre compatible avec des commandes.",
                            inline=False)
        await ctx.send(embed=pre_embed)
    @commands.command(description="Le changelog du bot")
    async def changelog(self, ctx):
        ch_embed = discord.Embed(title="Changelog de Fox API", color=0x95A5A6)
        ch_embed.set_footer(text=f"En réponse à {ctx.message.author.name} - Créé par Rix56 - Tous les changelogs sont disponible à l'adresse suivante : https://github.com/Rix565/foxbot-changelog/blob/master/README.md",
                            icon_url=ctx.message.author.avatar_url)
        ch_embed.add_field(name="Le changelog :",
                           value="**Changelog 3.0.1** :\n-Mise à jour des commandes rank , money_recup , et du giveaway d'argent pour les rendre plus jolis.\n\n**Changelog 3.0.2** :\n-Changement du prefix principal en +\n\n**Changelog 3.0.3** :\n-Ajout de commandes pour rechercher sur Internet.\n\n**Changelog 3.1.0** :\n-Modification de Rank pour afficher l'image de profil de l'utilisateur qui a lancé la commande\n-Ajout de la commande avatar pour voir son avatar\n\n**Changelog 3.2.0** : \n-Ajout de la catégorie Maltraitance\n-Ajout de la commande baiser , baffe , et de discord_logs , **UNIQUEMENT** pour les admins du bot\n\n**Changelog 3.2.5** :\n-Ajout des commandes suggestion, avis, transfert, say\n-Modification de la commande changelog pour mettre les titres des changelogs en gras\n\n**Changelog 3.5.0 :**\n-Ajout de l'anti-gros mots , de la commande +oof , et de la commande +module_info\n\n**Changelog 3.6.0 :**\n-Ajout du système d'activation/désactivation de fonctions (UNIQUEMENT POUR LES ADMINS DU SERVEUR)\n-Modification de l'anti-gros mots\n-Ajout de la commande +PIKA",
                           inline=False)
        await ctx.send(embed=ch_embed)

    @commands.command(description="Ton avatar")
    async def avatar(self, ctx, user=None):
        global member
        if user is not None:
            for x in ['<','@','>', '!']:
                    user = user.split(x)
                    user = ' '.join(user)
            try:
                member = ctx.guild.get_member(int(user))
            except:
                member = ctx.guild.get_member(user)
        try:
            avatar_embed = discord.Embed(title=f"Avatar de {member.name}")
            avatar_embed.set_image(url=member.avatar_url)
            await ctx.send(embed=avatar_embed)
        except:
            avatar_embed = discord.Embed(title=f"Avatar de {ctx.message.author.name}")
            avatar_embed.set_image(url=ctx.message.author.avatar_url)
            await ctx.send(embed=avatar_embed)

    @commands.command(description="Envoyer une suggestion")
    async def suggestion(self, ctx, *, msg):
        channel = self.client.get_channel(715193946204143717)
        await channel.send(f"Une idéé d'un serveur a été envoyé !\nNom du serveur : {ctx.guild}\nAuteur de la suggestion : {ctx.author}\nSa suggestion est : {msg}")
        await ctx.send(f"L'idéé {msg} a bel est bien été envoyé !")

    @commands.command(description="Envoyer son avis au niveau du bot")
    async def avis(self, ctx, *, msg):
        channel = self.client.get_channel(716302013012639824)
        await channel.send(f"Un avis a été envoyé de la part de {ctx.author} sur le serveur {ctx.guild} ! Voici son avis :\n{msg}")
        await ctx.send("Ton avis a bel est bien été envoyé !")

    @commands.command(description="Envoyer un report de bug")
    async def report_bug(self, ctx, *, msg):
        channel = self.client.get_channel(717717616713662464)
        await channel.send(
            f"Un bug a été découvert par {ctx.author} sur le serveur {ctx.guild},  voici le bug :\n{msg}")
        await ctx.send("Ton report de bug a bel est bien été envoyé !")

    @commands.command(description="Serveur officiel du bot")
    async def official_server(self, ctx):
        official_server_embed = discord.Embed(title="Serveur officiel du bot", description="Serveur officiel (Report bug , discussion avec les développeurs , etc...) https://discord.gg/YqKghAK", color=0xC27C0E)
        await ctx.send(embed=official_server_embed)
def setup(client):
    client.add_cog(Commandes_utiles(client))

from discord.ext import commands


class Recherche(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description="Rechercher sur google")
    async def google(self, ctx, *, search=None):
        if search is None:
            await ctx.send("Tu n'a pas mis quoi rechercher sur google !")
        else:
            await ctx.send(
                f"Voici ta recherche : (si tu vois des trucs pas pris en compte dans l'url fait des + gerre : how+to+basic) https://www.google.com/search?q={search}")

    @commands.command(description="Rechercher sur qwant")
    async def qwant(self, ctx, *, search=None):
        if search is None:
            await ctx.send("Tu n'a pas mis quoi rechercher sur qwant !")
        else:
            await ctx.send(
                f"Voici ta recherche : (si tu vois des trucs pas pris en compte dans l'url fait des + gerre : how+to+basic) https://www.qwant.com/?q={search}&t=web")

    @commands.command(description="Rechercher sur bing")
    async def bing(self, ctx, *, search=None):
        if search is None:
            await ctx.send("Tu n'a pas mis quoi rechercher sur bing !")
        else:
            await ctx.send(
                f"Voici ta recherche : (si tu vois des trucs pas pris en compte dans l'url fait des + gerre : how+to+basic) https://www.bing.com/search?q={search}")

    @commands.command(description="Rechercher sur ebay")
    async def ebay(self, ctx, *, search=None):
        if search is None:
            await ctx.send("Tu n'a pas mis quoi rechercher sur ebay !")
        else:
            await ctx.send(
                f"Voici ta recherche : (si tu vois des trucs pas pris en compte dans l'url fait des + gerre : how+to+basic) https://www.ebay.fr/sch/{search}")

    @commands.command(description="Rechercher sur ebay")
    async def youtube(self, ctx, *, search=None):
        if search is None:
            await ctx.send("Tu n'a pas mis quoi rechercher sur youtube !")
        else:
            await ctx.send(
                f"Voici ta recherche : (si tu vois des trucs pas pris en compte dans l'url fait des + gerre : how+to+basic) https://www.youtube.com/results?search_query={search}")

    @commands.command(description="Rechercher sur reddit")
    async def reddit(self, ctx, *, search=None):
        if search is None:
            await ctx.send("Tu n'a pas mis quoi rechercher sur reddit !")
        else:
            await ctx.send(
                f"Voici ta recherche : (si tu vois des trucs pas pris en compte dans l'url fait des + gerre : how+to+basic) https://www.reddit.com/search/?q={search}")


def setup(client):
    client.add_cog(Recherche(client))

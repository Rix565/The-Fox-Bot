from discord.ext import commands


class Maltraitance(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="Si je suis méchant , donne moi une baffe.")
    async def baffe(self, ctx):
        await ctx.send("Aie ! Ça fait mal ! J'ai été méchant ?")

    @commands.command(description="Beurk !")
    async def baiser(self, ctx):
        await ctx.send("AHHH ! JE VEUX PAS QUE ON SE BAISE ! NOOON ! OU J'APPELLE LE 17 !")

def setup(client):
    client.add_cog(Maltraitance(client))

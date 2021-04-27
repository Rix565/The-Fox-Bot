import discord
import random
from discord.ext import commands

colors = {
    'DEFAULT': 0x000000,
    'WHITE': 0xFFFFFF,
    'AQUA': 0x1ABC9C,
    'GREEN': 0x2ECC71,
    'BLUE': 0x3498DB,
    'PURPLE': 0x9B59B6,
    'LUMINOUS_VIVID_PINK': 0xE91E63,
    'GOLD': 0xF1C40F,
    'ORANGE': 0xE67E22,
    'RED': 0xE74C3C,
    'GREY': 0x95A5A6,
    'NAVY': 0x34495E,
    'DARK_AQUA': 0x11806A,
    'DARK_GREEN': 0x1F8B4C,
    'DARK_BLUE': 0x206694,
    'DARK_PURPLE': 0x71368A,
    'DARK_VIVID_PINK': 0xAD1457,
    'DARK_GOLD': 0xC27C0E,
    'DARK_ORANGE': 0xA84300,
    'DARK_RED': 0x992D22,
    'DARK_GREY': 0x979C9F,
    'DARKER_GREY': 0x7F8C8D,
    'LIGHT_GREY': 0xBCC0C0,
    'DARK_NAVY': 0x2C3E50,
    'BLURPLE': 0x7289DA,
    'GREYPLE': 0x99AAB5,
    'DARK_BUT_NOT_BLACK': 0x2C2F33,
    'NOT_QUITE_BLACK': 0x23272A
}


class Aide(commands.Cog):

    def __init__(self, CYPT):
        self.CYPT = CYPT

    @commands.command(
        name='help',
        description="La commande d'aide!"
    )
    async def help(self, ctx, cog='all'):

        await ctx.author.send("Voici mon aide :")

        color_list = [c for c in colors.values()]
        help_embed = discord.Embed(
            title='Aide de Fox API',
            color=random.choice(color_list)
        )
        help_embed.set_thumbnail(url=self.CYPT.user.avatar_url)
        help_embed.set_footer(
            text=f'En réponse à {ctx.message.author.name} - Créé par Rix56',
            icon_url=ctx.message.author.avatar_url
        )

        cogs = [c for c in self.CYPT.cogs.keys()]

        if cog == 'all':
            for cog in cogs:

                cog_commands = self.CYPT.get_cog(cog).get_commands()
                commands_list = ''
                for comm in cog_commands:
                    commands_list += f'**{comm.name}** - *{comm.description}*\n'

                help_embed.add_field(
                    name=cog,
                    value=commands_list,
                    inline=False
                ).add_field(
                    name='\u200b', value='\u200b', inline=False
                )

            pass
        else:

            lower_cogs = [c.lower() for c in cogs]

            if cog.lower() in lower_cogs:

                commands_list = self.CYPT.get_cog(cogs[lower_cogs.index(cog.lower())]).get_commands()
                help_text = ''

                for command in commands_list:
                    help_text += f'```{command.name}```\n' \
                                 f'**{command.description}**\n\n'

                    if len(command.aliases) > 0:
                        help_text += f'**Aliases :** `{"`, `".join(command.aliases)}`\n\n\n'
                    else:

                        help_text += '\n'

                    help_text += f'Format: `@{self.CYPT.user.name}#{self.CYPT.user.discriminator}' \
                                 f' {command.name} {command.usage if command.usage is not None else ""}`\n\n\n\n'

                help_embed.description = help_text
            else:

                await ctx.send('Invalid cog specified.\nUse `help` command to list all cogs.')
                return

        await ctx.author.send(embed=help_embed)
        await ctx.send("Aide envoyé en message privé !")

        return


def setup(CYPT):
    CYPT.add_cog(Aide(CYPT))

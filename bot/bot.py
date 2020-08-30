from os import getenv
import random as rd

import discord
from discord.ext.commands import Bot, Cog, command

from keep_alive import keep_alive
from help import BotHelpCommand


TOKEN = getenv("DISCORD_TOKEN")
PREFIX = getenv("PREFIX") or "r/"


class MainCog(Cog):
    """Commands to generate things related to 'random'"""

    @command()
    async def ping(self, ctx):
        """Checks latency"""

        await ctx.send(f"Pong; {round(bot.latency * 1000, 2)}ms")

    @command(name="int", aliases=["i", "integer"])
    async def randint(self, ctx, start: int = 0, end: int = 100):
        """get random integer between 'start' and 'end'

        start defaults to 0, end defaults to 100
        """
        # if not isinstance(start, int) or not isinstance(end, int):
        #     await ctx.send('Arguments must all be integers!')
        #     return
        integer = rd.randint(int(start), int(end))
        await ctx.send(integer)

    @command(aliases=["c", "ch", "choose"])
    async def choice(self, ctx, *choices):
        """choose something from a list (separate by space)"""
        await ctx.send(rd.choice(choices))

    @command(aliases=["sh", "shuf"])
    async def shuffle(self, ctx, *your_list):
        """shuffle a list separated by spaces"""
        your_list = list(your_list)
        rd.shuffle(your_list)
        await ctx.send(" ".join(your_list))


bot = Bot(command_prefix=PREFIX, help_command=None)

bot.add_cog(MainCog())
bot.help_command = BotHelpCommand()

keep_alive()
bot.run(TOKEN)

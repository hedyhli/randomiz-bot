from os import getenv
import random as rd
import asyncio

import discord
from discord.ext.commands import Bot, Cog, command

from help import BotHelpCommand


TOKEN = getenv("DISCORD_TOKEN")
PREFIX = getenv("PREFIX") or "r/"


class MainCog(Cog):
    """Commands to generate things related to 'random'"""

    @command()
    async def ping(self, ctx):
        """Checks latency"""

        await ctx.send(f"Pong; {round(bot.latency * 1000, 2)}ms")

    @command(aliases=["info", "bot"])
    async def about(self, ctx):
        """Returns info about the bot"""

        embed = discord.Embed(
            title="Randomiz bot",
            description="A 'random' bot that helps you to get random integers, choices, rolls dice, flips coins, and more.\nCheck it out on [github](https://github.com/hedythedev/randomiz-bot/) or join the [support server](https://discord.gg/uwyYpt9) to learn more.",
            color=0x41C03F,
        )

        await ctx.send(embed=embed)

    @command(name="int", aliases=["i", "integer"])
    async def randint(self, ctx, start: int = 0, end: int = 100):
        """get random integer between 'start' and 'end'

        start defaults to 0, end defaults to 100 - which means calling `r/int` will give you a random integer from 0 to 100

        **What is an integer?**
        > a number which is not a fraction; a whole number.

        **Examples**
        1. `r/int 1 50` - random integer between (including) 1 to 50
        2. `r/int 100 1000` - random integer between (including) 100 to 1,000
        3. `r/int -100 100` - negatives should work too
        """
        # if not isinstance(start, int) or not isinstance(end, int):
        #     await ctx.send('Arguments must all be integers!')
        #     return
        integer = rd.randint(int(start), int(end))
        await ctx.send(integer)

    @command(aliases=["ch", "choose"])
    async def choice(self, ctx, *choices):
        """choose something from a list (separate by space)

        **Examples**
        1. `r/ch apples bananas grapes`
        2. `r/ch hi hello`
        3. `r/ch Alice Bob`
        """
        await ctx.send(rd.choice(choices))

    @command(aliases=["sh", "shuf"])
    async def shuffle(self, ctx, *your_list):
        """shuffle a list separated by spaces

        **Examples**
        1. `r/shuffle a b c`
        2. `r/shuffle this is a cool bot`
        """
        your_list = list(your_list)
        rd.shuffle(your_list)
        await ctx.send(" ".join(your_list))

    @command(aliases=["flip", "co"])
    async def coin(self, ctx):
        """Flips a coin and tells you if it's heads or tails

        **Examples**
        1. `r/flip` (this will give you either heads or tails)
        """

        msg = await ctx.send(":coin: Flipping a coin...")
        await asyncio.sleep(1.5)
        await msg.edit(content=f":sparkles: {rd.choice(['Heads', 'Tails'])}!")

    @command(aliases=["roll"])
    async def dice(self, ctx, sides: int = 6):
        """Rolls a x-sided die (6 sides by default)

        **Examples**
        1. `r/roll` - roll a 6-sided die
        2. `r/roll 12` - roll a 12-sided die

        **Die vs. Dice?**
        > in modern standard English dice is both the singular and the plural: 'throw the dice' could mean a reference to either one or more than one dice.
        But here, I normally stick to 'die' when it's singular, 'dice' when it's plural.
        """

        if sides < 2:
            return await ctx.send(
                f"Hmm... I don't think a {sides} sided die is possible"
            )

        result = str(rd.randint(1, sides))
        await ctx.send(
            "I rolled a " + str(sides) + " sided die and got **" + result + "**!"
        )


bot = Bot(command_prefix=PREFIX, help_command=None)

bot.add_cog(MainCog())
bot.help_command = BotHelpCommand()

bot.run(TOKEN)

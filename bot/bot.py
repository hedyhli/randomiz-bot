from os import environ
import random as rd
import re

import discord
from discord.ext.commands import Bot, Cog, command


TOKEN = environ.get('DISCORD_TOKEN')


bot = Bot(command_prefix=';')

class Misc(Cog):
    """Miscellanous Commands"""

    @command(name='say', aliases=['s', 'msg', 'speak', 'talk'])
    async def say(self, ctx, *words):
        """Say something for me"""
        await ctx.send(' '.join(words))
    

class Main(Cog):
    """Commands to generate things related to 'random'"""

    @command(name='int', aliases=['i', 'integer'])
    async def random_int(self, ctx, start: int=0, end: int=100):
        """get random integer between 'start' and 'end'
        
        start defaults to 0, end defaults to 100
        """
        # if not isinstance(start, int) or not isinstance(end, int):
        #     await ctx.send('Arguments must all be integers!')
        #     return
        integer = rd.randint(int(start), int(end))
        await ctx.send(integer)
    
    @command(name='choice', aliases=['c', 'ch', 'choose'])
    async def random_choice(self, ctx, *choices):
        """choose something from a list (separate by space)"""
        await ctx.send(rd.choice(choices))

    @command(name='shuffle', aliases=['sh', 'shuf'])
    async def random_shuffle(self, ctx, *your_list):
        """shuffle a list separated by spaces"""
        your_list = list(your_list)
        rd.shuffle(your_list)
        await ctx.send(' '.join(your_list))


bot.add_cog(Main())
bot.add_cog(Misc())
bot.run(TOKEN)
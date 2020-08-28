from os import environ
import random as rd
import re

import discord
from discord.ext.commands import Bot, Cog, command


TOKEN = environ.get('DISCORD_TOKEN')


bot = Bot(command_prefix=';', help_command=None)

class Misc(Cog):
    """Miscellanous Commands"""

    @command(aliases=['s', 'msg', 'speak', 'talk'])
    async def say(self, ctx, *words):
        """Say something for me"""
        await ctx.send(' '.join(words))
      
    @command()
    async def ping(self, ctx):
        """Checks latency"""

        await ctx.send(f'Pong; {round(bot.latency * 1000, 2)}ms')
    
    @command()
    async def help(self, ctx):
        """Sends a help message"""

        embed = discord.Embed(
            title='Help for The Randomiz Bot',
            description='A utility bot that provides you commands to get random integers, choices, and more\nUse `help <command>` to get help on a specific command (WIP).',
            colour=0x41c03f
        ).add_field(
            name=f'\n---\n',
            value='**Main Commands**'
        ).add_field(
            name=f'`int`',
            value='*Get random integer*',
            inline=True
        ).add_field(
            name=f'`choice`',
            value='*Choose an item from a list (separate using space)*',
            inline=True
        ).add_field(
            name=f'`shuffle`',
            value='*Shuffle a list separated by space*',
            inline=True
        ).add_field(
            name='---',
            value='**Other Commands**'
        ).add_field(
            name=f'`help`',
            value='*Shows this message*',
            inline=True
        ).add_field(
            name=f'`ping`',
            value='*Check the bot\'s latency*',
            inline=True
        ).add_field(
            name='---\n**Still need help?**',
            value='*Join the [bot support server] for additional help*',
            inline=False
        )

        await ctx.send(embed=embed)
    

class Main(Cog):
    """Commands to generate things related to 'random'"""

    @command(name='int', aliases=['i', 'integer'])
    async def randint(self, ctx, start: int=0, end: int=100):
        """get random integer between 'start' and 'end'
        
        start defaults to 0, end defaults to 100
        """
        # if not isinstance(start, int) or not isinstance(end, int):
        #     await ctx.send('Arguments must all be integers!')
        #     return
        integer = rd.randint(int(start), int(end))
        await ctx.send(integer)
    
    @command(aliases=['c', 'ch', 'choose'])
    async def choice(self, ctx, *choices):
        """choose something from a list (separate by space)"""
        await ctx.send(rd.choice(choices))

    @command(aliases=['sh', 'shuf'])
    async def shuffle(self, ctx, *your_list):
        """shuffle a list separated by spaces"""
        your_list = list(your_list)
        rd.shuffle(your_list)
        await ctx.send(' '.join(your_list))


bot.add_cog(Misc())
bot.add_cog(Main())
bot.run(TOKEN)
import os
import random as rd
import re

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix=';')

class Misc(commands.Cog):
    """Miscellanous Commands"""

    @bot.command(name='say', help='say something for me')
    async def say(self, ctx, *args):
        await ctx.send(' '.join(args))
    
    @bot.command(name='rep', help='repeat previous command')
    async def rep(self, ctx):
        if self.messages:
            await ctx.send(self.messages[-1])

class Main(commands.Cog):
    """Commands to generate things related to 'random'"""

    @bot.command(name='int', help="get random integer between \'start\' and \'end\'")
    async def random_int(self, ctx, start, end):
        if not isinstance(start, int) or not isinstance(end, int):
            await ctx.send('Arguments must all be integers!')
            return
        integer = rd.randint(int(start), int(start))
        await ctx.send(integer)
    
    @bot.command(name='choice', help='choose something from a list of choices (separate by space)')
    async def random_choice(self, ctx, *choices):
        await ctx.send(rd.choice(choices))

    #@bot.event
    #async def on_message(self, message):
        #res = re.search(r"$!(.* .*)", message.content)
        #if res:
            #self.messages.append(res.group(1))


bot.add_cog(Main())
bot.run(TOKEN)
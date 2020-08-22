import discord
import asyncio
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["latency"], case_insensitive = True)
    async def ping(self, ctx):
        await ctx.send("Pong! {0}ms".format(round(self.bot.latency, 1)))

def setup(bot):
    bot.add_cog(ping(bot))
import discord
import asyncio
from discord.ext import commands

class server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["support"], case_insensitive = True)
    async def server(self, ctx):
        embed = discord.Embed(
            title = "Support Server",
            url = "https://discord.gg/wwUy65z",
            description = "Click above to join the Fall Guys Bot support server!",
            color = 0x30D8DE)
        embed.set_author(
            name = "Fall Guys Bot",
            icon_url = "https://corard.xyz/assets/bot/icon.png")
        await ctx.send(
            embed = embed)

def setup(bot):
    bot.add_cog(server(bot))
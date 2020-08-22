import discord
import asyncio
import random
from discord.ext import commands

class meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["memes"], case_insensitive = True)
    async def meme(self, ctx):
        
        with open("/root/fg-bot/assets/memes_list.txt") as f:
            memes = [line.strip().split("|") for line in f]
            title, image, permalink = random.choice(memes)

        embed = discord.Embed(
            title = title,
            colour = 0x30d8de,
            url = permalink)
        embed.set_author(
            name = "Fall Guys Bot",
            icon_url = "https://corard.xyz/assets/bot/icon.png")
        embed.set_image(
            url = image)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(meme(bot))
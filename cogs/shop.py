import discord
import asyncio
import random
import datetime
from discord.ext import commands

class shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["items"], case_insensitive = True)
    async def shop(self, ctx):
        
        embed = discord.Embed(
            title = "Featured Shop",
            colour = 0x30d8de)
        embed.set_author(
            name = "Fall Guys Bot",
            icon_url = "https://corard.xyz/assets/bot/icon.png")
        embed.add_field(
            name = "T-Rex",
            value = "Costume Upper",
            inline = True)
        embed.add_field(
            name = "T-Rex",
            value = "Costume Lower",
            inline = True)
        embed.add_field(
            name = "Z-Snap",
            value = "Celebration",
            inline = True)
        embed.set_image(
            url = "https://fgbot.xyz/shop/0822-0825.png")
#        embed.set_footer(
#            text = ("Shop resets in" + )

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(shop(bot))
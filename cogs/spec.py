import discord
import asyncio
from discord.ext import commands

class spec(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["specs", "minspec", "minspecs"], case_insensitive = True)
    async def spec(self, ctx):
        embed = discord.Embed(
            title = "Minimum Requirements:",
            description = "Requires a 64-bit processor and operating system",
            color = 0x30D8DE)
        embed.set_author(
            name = "Fall Guys Bot",
            icon_url = "https://corard.xyz/assets/bot/icon.png")
        embed.add_field(
            name = "OS:", value = "Windows 10 64bit only", inline = True)
        embed.add_field(
            name = "Processor:", value = "Intel Core i5 or AMD equivalent", inline = True)
        embed.add_field(
            name = "Memory:", value = "8 GB RAM", inline = True)
        embed.add_field(
            name = "Graphics:", value = "NVIDIA GTX 660 or AMD Radeon HD 7950", inline = True)
        embed.add_field(
            name = "Network:", value = "Broadband Internet connection", inline = True)
        embed.add_field(
            name = "Storage:", value = "2 GB available space", inline = True)
        embed.add_field(
            name = "Additional Notes:", value = "Gamepad Recommended", inline = True)
        await ctx.send(
            embed = embed)

def setup(bot):
    bot.add_cog(spec(bot))
import discord
import asyncio
from discord.ext import commands

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["infomation", "botinfo"], case_insensitive = True)
    async def info(self, ctx):
        embed = discord.Embed(
            title = "Bot Information",
            color = 0x30D8DE)
        embed.set_author(
            name = "Fall Guys Bot",
            icon_url = "https://corard.xyz/assets/bot/icon.png")
        embed.add_field(
            name = "Version",
            value = "v0.1.0",
            inline = True)
        embed.add_field(
            name = "Bot Owners",
            value = "Corard & Sarc",
            inline = True)
        embed.add_field(
            name = "Bot Developers",
            value = "Corard & Trypo",
            inline = True)
        embed.add_field(
            name = "Total Servers Connected",
            value = (len(self.bot.guilds)),
            inline = False)
        await ctx.send(
            embed = embed)

def setup(bot):
    bot.add_cog(info(bot))
import discord
import asyncio
from discord.ext import commands

class invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["add"], case_insensitive = True)
    async def invite(self, ctx):
        embed = discord.Embed(
            title = "Invite Bot",
            url = "https://discord.com/oauth2/authorize?client_id=744619278992539770&permissions=387136&scope=bot",
            description = "Click above to invite the bot to your server!",
            color = 0x30D8DE)
        embed.set_author(
            name = "Fall Guys Bot",
            icon_url = "https://corard.xyz/assets/bot/icon.png")
        embed.add_field(
            name = "Total Servers Connected",
            value = (len(self.bot.guilds)),
            inline = False)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(invite(bot))
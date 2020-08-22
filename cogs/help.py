import discord
import asyncio
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["commands", "commandlist", "commandslist"], case_insensitive = True)
    async def help(self, ctx):
        embed = discord.Embed(
            title = "Help",
            description = "View all bot commands here!",
            color = 0x30D8DE)
        embed.set_author(
            name = "Fall Guys Bot",
            icon_url = "https://corard.xyz/assets/bot/icon.png")
        embed.add_field(name="<:FGPrefix:745294702210842756> Prefix", value="!fg ", inline=True)
        embed.add_field(name="Example", value="!fg help", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="<:FGHelp:745287881605644431> Help", value="!fg help", inline=True)
        embed.add_field(name="What It Does", value="Shows this menu!", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="<:FGInfo:745289792685735978> Info", value="!fg info", inline=True)
        embed.add_field(name="What It Does", value="Shows basic information about the bot!", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="<:FGRounds:745289792757039184> Rounds", value="!fg rounds", inline=True)
        embed.add_field(name="What It Does", value="Gives details about Fall Guys different rounds!", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="<:FGMeme:745299007135285309> Meme", value="!fg meme", inline=True)
        embed.add_field(name="What It Does", value="Sends a random meme from the r/FallGuysMemes subreddit! (Random from top 10 of past week)", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="<:FGSpec1:745294700667338752> Spec", value="!fg spec", inline=True)
        embed.add_field(name="What It Does", value="Shows the PC hardware requirements for Fall Guys!", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="<:FGSupport:745352162661630083> Server", value="!fg server", inline=True)
        embed.add_field(name="What It Does", value="Gives an invite to the bot support server!", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="<:FGInvite:745321966700986368> Invite", value="!fg invite", inline=True)
        embed.add_field(name="What It Does", value="Gives the invite link for the bot!", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
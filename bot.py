import discord
import asyncio
from discord.ext import commands
import os

prefix = ["!fg ", "!FG ", "!fG ", "!Fg "]
bot = commands.Bot(
    command_prefix = prefix,
    case_insensitive = True,
    owner_id = 466314395677622282)
bot.remove_command('help')

TOKEN = " Token Here "

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for !fg help"))
    print("Online!")
    servers = list(bot.guilds)
    print("Connected on " + str(len(bot.guilds)) + " servers")
    print("Serving " + str(len(bot.users)) + " members!")
    print(" ")

@bot.event
async def on_guild_join(guild):
    print(" Joined " + str(guild.name))
    channel = bot.get_channel(745680840737947669)
    embed = discord.Embed(
        title = "New Server Joined!",
        color = 0x30D8DE)
    embed.set_author(
        name = "Fall Guys Bot",
        icon_url = "https://corard.xyz/assets/bot/icon.png")
    embed.add_field(
        name = "Server Name",
        value = (str(guild.name)),
        inline = True)
    embed.add_field(
        name = "Total Servers Connected",
        value = (len(bot.guilds)),
        inline = True)
    embed.add_field(
        name = "Total Users",
        value = (len(bot.users)),
        inline = False)
    await channel.send(
        embed = embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry! I don't recognise this command, please check `!fg help` for commands.")

for cog in os.listdir(r"/root/fg-bot/cogs"): # Replace With Cogs Folder
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)

        except Exception as e:
            print(f"{cog} connot be loaded!")
            raise e

bot.run(TOKEN)
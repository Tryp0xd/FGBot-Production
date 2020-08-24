import discord
import asyncio
import random
import datetime
from discord.ext import commands
import aiohttp
from bs4 import BeautifulSoup

import sys
import traceback


class shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)



    @commands.command(aliases = ["items"], case_insensitive = True)
    async def shop(self, ctx):

        is_website = "https://fallguysstore.com/"
        Item_names = []
        Items = []
        ItemType = []
        async with aiohttp.ClientSession() as session1:
            async with session1.get(is_website) as resp1:
                soup = BeautifulSoup(await resp1.text(), 'html.parser')
                items = soup.find_all("img", attrs={"loading" : "lazy"}, class_="alignnone")
                for i in range(len(items)):
                    pos1 = items[i]["src"].rfind("/")
                    pos2 = items[i]["src"].rfind(".")
                    curr_item = items[i]['src']
                    Item_names.append(curr_item[pos1+1:pos2].replace("-300x300", "")) 
        for i in range(len(Item_names)):
            l_dash = Item_names[i].rfind("-")
            ItemType.append(Item_names[i][l_dash+1:])
            Items.append(Item_names[i][:l_dash])
            if ItemType[i] == "Upper":
                ItemType[i] = "Costume Upper"
            elif ItemType[i] == "Lower":
                ItemType[i] = "Costume Lower"
            elif ItemType[i] == "Emote":
                ItemType[i] = "Celebration"
            elif ItemType[i] == "Pattern":
                ItemType[i] =  "Skin Pattern"
            elif ItemType[i] == "Faceplate":
                ItemType[i] = "Face Plate"
            elif ItemType[i] == "Colour":
                ItemType[i] = "Skin Colour"
            else:
                ItemType[i] == "Unknown"


        is_file = discord.File("G:\\FGBot-Production-master\\assets\\shop\\FGItemShop.png", filename="image.png")


        print(Items, ItemType) 
        embed = discord.Embed(
            title = "Featured Shop",
            colour = 0x30d8de)
        embed.set_author(
            name = "Fall Guys Bot",
            icon_url = "https://corard.xyz/assets/bot/icon.png")
        embed.add_field(
            name = Items[0],
            value = ItemType[0],
            inline = True)
        embed.add_field(
            name = Items[1],
            value = ItemType[1],
            inline = True)
        embed.add_field(
            name = Items[2],
            value = ItemType[2],
            inline = True)
        embed.set_image(
            url = "attachment://image.png")
#        embed.set_footer(
#            text = ("Shop resets in" + )

        await ctx.send(embed=embed, file=is_file)

def setup(bot):
    bot.add_cog(shop(bot))

import discord
import asyncio
from discord.ext import commands

class rounds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True, aliases = ["round", "maps", "roundlist", "roundslist", "maplist", "mapslist"], case_insensitive = True)
    async def rounds(self, ctx):
 
        names = []
        descs = []
        types = []
        race_types = []
        authors = []
        g_links = []
 
        with open("/root/fg-bot/assets/rounds/fg_data.txt","r") as readData: # Replace with fg_data.txt directory
            mapList = readData.readlines()
            for i in range(len(mapList)):
                currMap = mapList[i].split("|")
                names.append(currMap[1])
                descs.append(currMap[2])
                types.append(currMap[3])
                race_types.append(currMap[4])
                authors.append(currMap[5])
                g_links.append(currMap[6].replace("\n", ""))
 
        pages = 11
        cur_page = 1
        init_embed = discord.Embed(
        title= names[cur_page-1],
        description= descs[cur_page-1],
        colour = 0x30d8de)
        init_embed.set_author(name='Fall Guys Bot',
        icon_url="https://corard.xyz/assets/bot/icon.png")
        init_embed.add_field(name="Map Size", value=types[cur_page-1], inline=True)
        init_embed.add_field(name="Type", value=race_types[cur_page-1], inline=True)
        init_embed.add_field(name="Creator", value= authors[cur_page-1], inline=True)
        init_embed.set_footer(text=f"Page {cur_page}/{pages} - This embed will automatically delete after 60 seconds idle")
        init_embed.set_image(url=g_links[cur_page-1])
            
        message = await ctx.send(embed=init_embed)
 
        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
 
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
 
        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
 
                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    fwd_embed = discord.Embed(
                    title= names[cur_page-1],
                    description= descs[cur_page-1],
                    colour = 0x30d8de)
                    fwd_embed.set_author(name='Fall Guys Bot',
                    icon_url="https://corard.xyz/assets/bot/icon.png")
                    fwd_embed.add_field(name="Map Size", value=types[cur_page-1], inline=True)
                    fwd_embed.add_field(name="Type", value=race_types[cur_page-1], inline=True)
                    fwd_embed.add_field(name="Creator", value= authors[cur_page-1], inline=True)
                    fwd_embed.set_footer(text=f"Page {cur_page}/{pages} - This embed will automatically delete after 60 seconds idle")
                    fwd_embed.set_image(url=g_links[cur_page-1])
                    await message.edit(embed=fwd_embed)
                    await message.remove_reaction(reaction, user)
 
                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    bck_embed = discord.Embed(
                    title= names[cur_page-1],
                    description= descs[cur_page-1],
                    colour = 0x30d8de)
                    bck_embed.set_author(name='Fall Guys Bot',
                    icon_url="https://corard.xyz/assets/bot/icon.png")
                    bck_embed.add_field(name="Map Size", value=types[cur_page-1], inline=True)
                    bck_embed.add_field(name="Type", value=race_types[cur_page-1], inline=True)
                    bck_embed.add_field(name="Creator", value= authors[cur_page-1], inline=True)
                    bck_embed.set_footer(text=f"Page {cur_page}/{pages} - This embed will automatically delete after 60 seconds idle")
                    bck_embed.set_image(url=g_links[cur_page-1])
                    await message.edit(embed=bck_embed)
                    await message.remove_reaction(reaction, user)
                
                else:
                    await message.remove_reaction(reaction, user)
            
            except asyncio.TimeoutError:
                await message.delete()
                break

def setup(bot):
    bot.add_cog(rounds(bot))
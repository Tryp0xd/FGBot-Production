#cog
import discord
import asyncio
from discord.ext import tasks, commands


#for both shop and progress bar
from PIL import Image, ImageDraw

#for shop image
import aiohttp
import aiofiles
from bs4 import BeautifulSoup
import random

#for progress bar
import pytz
from datetime import datetime, date




class refreshData(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		self.refreshData.start()


	@tasks.loop(seconds=60)
	async def refreshData(self):

		path_to = "G:\\FGBot-Production-master\\assets\\"
		UTC = pytz.utc
		curr_date = str(datetime.now(UTC)).split(" ")
		ymd = str(curr_date[0]).split("-")
		time_reset = "15:24"
		if datetime.now(UTC).strftime("%H:%M") == time_reset:
			#progress bar
			progress_path = "progress\\"
			start_fg = date(2020,8,4)
			end_fg = date(2020,8, 27)
			date_rn = date(int(ymd[0]), int(ymd[1]),int(ymd[2]))
			diff_date = end_fg - start_fg
			t_days = end_fg - date_rn
			max_days = int(diff_date.days)
			days_left = int(t_days.days)

			calc_perc = round((max_days-days_left)/max_days, 2) * 100
			print(calc_perc)


			percentage1 = 9.75
			start_x = 311
			start_y = 237
			bottom_y = 363



			sp_image = Image.open(f"{path_to + progress_path}SeasonProgressBase.jpg")

			cp_sp = sp_image.copy()
			progress_fill = ImageDraw.Draw(cp_sp)
			progress_fill.rectangle((start_x,start_y,start_x+round(calc_perc * percentage1, 0), 363), fill=(248,60,163))
			cp_sp.save(f"{path_to + progress_path}SeasonProgress.jpg")

			#website
			path_to_shop = "shop\\"
			is_website = "https://fallguysstore.com/"
			async with aiohttp.ClientSession() as session:
				async with session.get(is_website) as resp:
					soup = BeautifulSoup(await resp.text(), "html.parser")
					items = soup.find_all("img", attrs={"loading" : "lazy"}, class_="alignnone")
					for i in range(len(items)):
						async with aiofiles.open(f"{path_to}{path_to_shop}is{i+1}.jpg", mode="wb") as f:
							async with session.get(items[i]['src'].replace('-300x300', '')) as grabImage:
								await f.write(await grabImage.read())
							

			ld_item1 = Image.open(f"{path_to}{path_to_shop}is1.jpg")
			ld_item2 = Image.open(f"{path_to}{path_to_shop}is2.jpg")
			ld_item3 = Image.open(f"{path_to}{path_to_shop}is3.jpg")

			r_i1 = ld_item1.resize((479,479))
			r_i2 = ld_item2.resize((479,479))
			r_i3 = ld_item3.resize((479,479))

			r_i1.save(f"{path_to}{path_to_shop}is1.jpg")
			r_i2.save(f"{path_to}{path_to_shop}is2.jpg")
			r_i3.save(f"{path_to}{path_to_shop}is3.jpg")

			itemshop_name = "FGItemShop"


			bg_array = ['backgrounds\\Splash_BlockParty.png', 'backgrounds\\Splash_ChompChomp.png', 'backgrounds\\Splash_DoorRush.png', 'backgrounds\\Splash_EggGrab.png', 'backgrounds\\Splash_FallBall.png', 'backgrounds\\Splash_FallMountain.png', 'backgrounds\\Splash_FloorIsLava.png', 'backgrounds\\Splash_FruitChute.png', 'backgrounds\\Splash_Gauntlet.png', 'backgrounds\\Splash_Hexagone.png', 'backgrounds\\Splash_Hoarders.png', 'backgrounds\\Splash_HoopsieDaisy.png', 'backgrounds\\Splash_Jinxed.png', 'backgrounds\\Splash_JumpClub.png', 'backgrounds\\Splash_JumpShowdown.png', 'backgrounds\\Splash_MatchFall.png', 'backgrounds\\Splash_RockandRoll.png', 'backgrounds\\Splash_RollOut.png', 'backgrounds\\Splash_Rotatonator.png', 'backgrounds\\Splash_RoyalRumble.png', 'backgrounds\\Splash_SeeSaw.png', 'backgrounds\\Splash_TailTag.png', 'backgrounds\\Splash_TeamTailTag.png', 'backgrounds\\Splash_TipToe.png', 'backgrounds\\Splash_Whirligig.png']
			bg_rng = random.randint(0,len(bg_array))
			print(len(bg_array))
			print(bg_rng)


			base_img = Image.open(f"{path_to}{path_to_shop}{bg_array[bg_rng]}")
			is_item1 = Image.open(f'{path_to}{path_to_shop}is1.jpg')
			is_item2 = Image.open(f'{path_to}{path_to_shop}is2.jpg')
			is_item3 = Image.open(f'{path_to}{path_to_shop}is3.jpg')
			itemshop = base_img.copy()

			itemshop.paste(is_item1, (116,300))
			itemshop.paste(is_item2, (721,300))
			itemshop.paste(is_item3, (1326,300))

			itemshop.save(f"{path_to}{path_to_shop}{itemshop_name}.png")

			base_img.close()
			is_item1.close()
			is_item2.close()
			is_item3.close()
			ld_item1.close()
			ld_item2.close()
			ld_item3.close()
			sp_image.close()
def setup(bot):
    bot.add_cog(refreshData(bot))
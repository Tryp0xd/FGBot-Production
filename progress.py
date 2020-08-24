import discord
import asyncio
from discord.ext import commands


class progress(commands.Cog):
	def __init__(self,bot):
		self.bot = bot



	@commands.command()
	async def progress(self, ctx):
		progressFile = discord.File("G:\\FGBot-Production-master\\assets\\progress\\SeasonProgress.jpg", filename="image.jpg")
		progressEmbed = discord.Embed(
			title = "Current Season Progress.",
			colour = 0x30d8de
			)

		progressEmbed.set_image(url = "attachment://image.jpg")

		await ctx.send(embed=progressEmbed, file=progressFile)
	

def setup(bot):
    bot.add_cog(progress(bot))
from saucenao_api import SauceNao
import os
from dotenv import load_dotenv
import discord 
from discord.ext import commands
import requests
import pandas as pd
from discord_ui import *
from asyncio import TimeoutError

key=os.getenv("sapi")
sauce = SauceNao(key)


class sauce_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name="image",help="image url test")
    async def imgt(self,ctx,*arg):
        global results
        try:
            try:
                results = sauce.from_url(ctx.message.attachments[0].url)
            except:
                results = sauce.from_url(arg)
        except:
            em = discord.Embed(title=f"{self.bot.get_emoji(958768110247223296)} Error!!!", description=f"No image or url provided", color=0xff4060)
            await ctx.send(embed=em)
        
        if results[0].similarity<80.0:
            em = discord.Embed(title=f"{self.bot.get_emoji(958768110247223296)} Error!!!", description=f"No similar images found", color=0xff4060)
            await ctx.send(embed=em)
        else:
            results=results[0]
            em=discord.Embed(title=results.title,url=results.urls[0],description=f"""
            author : {results.author}
            """)
            em.set_thumbnail(url=results.thumbnail)
            em.set_footer(text="saucenao reverse search",icon_url='https://i.imgur.com/8O0yxf7.png')
            await ctx.send(embed=em)
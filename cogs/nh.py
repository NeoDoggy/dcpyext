import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from hentai import *
from discord_ui import *
from asyncio import TimeoutError
import time


class nh_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name="nh",help="nhentai fetcher")
    async def nh(self,ctx,args=None,*nt): # <- nt = number or tag , [args=None] for no command inputs
        if args==None:
            await ctx.send(embed=discord.Embed(title=f"{self.bot.get_emoji(958768110247223296)} Error!!!", description=f"command needed", color=0xff4060) )
        else:
            if args=="random":
                book=Utils.get_random_hentai()
                nhembed=discord.Embed(title=book.title(),url=book.url)
                nhembed.set_image(url=book.cover)
                nhembed.set_footer(text="nhentai-"+str(book.id),icon_url='https://i.imgur.com/KRARu5m.png')
                await ctx.send(embed=nhembed)

            elif args=="find":
                try:
                    num=int(nt[0])
                    book=Hentai(num)
                    nhembed=discord.Embed(title=book.title(),url=book.url)
                    nhembed.set_image(url=book.cover)
                    nhembed.set_footer(text="nhentai-"+nt[0],icon_url='https://i.imgur.com/KRARu5m.png')
                    await ctx.send(embed=nhembed)
                except:
                    await ctx.send(embed=discord.Embed(title=f"{self.bot.get_emoji(958768110247223296)} Error!!!", description=f"no numbers provided", color=0xff4060) )

            elif args=="query":
                try:
                    kw=nt[0].replace(',',' ')
                    dj=Utils.search_by_query(kw, sort=Sort.PopularWeek)
                    dj=list(dj)
                    page=0
                    book=dj[page]
                    nhembed=discord.Embed(title=book.title(),url=book.url)
                    nhembed.set_image(url=book.cover)
                    nhembed.set_footer(text="nhentai-"+str(book.id),icon_url='https://i.imgur.com/KRARu5m.png')
                    msg = await ctx.send(embed=nhembed, components=[
                        Button("previous", color="blurple", custom_id="pre"),
                        Button("next", color="green", custom_id="nex")
                    ])
                    while True:
                        try:
                            btn = await msg.wait_for("button", self.bot, by=ctx.author, timeout=20)
                            bc = btn.data["custom_id"]
                            
                            if page<len(dj) and page>=0:
                                if bc=="nex" and page<len(dj)-1:
                                    page+=1
                                elif bc=="pre" and page>0:
                                    page-=1 

                            book=dj[page]
                            nhembed=discord.Embed(title=book.title(),url=book.url)
                            nhembed.set_image(url=book.cover)
                            nhembed.set_footer(text="nhentai-"+str(book.id),icon_url='https://i.imgur.com/KRARu5m.png')
                            await msg.edit(embed=nhembed)

                        except TimeoutError:
                            break

                except:
                    await ctx.send(embed=discord.Embed(title=f"{self.bot.get_emoji(958768110247223296)} Error!!!", description=f"no keywords provided", color=0xff4060) )

            elif args=="read":
                try:
                    page=0
                    num=int(nt[0])
                    book=Hentai(num)
                    nhembed=discord.Embed(title=book.title(),url=book.url)
                    nhembed.set_image(url=book.image_urls[page])
                    nhembed.set_footer(text="nhentai-"+nt[0]+f"-page {page+1}",icon_url='https://i.imgur.com/KRARu5m.png')                   
                    msg = await ctx.send(embed=nhembed, components=[
                        Button("previous", color="blurple", custom_id="pre"),
                        Button("next", color="green", custom_id="nex")
                    ])
                    while True:
                        try:
                            btn = await msg.wait_for("button", self.bot, by=ctx.author, timeout=20)
                            bc = btn.data["custom_id"]

                            if page<book.num_pages and page>=0:
                                if bc=="nex" and page<book.num_pages-1:
                                    page+=1
                                elif bc=="pre" and page>0:
                                    page-=1 
                                else:
                                    em = discord.Embed(title=f"{self.bot.get_emoji(958768110247223296)} Error!!!", description=f"start or end of the book", color=0xff4060) 
                                    emsg = await ctx.send(embed=em)
                                    await emsg.delete(delay=2)
                            
                            nhembed=discord.Embed(title=book.title(),url=book.url)
                            nhembed.set_image(url=book.image_urls[page])
                            nhembed.set_footer(text="nhentai-"+nt[0]+f"-page {page+1}",icon_url='https://i.imgur.com/KRARu5m.png')
                            await msg.edit(embed=nhembed)

                        except TimeoutError:
                            break

                except:
                    await ctx.send(embed=discord.Embed(title=f"{self.bot.get_emoji(958768110247223296)} Error!!!", description=f"no numbers provided", color=0xff4060))

            else:
                em = discord.Embed(title=f"Error!!!", description=f"Command not found.\nuse /help for commands", color=0xff4060) 
                await ctx.send(embed=em)
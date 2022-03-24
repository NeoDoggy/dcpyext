import os
import discord 
from discord.ext import commands
from dotenv import load_dotenv
from hentai import Hentai, Format
from hentai import Utils

class nh_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    #nhcrawler
    """
    @commands.command(name="nh",help="nhentai finder")
    async def nh(self,ctx,args):
        num=args
        await ctx.send('file fetching... plz wait',delete_after=1)
        os.system(f'./nhcrawl.sh -n {num} -l 1')
        tmpfile=discord.File(f'./temphtml/{num}/1.png',filename="image.png")
        nhembed=discord.Embed(title=f'cover of {num}',url=f'https://nhentai.net/g/{num}',description='wah',color=0xFFC0CB)
        nhembed.set_image(url='attachment://image.png')
        await ctx.send('Finished',delete_after=1)
        await ctx.channel.send(file=tmpfile,embed=nhembed)
        os.system(f'rm -rf ./temphtml/{num}')
    """
    @commands.command(name="nh",help="nhentai fetcher")
    async def nh(self,ctx,args=None,*nt): # <- nt = number or tag , [args=None] for no command inputs
        if args==None:
            await ctx.send("command needed")
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
                    await ctx.send("no numbers provide")

            else:
                em = discord.Embed(title=f"Error!!!", description=f"Command not found.\nuse /help for commands", color=0xff4060) 
                await ctx.send(embed=em)
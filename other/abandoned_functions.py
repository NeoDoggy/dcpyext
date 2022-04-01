from discord_components import *
import discord
from discord.ext import commands
from dotenv import load_dotenv

class help_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    #help
    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        hembed=discord.Embed(title="Help")

        hembed.add_field(name = 'Music', value= """
        /p {url} or /p music {name} - play YT songs
        /q - show queue
        /skip - skip, as shown
        /leave - also, as shown""", inline = False)

        hembed.add_field(name = 'Twitter', value= """
        /twtfind {tag}
        multiple tags usage:
        OR "#tag1 OR #tag2"
        AND : "#tag1 #tag2""", inline = False)

        hembed.add_field(name = 'nhentai', value= """
        /nh 
        > find {booknum} - find a doujinshi from nhentai
        > random - generate a random hentai from the library""", inline = False)

        await ctx.send(embed=hembed)
    
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
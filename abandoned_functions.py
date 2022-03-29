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
    
    
import discord
from discord.ext import commands
from discord_ui import *
from asyncio import TimeoutError
import random

colors = [  0xf94144, 
            0xf3722c, 
            0xf8961e, 
            0xf9844a, 
            0xf9c74f, 
            0x90be6d, 
            0x43aa8b, 
            0x4d908e, 
            0x577590, 
            0x277da1, 
         ]

class help_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot


    #help
    @commands.command(name="help",help="help")
    async def help(self,ctx):
        eh=discord.Embed(title="Help",description="choose a help label below",color=random.choice(colors))
        msg = await ctx.send(embed=eh,
        components=
        [SelectMenu(placeholder="command for help",
            options=[
                SelectOption(
                    label="Music",
                    value="music",
                    description="music commands",
                    emoji="🎵"
                ),
                SelectOption(
                    label="Twitter",
                    value="twitter",
                    description="twitter commands",
                    emoji="🕊"
                ),
                SelectOption(
                    label="nhentai",
                    value="nhentai",
                    description="nhentai commands",
                    emoji="👃🏻"
                ),
            ])]
        )

        eM=discord.Embed(title="Music",color=random.choice(colors)).add_field(name = 'commands:', value= """
                                /p {url} or /p music {name} - play YT songs
                                /q - show queue
                                /skip - skip, as shown
                                /leave - also, as shown""", inline = False)
        eT=discord.Embed(title="Twitter",color=random.choice(colors)).add_field(name = 'commands:', value= """
                                /twtfind {tag}
                                multiple tags usage:
                                OR "#tag1 OR #tag2"
                                AND : "#tag1 #tag2""", inline = False)
        eN=discord.Embed(title="nhentai",color=random.choice(colors)).add_field(name = 'commands:', value= """
                                /nh 
                                > find {booknum} - find a doujinshi from nhentai
                                > random - generate a random hentai from the library""", inline = False)

        try:
            sel = await msg.wait_for("select", self.bot, by=ctx.author, timeout=20)
            hc = sel.selected_options[0].value
            await msg.delete()

            if hc=="music":
                await ctx.reply(embed=eM,mention_author=False)
            elif hc=="twitter":
                await ctx.reply(embed=eT,mention_author=False)
            elif hc=="nhentai":
                await ctx.reply(embed=eN,mention_author=False)
            
        except TimeoutError:
            await msg.delete()

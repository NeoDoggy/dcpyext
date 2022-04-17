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
        eh=discord.Embed(title=":exclamation:| Help",description="choose a help label below",color=random.choice(colors))
        msg = await ctx.send(embed=eh,
        components=[
            SelectMenu(placeholder="command for help",
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
                        emoji=self.bot.get_emoji(958762701004349471)
                    ),
                    SelectOption(
                        label="nhentai",
                        value="nhentai",
                        description="nhentai commands",
                        emoji=self.bot.get_emoji(941019319846989875)
                    ),
                    SelectOption(
                        label="covid",
                        value="covid",
                        description="covid commands",
                        emoji=self.bot.get_emoji(958768110247223296)
                    ),
                    SelectOption(
                        label="image",
                        value="image",
                        description="image search commands",
                        emoji=self.bot.get_emoji(965152697420492800)
                    ),
                    SelectOption(
                        label="cancel",
                        value="cancel",
                        description="cancel command help center",
                        emoji="❌"
                    ),
                ]),
        ])

        eM=discord.Embed(title=":musical_note: | Music",color=random.choice(colors)).add_field(
                            name = 'commands:', value= """\n
                                /p {url} or /p music {name} - play YT songs

                                /q - show queue

                                /skip - skip, as shown

                                /leave - also, as shown
                                \n""", inline = False).set_footer(
                            text="help center > music commands",icon_url='https://i.imgur.com/jtBJhrQ.jpg')

        eT=discord.Embed(title="<:twticon:958762701004349471> | Twitter",color=random.choice(colors)).add_field(
                            name = 'commands:', value= """\n
                                /twtfind {tag}

                                multiple tags usage:
                                OR gate : "#tag1 OR #tag2"
                                AND gate : "#tag1 #tag2"
                                \n""", inline = False).set_footer(
                            text="help center > twitter commands",icon_url='https://i.imgur.com/jtBJhrQ.jpg')

        eN=discord.Embed(title="<:Icon_Latency:941019319846989875> | nhentai",color=random.choice(colors)).add_field(
                            name = 'commands:', value= """\n
                                /nh find {booknum} - find a doujinshi from nhentai

                                /nh random - generate a random hentai from the library

                                /nh query {tags,author,groups.etc} - find doujinshi with any keywords

                                /nh read {booknum} - read a doujinshi
                                \n""", inline = False).set_footer(
                            text="help center > nhentai commands",icon_url='https://i.imgur.com/jtBJhrQ.jpg')
        
        eC=discord.Embed(title=f"{self.bot.get_emoji(958768110247223296)} | covid",color=random.choice(colors)).add_field(
                            name = 'commands:', value= """\n
                                /covid - show today's infected population
                                \n""", inline = False).set_footer(
                            text="help center > covid commands",icon_url='https://i.imgur.com/jtBJhrQ.jpg')
        
        eIS=discord.Embed(title=f"{self.bot.get_emoji(965152697420492800)} | image",color=random.choice(colors)).add_field(
                            name = 'commands:', value= """\n
                                /image {url} - reverse image and anime scene search
                                p.s. this command also supports attachments
                                \n""", inline = False).set_footer(
                            text="help center > image commands",icon_url='https://i.imgur.com/jtBJhrQ.jpg')
        
        while True:
            try:
                sel = await msg.wait_for("select", self.bot, by=ctx.author, timeout=20)
                hc = sel.selected_options[0].value
                #await msg.delete()
                if hc=="music":
                    await ctx.reply(embed=eM,mention_author=False)
                elif hc=="twitter":
                    await ctx.reply(embed=eT,mention_author=False)
                elif hc=="nhentai":
                    await ctx.reply(embed=eN,mention_author=False)
                elif hc=="covid":
                    await ctx.reply(embed=eC,mention_author=False)
                elif hc=="image":
                    await ctx.reply(embed=eIS,mention_author=False)
                elif hc=="cancel":
                    await msg.delete()
                    await ctx.message.delete()
                
            except TimeoutError:
                await msg.delete()

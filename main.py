import os
from posix import uname_result
import discord 
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime as dt
from youtube_dl import YoutubeDL


class main_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.help_message="""
```
Main:
/test - see whether the bot's alive

Music:
/play \{url\} - play YT songs
/queue - show queue
/skip - skip, as shown
/disconnect - also, as shown

Twitter:
no commands yet
```
"""

        self.text_channel_list=[]
    
    
    #start up
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)
        print(f'{self.bot.user} is ready to work')
        activity = activity = discord.Game(name="幫ニオ做家事的遊戲")
        await self.bot.change_presence(status=discord.Status.online, activity=activity)
       
    #help
    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)


    #shout out
    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)
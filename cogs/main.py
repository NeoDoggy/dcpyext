import os
#from posix import uname_result
import discord 
from discord.ext import commands
from dotenv import load_dotenv
#from datetime import datetime as dt
import requests
import time
from discord.ext.commands import CommandNotFound


class main_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.text_channel_list=[]
    
    #command error
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error): 
        if isinstance(error, commands.CommandNotFound): 
            em = discord.Embed(title=f"{self.bot.get_emoji(958768110247223296)} Error!!!", description=f"Command not found.\nuse /help for commands", color=0xff4060) 
            await ctx.send(embed=em)
        else:
            print(error)


    #start up
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)
        print(f'{self.bot.user} is ready to work')
        activity = discord.Game(name="/help for commands")
        await self.bot.change_presence(status=discord.Status.online, activity=activity)
        #await self.bot.user.edit(username="nyadoggy")  #edit username
        #img = requests.get("https://i.imgur.com/jtBJhrQ.jpg").content 
        #await self.bot.user.edit(avatar=img)  #change avatar

    #test
    @commands.command(name="test",help="ping")
    async def test(self,ctx):
        msg = await ctx.send(self.bot.get_emoji(869447774876336139))
        await msg.delete(delay=3)

    @commands.command(name="michan",help="mafumafu")
    async def michan(self,ctx):
        await ctx.message.delete()
        await ctx.send(self.bot.get_emoji(967357799107530862))

    #test embed
    @commands.command(name="testembed",help="test embed")
    async def tsemb(self,ctx):
        tsembed=discord.Embed(
            title="test",
            description="dis test",
            url="https://google.com",
            color=0xFFC0CB,
            footer="ft test"
        )
        ts=await ctx.send(embed=tsembed)
        time.sleep(2)
        tsembed=discord.Embed(
            title="test",
            description="meow",
            url="https://google.com",
            color=0xFFC0CB,
            footer="ft test"
        )
        await ts.edit(embed=tsembed)

    

    #shout out
    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)
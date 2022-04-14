import discord
from discord.ext import commands
from discord_slash import cog_ext
from asyncio import TimeoutError

class slash_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @cog_ext.cog_slash(name="testS",description="meow",guild_ids=[677850065288691717])
    async def testS(self,ctx):
        await ctx.send("meow")
    
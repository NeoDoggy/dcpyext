from head import *


class main_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.help_message="""
```
Main:
/test - see whether the bot's alive

Music:
/p {url} or /p music {name} - play YT songs
/q - show queue
/skip - skip, as shown
/leave - also, as shown

Twitter:
no commands yet

nhentai:
/nh {booknum} - find a doujinshi from nhentai
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
        #await self.bot.user.edit(username="nyadoggy")
       
    #help
    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)
    #test
    @commands.command(name="test",help="test")
    async def test(self,ctx):
        await ctx.send('im alive')
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
        await ctx.send(embed=tsembed)

    #shout out
    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)
from head import *

from music import music_cog
from main import main_cog
from nh import nh_cog

load_dotenv()
token = os.getenv('bot_token')
prefix = os.getenv('prefix')

bot=commands.Bot(command_prefix=prefix)

bot.remove_command('help')

bot.add_cog(music_cog(bot))
bot.add_cog(main_cog(bot))
bot.add_cog(nh_cog(bot))


"""
@bot.event
async def on_ready():
    print(f'{bot.user} is ready to work')
    activity = activity = discord.Game(name="幫ニオ做家事的遊戲")
    await bot.change_presence(status=discord.Status.online, activity=activity)
"""


"""
@bot.command()
async def nh(ctx,args):
    num = args
    await ctx.send('file fetching... plz wait')
    os.system(f'./nhcrawl.sh -n {num} -l 1')
    tmpfile=discord.File(f'./temphtml/{num}/1.png',filename="image.png")
    nhembed=discord.Embed(title=f'cover of {num}',url=f'https://nhentai.net/g/{num}',description='wah',color=0xFFC0CB)
    nhembed.set_image(url='attachment://image.png')
    await ctx.send('Finished',delete_after=5)
    await ctx.channel.send(file=tmpfile,embed=nhembed)
    os.system(f'rm -rf ./temphtml/{num}')
"""

bot.run(token)
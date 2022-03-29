import os
#from posix import uname_result
import discord 
from discord.ext import commands
from dotenv import load_dotenv
from discord_ui import *
#from datetime import datetime as dt

from cogs import music 
from cogs import main
from cogs import nh
from cogs import twt
from cogs import help

load_dotenv()
token = os.getenv('bot_token')
prefix = os.getenv('prefix')

bot=commands.Bot(command_prefix=prefix)
ui = UI(bot)

bot.remove_command('help')

bot.add_cog(music.music_cog(bot))
bot.add_cog(main.main_cog(bot))
bot.add_cog(nh.nh_cog(bot))
bot.add_cog(twt.twt_cog(bot))
bot.add_cog(help.help_cog(bot))

bot.run(token)
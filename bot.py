from head import *

from music import music_cog
from main import main_cog
from nh import nh_cog
from twt import twt_cog

load_dotenv()
token = os.getenv('bot_token')
prefix = os.getenv('prefix')

bot=commands.Bot(command_prefix=prefix)

bot.remove_command('help')

bot.add_cog(music_cog(bot))
bot.add_cog(main_cog(bot))
bot.add_cog(nh_cog(bot))
bot.add_cog(twt_cog(bot))

bot.run(token)
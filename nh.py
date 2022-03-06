from head import *

class nh_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    #nhcrawler
    @commands.command(name="nh",help="nhentai finder")
    async def nh(self,ctx,args):
        num=args
        await ctx.send('file fetching... plz wait',delete_after=1)
        os.system(f'./nhcrawl.sh -n {num} -l 1')
        tmpfile=discord.File(f'./temphtml/{num}/1.png',filename="image.png")
        nhembed=discord.Embed(title=f'cover of {num}',url=f'https://nhentai.net/g/{num}',description='wah',color=0xFFC0CB)
        nhembed.set_image(url='attachment://image.png')
        await ctx.send('Finished',delete_after=1)
        await ctx.channel.send(file=tmpfile,embed=nhembed)
        os.system(f'rm -rf ./temphtml/{num}')
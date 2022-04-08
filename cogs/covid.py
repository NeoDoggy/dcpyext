import os
import discord 
from discord.ext import commands
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

def get_ctx():
    url = 'https://www.cdc.gov.tw/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text,'html.parser')
    Elem = soup.find_all('div', class_="content-boxes-v3")
    ElemN = [e.text for e in Elem]
    today = str(date.today().year)+' - '+str(date.today().month)+str(date.today().day)
    yesterday = str((date.today()-timedelta(days=1)).year)+' - '+str((date.today()-timedelta(days=1)).month)+str((date.today()-timedelta(days=1)).day)
    has=False
    covid_ctx=""
    retctx=[]
    for i in ElemN:
        tdc = i.replace("\n",'')
        if tdc.startswith(today):
            if '新增' in tdc:
                covid_ctx=tdc.strip(today)
                retctx.append(covid_ctx)
                has=True
                retctx.append(has) 
    if has==False:
        for i in ElemN:
            tdc = i.replace("\n",'')
            if tdc.startswith(yesterday):
                if '新增' in tdc:
                    covid_ctx=tdc.strip(yesterday)
                    retctx.append(covid_ctx)
                    retctx.append(has)
    return retctx

class covid_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name="covid",help="todays covid")
    async def covid(self,ctx):
        cov_ctx=get_ctx()
        today = date.today()
        yesterday = date.today()-timedelta(days=1)
        if cov_ctx[1]==True:
            em = discord.Embed(title=f"{self.bot.get_emoji(958768110247223296)} {today} 確診報告", description=cov_ctx[0], color=0xff4060) 
        else:
            em = discord.Embed(title=f"{self.bot.get_emoji(958768110247223296)} {yesterday} 確診報告", description=cov_ctx[0], color=0xff4060) 
        await ctx.send(embed=em)
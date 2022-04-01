import os
#from posix import uname_result
from dotenv import load_dotenv
import discord 
from discord.ext import commands
import tweepy
import requests
import pandas as pd
from discord_ui import *
from asyncio import TimeoutError

load_dotenv()

ck=os.getenv('api_key')
cks=os.getenv('api_key_secret')
at=os.getenv('ac_token')
ats=os.getenv('ac_token_secret')
brr=os.getenv('bearer_token')

pd.set_option('display.max_columns', None)

client = tweepy.Client( bearer_token=brr, 
                        consumer_key=ck, 
                        consumer_secret=cks, 
                        access_token=at, 
                        access_token_secret=ats, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True
                        )

def find(q=""):
    # Define query
    query = q
    tweets = client.search_recent_tweets(query=query, 
                                        tweet_fields=['referenced_tweets'],
                                        max_results=10
                                        )
    tweets_dict = tweets.json()
    tweets_data = tweets_dict['data'] 
    twt = pd.json_normalize(tweets_data)
    return twt

def id_to_username(id=""):
    u = client.get_user(id=id)
    u = u.json()
    u = u['data']['username']
    return u

class twt_cog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name="twtfind",help="find images on twitter")
    async def tf(self,ctx,args):
        tags="("+args+")"
        name=find(tags+' has:images')
        #await ctx.send(name['entities.urls'][0][0]['expanded_url'])
        author=name['text'][0].split('@')[1].split(':')[0]
        await ctx.send((f"https://twitter.com/{author}/status/{name['referenced_tweets'][0][0]['id']}"))
        #await ctx.send(f"https://twitter.com/{id_to_username(name['author_id'][0])}/status/{name['id'][0]}")

    @commands.command(name="twt",help="twtpage")
    async def twf(self,ctx,args):
        page=0
        tags="("+args+")"
        name=find(tags+' has:images')
        author=name['text'][page].split('@')[1].split(':')[0]
        msg = await ctx.send((f"https://twitter.com/{author}/status/{name['referenced_tweets'][page][0]['id']}"), components=[
            Button("previous", color="blurple", custom_id="pre"),
            Button("next", color="green", custom_id="nex")
        ])
        while True:
            try:
                btn = await msg.wait_for("button", self.bot, by=ctx.author, timeout=20)
                bc = btn.data["custom_id"]
                
                if page+1<10 and page>=0:
                    if bc=="nex":
                        page+=1
                    elif bc=="pre" and page>0:
                        page-=1 
                author=name['text'][page].split('@')[1].split(':')[0]
                await msg.edit((f"https://twitter.com/{author}/status/{name['referenced_tweets'][page][0]['id']}"))

            except TimeoutError:
                break        
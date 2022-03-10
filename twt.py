import os
#from posix import uname_result
from dotenv import load_dotenv
import discord 
from discord.ext import commands
import tweepy
import requests
import pandas as pd


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
        
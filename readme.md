Discord bot
===
## Description
A bot made with [discord.py](https://discordpy.readthedocs.io) and some homemade apis.  


## Services
**nyadoggy** is a music bot made with python and some other languages such like shell codes or else. This bot provides services such like **music** in voice channels or ones like **image and anime search**, **twitter search**, and **covid infected number search** etc. The NSFW one includes randoming a hentai from **nhentai**, what's more, you can read one in Discord with nyadoggy by pressing buttons,no need to get on ur browser!  

## How it's programmed

### Used moduels:
```python
#requirements.txt
discord.py==1.7.2
    ├──discord-components==2.1.2
    └──discord-ui==5.1.6
youtube-dl==2021.12.17
requests==2.26.0
    ├──requests-oauthlib==1.3.0
    ├──requests-toolbelt==0.9.1
    └──requests-unixsocket==0.2.0
pandas==1.2.3
python-dotenv==0.17.1
saucenao-api==2.4.0
    ├──PixivPy==3.5.11
    └──tweepy==4.6.0
beautifulsoup==4.11.1 
```

### Structure tree
```python
#structure tree
.
├── bot.py
├── cogs
│   ├── __init__.py
│   ├── __pycache__
│   ├── covid.py
│   ├── help.py
│   ├── main.py
│   ├── music.py
│   ├── nh.py
│   ├── sauce.py
│   └── twt.py
├── image
├── removed_functions
│   ├── abandoned_functions.py
│   ├── nhcrawl.sh
│   └── slashC.py
└── requirements.txt
```

### Solving messy codes
In order to solve messy codes gathering in the main bot file and making it unreadable, I use cogs to solve it.  
What's an cog? A cog is like a costumize moduel. So whenever we need or not of this funtion or command, we just import it or unimport.  
The example usage is below:  
```python=
#import from customize package
from cogs import music 
from cogs import main
from cogs import nh
from cogs import twt
from cogs import help
from cogs import covid
from cogs import sauce

# import it into main command
bot.add_cog(music.music_cog(bot))
bot.add_cog(main.main_cog(bot))
bot.add_cog(nh.nh_cog(bot))
bot.add_cog(twt.twt_cog(bot))
bot.add_cog(help.help_cog(bot))
bot.add_cog(covid.covid_cog(bot))
bot.add_cog(sauce.sauce_cog(bot))
```

## Commands & Files

The commands below uses async funtions in order for mutitasking and not disturbing to the original flow.  

### ⌨️ `bot.py`
This is the file for importing cogs and running the bot.  

---

### ⚙️ `cogs->main.py`
This is the cog for fool-proof mechanism and other bot maintenance funtions.  
*example of fool-proof:*  
<img src="https://i.imgur.com/AKMvnaE.png" width=300></img>


---

### ⚙️ `cogs->help.py`
A cog for help commands, the interface is shown in the below image:  

 **Command usage:**  
<img src="https://i.imgur.com/enEMLZF.png" width=300></img>

 **Select menu:**  
<img src="https://i.imgur.com/wHWFgCR.png" width=300></img>

---

### ⚙️ `cogs->music.py`
A cog for playing music in voice channels.  
#### 🔧 commands
`/p {arg}`
Plays a song within a youtube link.  

`/p music {arg}`
Plays a song within a song name.  

`/q`
Shows the queue of the playlist.  

`/skip`
Skip now song.  

`/leave`
Leave the voice channel.  

---

### ⚙️ `cogs->nh.py`
A cog for nhentai related commands.  
#### 🔧 commands
`/nh random`  
Sends a random doujinshi.  

`/nh find {arg}`  
Sends a specific doujinshi.  

`/nh read {arg}`  
Sends a specific doujinshi with buttons to flip pages.  
*example:*  
<img src="https://i.imgur.com/jHvbc0F.png" width=300></img>

`/nh query {arg}`  
Finds doujinshi with the arguments provided.  
*The argument can be a tag or an author name.*  

---

### ⚙️ `cogs->covid.py`
A cog for covid-19 related commands.  
#### 🔧 commands
`/covid`  
Sends todays infected populations.  
*example:*  
<img src="https://i.imgur.com/5RCPXuL.png" width=300></img>

---

### ⚙️ `cogs->sauce.py`
A cog for image reverse finding related commands.  
#### 🔧 commands
`/image {url} or /image {attachment}`  
Finds a anime scene or image on the internet.  
*example:*  
<img src="https://i.imgur.com/PA2kd8U.png" width=300></img>

---

### ⚙️ `cogs->twt.py`
A cog for twitter related commands.  
#### 🔧 commands
`/twtfind {arg}`  
Finds the most popular tweet by the argument/tags provided.  
*example:*  
<img src="https://i.imgur.com/J3Z4fvB.png" width=300></img>

## Commands or functions for future

### Slash commands
Due to discord 2.0 unknown issues, slash commands will confict with some original funtions. So in order to solve it, I removed all the slash commands.Hope it's appropriate to add slash commands to bots in the future.  

### mongoDB
Docker up the bot for all users to run wherever they want.  

## Python learning experience
Python is fun and easy to learn, although it's a cult programming language.  

## github repo
https://github.com/NeoDoggy/dcpyext




###### `made with ❤ by neodoggy 2022`
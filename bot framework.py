import discord
from discord.ext import commands
from random import choice, randint


class Command():
    def __init__(self, bot):
        self.bot = bot
        self.shouldI = ["I agree.", "That's false.","Reconsider it.", "Maybe.",
                        "It's your life, not mine.", "You should get a life.",
                        "Ask me something more important.", "Yes, have fun!",
                        "I'm not sure if you should.", "Don't ask me."]
        bot = discord.Client()
        
bot = 

@polari.event
async def onReady():
    print("Client logged in")
    print(polari.user.name + " " + polari.user.id)
    polari.say("Hello, I'm Polari, Rosalina's best advisor.")
    polari.say("My username is " + polari.user.id)

@polari.command()
async def hello(*args):
    await polari.say("Hello, world!")
    
@polari.command()
async def userInfo(discord.Member member):
    await polari.say("{0.name} 


    
my_bot.run("MzIxODQ4ODUwMzA4NjYxMjQ4.DBkLRA.hqt-ki6T_X8sm6MKy5gQMMC2h3g")
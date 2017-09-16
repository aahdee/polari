import discord
from discord.ext import commands
from random import choice, randint

polari = Bot(command_prefix="~")

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
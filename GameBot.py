#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Thomas
#
# Created:     26/03/2019
# Copyright:   (c) Thomas 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import discord
import random
import urllib.request
import os
from os import walk
from discord.utils import get
dir_path = os.path.dirname(os.path.realpath(__file__))

#Variables that contains the user credentials to access Twitter API
f = open("C:/Users/computing/Desktop/DoggoBot/TOKEN.txt", "r")
TOKEN = f.read();

client = discord.Client()

@client.event
async def on_message(message):
    rand = random.randint(0,200)
    TrueMsg = message
    message = message.content.lower()
    msg = ""
    author = message.author
    channel = message.channel
    #Add Emoji Reaction to any message containing 'bork'
    #if "bork" in text:
        #await message.add_reaction("\U0001F415")

    #if message author is this bot
    if author == client.user:
        #Add emoji reaction to any message sent by the bot
        #await message.add_reaction("\U0001F436")
        #stop the bot replying to itself
        return

    #if author is any bot
    if author.bot == True:
        #stop bot from responding
        return

    if message.startswith('&play '):
        m = message[6:]
        print m
        if m.strip() = 'guesser':
            for emoji in client.emoji():
                await message.channel.send(emoji)


    if (text.startswith('&help')
        msg = "$play - play a game \nAvailable Games: \n  - Gusser - 60secs to guess the emoji \n - Werewolves - A discord version of the card game werewolves\
        \n$help - Show this help menu\
        \n\n***If you have an issue with the bot please contact tinyman1199#6969***"

        await message.channel.send(msg)

    #if "test" in text:
    #    embed = discord.Embed();
    #    embed.set_thumbnail(url='https://images.dog.ceo/breeds/chow/n02112137_5089.jpg')
    #    await message.channel.send(embed=embed)





@client.event
#log basic info when the bot starts running
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

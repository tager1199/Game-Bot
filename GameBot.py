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
import asyncio
import tracemalloc
from discord.ext import tasks
from os import walk
from discord.utils import get
dir_path = os.path.dirname(os.path.realpath(__file__))

#Variables that contains the user credentials to access Twitter API
f = open("TOKEN.txt", "r")
TOKEN = f.read();
playGuesser = False
global emoji
client = discord.Client()
tracemalloc.start()
file = open("C:\\Users\\computing\\Desktop\\GameBot\\Game-Bot\\uniqueEmojis.txt",'r')
emojiList = file.readlines()
global gameChannel
@client.event
async def on_message(message):
    rand = random.randint(0,200)
    emojiList.append(client.emojis)
    global playGuesser
    global emoji
    global gameChannel
    msg = ""
    author = message.author
    channel = message.channel
    TrueMsg = message
    message = message.content.lower()
    #if message author is this bot
    if author == client.user:
        #stop the bot replying to itself
        return

    #if author is any bot
    if author.bot == True:
        #stop bot from responding
        return

    if message.startswith('&play '):
        m = message[6:]
        await channel.send("\ud83d\ude00")
        if m.strip() == 'guesser':
            if playGuesser == False:
                playGuesser = True
                gameChannel = channel
                await channel.send('Starting a game of Guesser\
                \nOnce the game starts you\'ll have 60seconds to guess the randomly selected emoji\
                \nOnly guesses with a single emoji will be counted please dont send multiple in the same message')
                await gameChannel.send('Game of guesser starting....')
                emoji = random.choice(emojiList)
                await asyncio.sleep(1)
                await gameChannel.send('NOW!!!!')
                await asyncio.sleep(30)
                if playGuesser == True:
                    await gameChannel.send('30 Seconds Left! :timer:')
                    await asyncio.sleep(20)
                    if playGuesser == True:
                        await gameChannel.send('10 Seconds Left! :timer:')
                        await asyncio.sleep(10)
                        if playGuesser == True:
                            await gameChannel.send('Unfortunatley no one guessed the emoji correctly. \nThe emoji was: ')
                            await gameChannel.send(emoji)
                            playGuesser = False
            else:
                await channel.send('A Game of guesser is already ongoing')


    if playGuesser == True:
        if message == str(emoji):
            await gameChannel.send(('Congratualtions {0.author.mention}. You guessed correctly. \n The emoji was: ').format(TrueMsg))
            await gameChannel.send(emoji)
            playGuesser = False


    if (message.startswith('&help')):
        msg = '''$play - play a game \nAvailable Games:\n  - Guesser - 60secs to guess the emoji
        - Werewolves - A discord version of the card game werewolves
        $help - Show this help menu
        \n\n***If you have an issue with the bot please contact tinyman1199#6969***'''

        await channel.send(msg)

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

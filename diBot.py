import discord
import asyncio
import pickle
import logging
import time
import random
import json
import UserCommands
#import Forest_hut


class area():
    def __init__(self):
        self.areaName = '???'
        self.playersInArea = []
        self.areaDescription = ''' \n
An abyss of nothingness surrounds you, pure nothingness.

And yet...

You can\'t seem to shake the feeling that you are not alone...'''
        self.ThingsInArea = []


with open("Item.json", "r") as read_file:
    itemIndex = json.load(read_file)

class player():
    def __init__(self):
        self.Location = area()
        self.Username = ''
        self.secret = False
        self.greet_function = greeter

client = discord.Client()
PlayerList = {}


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(PlayerList)
    print(itemIndex)
    print("update {}")

@client.event
async def on_message(message):
    
    global PlayerList
    confused = True


    if message.content.startswith('d!test'):
        print("about to do a thing")
        await UserCommands.Help(message)
        print("prossesing message {}".format(message.content))

                
    if message.content.startswith("d!"):
        print("prossesing message {}".format(message.content))
        if message.content.startswith("d!new account"):
            if message.author.id in PlayerList:
                await client.send_message(message.channel, 'you\'re already in our data base')
            else:
                await Help(message)
        elif message.author.id in PlayerList:
            for i in coms.commands.keys():
            
                if ( message.content.startswith(i) ):
            
                    await coms.commands[i](message)
                    confused = False
                    break

            if (confused == True):
                await client.send_message(message.channel, 'I didn\t understand for a list of commands use !help')
        else:
            await client.send_message(message.channel, 'looks like your not in our data base please use !new account and create an account to use this bot')



async def greeter(message):
    if message.content.lower().startswith('!checkin'):
        print(message.author.id)
        print(PlayerList.keys())
        await client.send_message(message.channel, 'Hello %s, Welcome back.' % PlayerList[message.author.id].Username)
        
        await client.send_message(message.channel, 'You are in the {}. Would you like to look around?'.format(PlayerList[message.author.id].Location.areaName))

        def check(msg):
            return msg.content.startswith('$look around')
            
        message = await client.wait_for_message(author=message.author, check=check)
        await client.send_message(message.channel, PlayerList[message.author.id].Location.areaDescription)

    elif message.content.startswith('$walk through forest'):
        await client.send_message(message.channel, 'You walk through the forest, passing by the various life in the forest.')

        def check(msg):
            return msg.content.startswith('$walk through the dark side')

        message = await client.wait_for_message(author = message.author, check = check)
        PlayerList[message.author.id].secret = True
        Forest_hut.player_enter(message)
        PlayerList[message.author.id].greet_function = Forest_hut.greeter()



client.run('Mjg4OTY2NjI1MjAwMTc3MTUy.DjZkJA.aRmsmA2Yq7AjH5e5VIoqMiG_ftQ')


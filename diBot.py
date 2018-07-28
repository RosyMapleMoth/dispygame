import discord
import asyncio
import pickle
import logging
import time
import random

import Forest_hut

    


class area():
    def __init__(self):
        self.areaName = '???'
        self.playersInArea = []
        self.areaDescription = ''' \n
An abyss of nothingness surrounds you, pure nothingness.

And yet...

You can\'t seem to shake the feeling that you are not alone...'''

        

class player():
    def __init__(self):
        self.Location = area()
        self.Username = ''
        self.secret = False
        self.greet_function = greeter

client = discord.Client()
PlayerList = {}

forest = area()
forest.areaName ='The great forest'
forest.areaDescription = ''' it\'s the woods, spooky '''
void = area()

Areas = [forest, void]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(PlayerList)
    

@client.event
async def on_message(message):
    global PlayerList

    if (message.author.id in PlayerList):
        await PlayerList[message.author.id].greet_function(message)
    
    elif message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.lower().startswith('!checkin'):
        await client.send_message(message.channel,'''
Hello %s, Welcome to Discordia!
This is an interactive text based MMO which is currently under production.''' % message.author.name )
        await client.send_message(message.channel, 'If you would like to create a profile please type \"!d create profile\" ')

    elif message.content.startswith('!d create profile'):
        await client.send_message(message.channel, 'Thank you for joining this project')
        await client.send_message(message.channel, 'To pick a name for your in-game player type $name nameHere')
        PlayerList[message.author.id] = player()
        PlayerList[message.author.id].Location = Areas[0]
        Areas[0].playersInArea.append(PlayerList[message.author.id])

        def check(msg):
            return msg.content.startswith('$name')
        
        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('$name'):].strip()

        PlayerList[message.author.id].Username = name
        await client.send_message(message.channel, '{} is a good name!'.format(name))

    elif message.content.startswith('!savegame'):
        afile = open('PlayerData', 'wb')
        pickle.dump(PlayerList, afile)
        afile.close()
        
    elif message.content.startswith('!loadgame'):
        file2 = open('PlayerData', 'rb')
        PlayerList = pickle.load(file2)
        file2.close()

    

async def greeter(message):
    if message.content.lower().startswith('!checkin'):
        print(message.author.id)
        print(PlayerList.keys())
        await client.send_message(message.channel, 'Hello %s, Welcome back.' % PlayerList[message.author.id].Username)
        
        await client.send_message(message.channel, 'You are in the {}. Would you like to look around?'.format(PlayerList[message.author.id].Location.areaName))

        def check(msg):
            return msg.content.startswith('$look around')
            
        message = await client.wait_for_message(author=message.author, check=check)
        #if ()
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


    


    
    
    

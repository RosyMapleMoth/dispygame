import discord
import asyncio
import pickle
import logging
import time

    


class area():
    def __init__(self):
        self.areaName = '???'
        self.playersInArea = None
        self.areaDescription = ''' \n
an abyss of nothingness surrounds you, pure nothingness.

And yet...

You can\'t seem to shake the feeling that you are not alone'''
        

class player():
    def __init__(self):
        self.Location = area()
        self.Username = ''

client = discord.Client()
PlayerList = {}

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

    
    if message.content.startswith('!test'):
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
        if (message.author.id in PlayerList):
            print(message.author.id)
            print(PlayerList.keys())
            await client.send_message(message.channel, 'Hello %s Welcome back' % PlayerList[message.author.id].Username)
            await client.send_message(message.channel, 'you are in the {} would you like to look around'.format(PlayerList[message.author.id].Location.areaName))

            def check(msg):
                return msg.content.startswith('$look around')
            message = await client.wait_for_message(author=message.author, check=check)
            await client.send_message(message.channel, PlayerList[message.author.id].Location.areaDescription)
            
        else:
            await client.send_message(message.channel,
                                      'Hello %s Welcome to Discordia this is an interactive text based MMO \n which is currently under production'
                                      % message.author.name )
            await client.send_message(message.channel, 'If you would liek to create a profile please type \"!d create profile\" ')

    elif message.content.startswith('!d create profile'):
        await client.send_message(message.channel, 'thank you for joining this projec')
        await client.send_message(message.channel, 'To pick a name for your in game player type $name nameHere')
        PlayerList[message.author.id] = player()
        PlayerList[message.author.id].Location = area()

        def check(msg):
            return msg.content.startswith('$name')
        
        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('$name'):].strip()

        PlayerList[message.author.id].Username = name
        await client.send_message(message.channel, '{} is a good name'.format(name))

    elif message.content.startswith('!savegame'):
        afile = open('PlayerData', 'wb')
        pickle.dump(PlayerList, afile)
        afile.close()
        
    elif message.content.startswith('!loadgame'):
        file2 = open('PlayerData', 'rb')
        PlayerList = pickle.load(file2)
        file2.close()
        
        
client.run('Mjg4OTY2NjI1MjAwMTc3MTUy.DjZkJA.aRmsmA2Yq7AjH5e5VIoqMiG_ftQ')


    


    
    
    

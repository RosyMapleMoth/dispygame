import discord
import asyncio
import pickle
import logging
import time
import random

import diBot

class player():
    def __init__(self):
        self.Limbs = ['Left Arm', 'Right Arm', 'Left Leg', 'Right Leg', 'Head']
        self.Username = ''

    
PlayerList = {}

reply = client.send_message
    

def player_enter(message):
    PlayerList[message.author.id] = player()
    PlayerList[message.author.id].Username = name
    greetings(message)


async def greeter(message):
    if (message.content.startswith('!') | message.content.startswith('$')) & message.channel != message.author.PrivateChannel:
        reply_msg = await reply(message.channel, 'Error - Invalid Message')
        await asyncio.sleep(3)
        client.delete_message(message)
        client.delete_message(reply_msg)

    elif message.content.startswith('!checkin'):
        reply(message.channel, 'You are in a strange hut in the middle of the woods.')

              
    
    

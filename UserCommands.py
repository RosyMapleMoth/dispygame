import discord
import asyncio
import pickle
#import diBot
# this file currently holds all user commands




async def CreateAccount(message):
        
    
    await diBot.client.send_message(message.channel, 'Thank you for joining this project, as a warnning this a work in progress')
    await diBot.client.send_message(message.channel, 'To pick your IGN(in game name) type $name your name')

    def check(msg):
        return msg.content.startswith('$name')
        
    message = await diBot.client.wait_for_message(author=message.author, check=check)
    name = message.content[len('$name'):].strip()

    diBot.PlayerList[message.author.id].Username = name
    await diBot.client.send_message(message.channel, '{} is a good name!'.format(name))

# Send in the user message and a status for the fuunction called
@asyncio.coroutine
async def GameError(message, status):
    if (status == "UnderConstruction"):
        await diBot.client.send_message(message.channel, "whooops this is a place holder the feature you attempted to use is underconstruction")
    elif(status == "XXX"):
        await diBot.client.send_message(message.channel, "whooops looks like the feature you attempted to use is broken at the momment i'm sure our devs are wokring on the issue")
    elif(status =="Inaccesable"):
        await diBotclient.send_message(message.channel, "whooops looks like the feature you attempted to use isn't supposed to be accsuable yet, our bad. please type !admin or contact an admin directly with infermation regardding this issue")
    elif(status == "TODO"):
        await diBotclient.send_message(message.channel, "whooops looks like the feature you attempted to use isn't in the game yet check back later or watch the change log for updates")
    else:
       await diBot.client.send_message(message.channel, "wow how did you get here?, we would like to know! please use !admin or contact us directly becuase we would like to know!")        


@asyncio.coroutine
async def Help(message):
    print("inside helper")
    await GameError(message, "UnderConstruction")

async def LoadAndSave(todo):
    if (todo == "save"):
        afile = open('PlayerData', 'wb')
        json.dump(PlayerList, afile)
        afile.close()
    elif(todo == "load"):
        file2 = open('PlayerData', 'rb')
        PlayerList = json.load(file2)
        file2.close()
    else:
        print("unacceptable state input")


import diBot 

        



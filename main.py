import discord
import os
#import my defs
import fun
#keep alive
from keep_alive import keep_alive

client = discord.Client()



spamL = [
    "පීස් මැසේජ් ස්පෑම් කරන්න එපා යාලු ", "එපා පරයෝ ස්පෑම් කරන්න ",
    "ඔයා ස්පෑම් කරපු මැසේජ් අයින් වෙයි "
]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name='For Bugs to fix'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #hi
    if (message.content == "HI" or message.content == "Hi"
            or message.content == "hi"):
        out = fun.hi() + fun.coolImoji()
        await message.channel.send(out + message.author.mention)

    #bye
    if (message.content == "bye" or message.content == "BYE"
            or message.content == "Bye"):
        out = fun.bye() + fun.coolImoji()
        await message.channel.send(out + message.author.mention)
    #love
    if (message.content == "wadan" or message.content == "Wadan"
            or message.content == "WADAN"):
        out = fun.love() + fun.loveImoji()
        await message.channel.send(out)
    #command
    if message.content.startswith('!'):
        if message.content.startswith('!clear'):
            #logs
            print("mee6 clean by ")
        else:
            await message.delete()
            out = fun.cmd() + fun.angryImoji()
            await message.channel.send(out, delete_after=5)
    #invite
    if (message.content == "invite" or message.content == "INVITE"
            or message.content == "Invite"):
        await message.channel.send(
            "hey " + message.author.mention +
            " here is the invite link https://discord.gg/VhZPurRWf8 ")
    #awake
    if (message.content == "negitapn" or message.content == "negatapan pago"
            or message.content == "tho nidida pago"):
        await message.channel.send("ado " + message.author.mention +
                                   " mn nidi ne bomka")


client.run('')

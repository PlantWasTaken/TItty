from ast import arg
import discord
from discord.ext import commands
import time as t
import random as rd
import os

token = "MTAyMDQxODA4Nzg2ODE4NjcyOA.GCAxCq.-aQZCrgAE5mm4THgDB0ggnyfesAIyPr3tN1k10"
client = discord.Client(intents = discord.Intents.all())
channel = 1020778135869997176
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

def wrt_file(lnk, name):
    f = open(name, "a")
    for i in lnk:
        if(i[0] != "h"):
            f.write(i[1:] + "\n")
        else:
            f.write(i + "\n")
    f.close()

def rnd_img(name):
    return rd.choice(open(name).readlines())

@bot.event
async def on_ready():
    print("Ready")


@bot.command(name = "bb")
async def on_message(ctx, args):
    if(args.lower() == "b"):
        await ctx.channel.send(rnd_img("boob.txt"))

    elif(args.lower() == "a"):
        await ctx.channel.send(rnd_img("ass.txt"))

    elif(args.lower() == "p"):    
        await ctx.channel.send(rnd_img("puss.txt"))

    elif(args.lower() == "rnd"):
        await ctx.channel.send(rnd_img("rnd.txt"))

@bot.command(name = "link")
async def on_message(ctx, *args):
    lnk = list(args)
    if(lnk[0][0] == "b"):
        wrt_file(lnk, "boob.txt")

    elif(lnk[0][0] == "a"):
        wrt_file(lnk, "ass.txt")

    elif(lnk[0][0] == "p"):
        wrt_file(lnk, "puss.txt")
            
    #rnd collection of all images        
    wrt_file(lnk, "rnd.txt")

bot.run(token)
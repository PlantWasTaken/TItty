import discord
from discord.ext import commands
import time as t
import random as rd

token = "MTAyMDQxODA4Nzg2ODE4NjcyOA.Gqt2mH.Ud8_rVv1T9KRb8eIutG0AFVFM1rgd4SVawnwoc"
client = discord.Client(intents = discord.Intents.all())
channel = 1020778135869997176
bot = commands.Bot(command_prefix="$", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Ready")


@bot.command(name = "bb")
async def on_message(ctx, *args):
    random_line = rd.choice(open("boob.txt").readlines())
    await ctx.channel.send(random_line)

@bot.command(name = "link")
async def on_message(ctx, *args):
    f = open("boob.txt", "a")
    f.write("".join(args) + "\n")
    f.close()

bot.run(token)
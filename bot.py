# PSBot by Fowth

import discord
from discord.ext import commands
import asyncio

bot = commands.Bot('?')

@bot.event
async def on_ready():
    print ("Bot is nu online!")
    print ("Hij is nu klaar voor gebruik")
    print ("Let op! Het is  nog niet allemaal 100% klaar.")

@bot.command(pass_context=True)
async def regels(ctx):
    await bot.say("Deze command word binnenkort uitgewerkt. Probeer het voor nu met MEE6")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Lees de regels beter door!".format(user.name))
    await bot.kick(user)

bot.run("NDc2MjczMDgyMzM2ODA0ODc1.DkrL8Q.798QwTCNUFNQeq9JtQXAkGzUqiE")

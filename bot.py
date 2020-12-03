import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import random
import json
import os

bot = commands.Bot(command_prefix='admin.')
client = discord.Client()

@bot.event
async def on_ready():
    print("준비 완료!")
    print(bot.user.name)
    print(bot.user.id)
    print("------------------------")

@bot.command(name="msg")
async def Echo(ctx, *, text: str):
    await ctx.send(text)

bot.run(os.environ['token'])

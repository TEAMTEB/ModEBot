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
    print("준비 완료!")
    game = discord.Game("admin.help | MEB 1.3 | 팀 텝 공식 포럼 관리용 봇!")
    await bot.change_presence(status=discord.Status.online, activity=game)

@commands.has_permissions(administrator=True)
@bot.command(name="msg", help="당신이 한 말을 따라합니다.", usage="admin.msg [말]")
async def Echo(ctx, *, text: str):
    await ctx.send(text)

bot.run(os.environ['token'])

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
    game = discord.Game("admin.help | MEB 1.4 | 팀 텝 공식 포럼 전용 봇! | 프로필 업데이트!")
    await bot.change_presence(status=discord.Status.online, activity=game)

@commands.has_permissions(administrator=True)
@bot.command(name="msg", help="당신이 한 말을 따라합니다.", usage="admin.msg [말]")
async def Echo(ctx, *, text: str):
    await ctx.send(text)
    
@bot.command(name="pf", help="프로필을 보여줍니다!", usage=".pf")
async def ping(message):
    embed = discord.Embed(color=0x7289DA, title=f"{message.author} 프로필")
    embed.set_thumbnail(url=message.author.avatar_url)
    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
    embed.add_field(name="서버 접속일", value=f"{message.author.joined_at.year}년 {message.author.joined_at.month}월 {message.author.joined_at.day}일", inline=False)
    badge = []
    if 784034952303607818 in map(lambda x: x.id, message.author.roles):
        badge.append("<:TEBDEV:784037256242397184>")
    if 776639464415297576 in map(lambda x: x.id, message.author.roles):
        badge.append("<:user:784039384416387072>")

    if len(badge) == 0: embed.add_field(name="서버 전용 뱃지", value=f"> **뱃지가 없습니다.**", inline=False)
    else: embed.add_field(name="서버 전용 뱃지", value=f"> {' '.join(badge)}", inline=False)
    await message.channel.send(embed=embed)

bot.run(os.environ['token'])

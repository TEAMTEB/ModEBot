import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import random
import json
import os
import datetime, ast

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print("준비 완료!")
    print(bot.user.name)
    print(bot.user.id)
    print("------------------------")
    game = discord.Game(".help | MEB 1.5.2 | 팀 텝 공식 포럼 전용 봇! | 실행 오류 해결!")
    await bot.change_presence(status=discord.Status.online, activity=game)

@commands.has_permissions(administrator=True)
@bot.command(name="msg", help="당신이 한 말을 따라합니다.", usage=".msg [말]")
async def Echo(ctx, *, text: str):
    await ctx.send(text)

@bot.command(name="pf", help="프로필을 보여줍니다!", usage=".pf")
async def ping(message):
    embed = discord.Embed(color=0x7289DA, title=f"{message.author}님의 프로필")
    embed.set_thumbnail(url=message.author.avatar_url)
    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
    embed.add_field(name="서버에 들어온 날!", value=f"{message.author.joined_at.year}년 {message.author.joined_at.month}월 {message.author.joined_at.day}일", inline=False)
    badge = []
    if 778136754632654868 in map(lambda x: x.id, message.author.roles):
        badge.append("<:TEBDEV:784037256242397184> 띵이봇 개발자")
    if 776639293484957737 in map(lambda x: x.id, message.author.roles):
        badge.append("<:forum:784229490233704489> 서버 관리자")
    if 779140061740400661 in map(lambda x: x.id, message.author.roles):
        badge.append("<:e_:784229490409996348> 웹사이트 관리자")
    if 783964719455141928 in map(lambda x: x.id, message.author.roles):
        badge.append("<:dsin:784229490418647050> 디자이너")
    if 776639464415297576 in map(lambda x: x.id, message.author.roles):
        badge.append("<:user:784039384416387072> 이용자")
    if 776643196067250197 in map(lambda x: x.id, message.author.roles):
        badge.append(":pushpin: 구독자")
    if 797423897456541707 in map(lambda x: x.id, message.author.roles):
        badge.append("<:boost:797427813959204864> 서버 부스터!")

    if len(badge) == 0: embed.add_field(name="서버 전용 뱃지", value=f"> **뱃지가 없습니다.**", inline=False)
    else: embed.add_field(name="서버 전용 뱃지", value=f"> {' '.join(badge)}", inline=False)
    await message.channel.send(embed=embed)
                    
def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)                          

@bot.command(name='실행')
async def eval_fn(ctx, *, cmd):
    owner = [694017913723682946, 724862211251765250]
    if ctx.author.id in owner:
        msgembed = discord.Embed(title='실행', description='실행이 완료되었어요!')
        msgembed.add_field(name='**INPUT**', value=f'```py\n{cmd}```', inline=False)
        msgembed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        try:
            fn_name = "_eval_expr"
            cmd = cmd.strip("` ")
            cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
            body = f"async def {fn_name}():\n{cmd}"
            parsed = ast.parse(body)
            body = parsed.body[0].body
            insert_returns(body)
            env = {
                'bot': bot,
                'commands': commands,
                'ctx': ctx,
                '__import__': __import__
                }
            exec(compile(parsed, filename="<ast>", mode="exec"), env)

            result = (await eval(f"{fn_name}()", env))
        except Exception as a:
            result = a
        if result == '':
            result = 'None'
        msgembed.add_field(name="**OUTPUT**", value=f'```py\n{result}```', inline=False)    
        await ctx.send(embed=msgembed)
    else:
        await ctx.send("당신의 말은 듣지 못하게 설정되어있어요 ㅜㅜ...")

bot.run(os.environ['token'])

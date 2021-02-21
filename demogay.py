import discord
from discord.ext import commands
from discord import Member
from PIL import Image
import shutil
import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Demo Mesa'))
    print('connected')

@bot.command()
async def gay(ctx, member: Member = None):
    if not member:
        member = ctx.author
    r = requests.get(member.avatar_url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open("gay.webp", 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        size=(128,128)
        Image.open('gay.webp').resize(size).convert('RGBA').save('gay.png', 'png')
        exec(open("gay.py").read())
        await ctx.send(file=discord.File('output.png'))

@bot.command()
async def pfp(ctx, member: Member = None):
    if not member:
        member = ctx.author
    await ctx.send(member.avatar_url)

@bot.command()
@commands.is_owner()
async def restart(ctx):
    await ctx.send("<a:loading:813072468657831946>")
    await bot.logout()

@bot.command()
@commands.is_owner()
async def logout(ctx):
    await ctx.send('\N{WAVING HAND SIGN}')
    await bot.logout()
    await exit(122)

bot.run(token)

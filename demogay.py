import discord
import random
import json
from discord.ext import commands
from discord import Member
from PIL import Image
import shutil
import requests
import os
import subprocess
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
@commands.is_owner()
async def run(ctx, *, content=""):
    if not content:
        await ctx.send("what do i run dumdum? you made me you shouldn't be this dumb. sorry if i hurt your feelings. i am merely your imagination. anyway, i trust you not to enter a dumb command so plz don't break shit.")
        return
    os.system(content)

@bot.command()
async def man(ctx, *, content=""):
    if not content:
        await ctx.send("specify a command dumdum")
        return
    if checknaughty(ctx.author.id):
        await ctx.send("<:bill:814957341187113010> you are on the naughty list and i am rapidly approaching your location")
        return
    if ";" in content:
        await ctx.send("you are now on the naughty list <:pika_gun:814948352877264946>")
        naughty(ctx.author.id)
        return
    if "@" in content:
        await ctx.send(content="there are no manuals for people", file=discord.File("Demoman_autodejectedtie01.wav"))
        return
    man = subprocess.check_output('man ' + content + " | sed '/DESCRIPTION/q' | sed '$d'", shell=True).decode('utf8')
    if not man:
        await ctx.send("sowwy, Dr. Demo doesn't know that command yet. ping that dumdum darky to install it or sumin")
        return
    await ctx.send(man)

@bot.command()
async def pfp(ctx, member: Member = None):
    if not member:
        member = ctx.author
    await ctx.send(member.avatar_url)

@bot.command()
async def react(ctx, *, content = ""):
    if not content:
        await ctx.send("how? dumdum")
        return
    with open('reaction_images.json') as f:
        images = json.load(f)
    if content not in images.keys():
        await ctx.send("ping that dumdum darky and tell her what images to use for this reaction")
        return
    reaction = images.get(content)[random.randint(0, len(images.get(content))-1)]
    await ctx.send(reaction)

@bot.command()
async def patchnotes(ctx):
    notes = subprocess.check_output('git log -1 --pretty=%B', shell=True).deode('utf8').strip()
    await ctx.send(notes)

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

@bot.command()
@commands.is_owner()
async def update(ctx):
    os.system("git pull")
    await ctx.send("<a:loading:813072468657831946>")
    await bot.logout()

def naughty(id):
    with open("naughtylist.txt", "a") as f:
        f.write(str(id) + '\n')

def checknaughty(id):
    with open("naughtylist.txt", "r") as f:
        for line in f.readlines():
            if str(id) in line:
                return True
        return False

bot.run(token)

import discord
from discord.ext import commands



bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run('ODEwOTc1OTA5NjAyMzk0MTUy.YCreLA.w0gyBx0-H9kGLGxybDE9RfFn7Fg')
                                                                                

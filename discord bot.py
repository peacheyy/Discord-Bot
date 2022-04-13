import discord
from discord.ext import commands
import aiohttp
import os

unsplash = os.getenv("ooGw9uAv1MDNQHDWErCg5UIetgOFStXEEutjJqOUeXo")

#client = commands.Bot(command_prefix = '!')
client = discord.Client()

@client.event
async def on_ready():
    print('Logged on as {0.user}!'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')

@client.event
async def  image(ctx, *, search):
    url = f'https://api.unsplash.com/photos/random/?query={search}&orientation=squarish&client_id={unsplash}'
    async with client.ses.get(url) as r:
        if r.status in range(200, 299):
            data = await r.json()
            url = data['urls']['regular']
            mbed = discord.Embed(title = 'here is your image').set_image(url = url)
            await ctx.send(embed = mbed)
        else:
            await ctx.send(f'Error when making request. {r.status}')

client.run('OTU4NDM0OTM5MTEwNTU1NzQ4.YkNSGA.7mlF8lGQNFK4JumXC9KvFfo2Mv8')
#Evan Peachey & Mia Dubac 
#DISCORD BOT
import random
import discord
from discord.ext import commands
from discord.ext.commands import Context
import aiohttp



client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Logged on as {0.user}!'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!')

'''@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')'''
#Evan's code for welcome

'''client_id = "ooGw9uAv1MDNQHDWErCg5UIetgOFStXEEutjJqOUeXo"
client_secret = "GzJQu11kfECh2yWXiPiY6ZMOOt9zRBXol8zw0o7y6JI"
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
code = ""

auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)

api.search.photos("office")'''

'''@client.command()
async def image(ctx, *, search):
    search = search.replace(' ', '')
    url = f'https://api.unsplash.com/photos/random/?query={search}&orientation=squarish&client_id={auth}'
    async with client.ses.get(url) as picture:
        if picture.status in range(200, 299):
            data = await picture.json()
            url = data['urls']['regular']
            mbed = discord.Embed(
                title = 'Here is your image'
                ).set_image(url=url)
            await ctx.send(embed=mbed)
        else:
            await ctx.send(f'Error when making request. {picture.status}')'''
#unfinished code using unsplash for photo search command


@client.command()
async def image(ctx, arg):
    async with aiohttp.ClientSession() as session:
        request = await session.get(f'https://some-random-api.ml/img/{arg}')
        imagejson = await request.json()
    embed = discord.Embed(title = f'{arg}', color = discord.Color.purple())
    embed.set_image(url=imagejson['link'])
    await ctx.send(embed=embed)

@client.command()
async def insult(ctx: Context, *, message: str = None):
    if message is None:
        await ctx.send('choose from .insult (yo mama/roast/tame)\ntype this in the form: .insult yo mama')
    if message == 'yo mama':
        yo_mama_list = ["yo mama so fat I took a picture of her last Christmas and it's still printing", "yo mama is so ugly when she tried to join an ugly contest they said,'Sorry, no professionals'","yo mama so fat and old when God said, 'let there be light,' he asked your mother to move out of the way","yo mama is so fat when she sat on WalMart, she lowered the prices", "yo mama is so fat that Dora can't even explore her","yo mama is so stupid, she put two quarters in her ears and thought she was listenng to 50 Cent","yo mama is so stupid, she climbed over a glass wall to see what was on the other side","yo mama is so fat she doesn't need the internet because she is already world wide","yo mama is so stupid she brought a spoon to the super bowl","yo mama is so fat, when she sat on an iPod she made the iPad","yo mama is so ugly when she took a bath the water jumped out","yo mama so ugly when she went into a haunted house she came out with a job application"]
        yo_mama = random.choice(yo_mama_list)
        insult = ctx.author.display_name + ', ' + yo_mama
        await ctx.send(insult)
    if message == 'roast':
        roast_list = ["sucks at Minecraft","can't play pvp","sucks at Elden Ring","sounds like a 12 year old","has a creepy face","cries too much","should use a glue stick instead of chapstick","should log off","has no thoughts"]
        roast = random.choice(roast_list)
        insult = ctx.author.display_name + " " + roast
        await ctx.send(insult)
    if message == 'tame':
        tame_list = ['stinky','smelly','weird','ugly','dumb','awkward','short','disappointing']
        tame = random.choice(tame_list)
        insult = ctx.author.display_name + ' is ' + tame
        await ctx.send(insult)

#code help
#https://github.com/C4MIV3R/pancakeBot/blob/master/commands/catboy.js


client.run('OTU4NDM0OTM5MTEwNTU1NzQ4.YkNSGA.QUrV9ClTJ1c3sbMNNHbPbL92K08')
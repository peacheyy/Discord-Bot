import random
from discord.ext import commands
import unsplash
from unsplash.api import Api
from unsplash.auth import Auth



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



'''
@client.event
async def  image(ctx, *, search):
    url = f'https://api.unsplash.com/photos/random/?query={search}&orientation=squarish&client_id={unsplash}'
    async with client.ses.get(url) as picture:
        if picture.status in range(200, 299):
        
        else:
            await ctx.send(f'Error when making request. {picture.status}')'''




@client.command()
async def insult(ctx):
    insult = ''
    if ctx.channel.name == 'general':
        if user_message.lower() == '!insult':
            await message.channel.send('choose from !insult (yo mama/roast/tame)')
            await message.channel.send('type this in the form: !insult yo mama')
        elif user_message.lower() == '!insult yo mama':
            yo_mama_list = ["yo mama so fat I took a picture of her last Christmas and it's still printing", "yo mama is so ugly when she tried to join an ugly contest they said,'Sorry, no professionals'","yo mama so fat and old when God said, 'let there be light,' he asked your mother to move out of the way","yo mama is so fat when she sat on WalMart, she lowered the prices", "yo mama is so fat that Dora can't even explore her","yo mama is so stupid, she put two quarters in her ears and thought she was listenng to 50 Cent","yo mama is so stupid, she climbed over a glass wall to see what was on the other side","yo mama is so fat she doesn't need the internet because she is already world wide","yo mama is so stupid she brought a spoon to the super bowl","yo mama is so fat, when she sat on an iPod she made the iPad","yo mama is so ugly when she took a bath the water jumped out","yo mama so ugly when she went into a haunted house she came out with a job application"]
            #http://www.laughfactory.com/jokes/yo-momma-jokes #use this link for yo mama jokes
            yo_mama = random.choice(yo_mama_list)
            insult = insult + {username} + ',' + yo_mama
        elif user_message.lower() == '!insult roast':
            roast_list = ["sucks at Minecraft","can't play pvp","sucks at Elden Ring","sounds like a 12 year old","has a creepy face","cries too much","should use a glue stick instead of chapstick","should log off","has no thoughts"]
            roast = random.choice(roast_list)
            insult = insult + {username} + roast
        elif user_message.lower() == '!insult tame':
            tame_list = ['stinky','smelly','weird','ugly','dumb','awkward','short','disappointing']
            tame = random.choice(tame_list)
            insult = insult + {username} + 'is' + tame

#work on the roasts and tame section a bit more; change it up

'''
@client.event()
async def disastergirl_meme():
    #code to make your profile picture go on the face of disaster girl
'''
#https://github.com/C4MIV3R/pancakeBot/blob/master/commands/catboy.js
#code help

client.run('')
from nextcord.ext import commands
import nextcord
import requests, json, random

links = json.load(open("gifs.json"))
# gateway needed for any intent of the bot
intents = nextcord.Intents.default()
intents.message_content = True

# command line to start a prompt: !cat 'prompt'
bot = commands.Bot(command_prefix='!cat ', intents = intents)
# your personal discord bot token -- can access through discord developer portal
discord_token = 'your_discord_token'

@bot.command(name='pic')
async def cat(ctx):
    # catapi -- get your personal api key
    response = requests.get('https://api.thecatapi.com/v1/images/search?&api_key=your_api_key')
    # get the url key from dictionary in array
    image_link = response.json()[0].get('url') 
    await ctx.send(image_link)

@bot.command(name='gifs', aliases=["cool", "feed", "sleep", "cute", "angry", "play", "random"])
# the aliases are based on the keys in json file
async def gif(ctx):
    # select a random value from json file with invoked aliases
    await ctx.send(random.choice(links[ctx.invoked_with]))

@bot.command(name='hi')
async def SendMessage(ctx):
    # prompt for saying hi
    await ctx.send('Meow human I am cat-gifs')

@bot.event
    # terminal printing
async def on_ready():
    print(f"Logged in as: {bot.user.name}")

bot.run(discord_token)
    
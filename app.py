from nextcord.ext import commands
import nextcord
import requests, json, random

links = json.load(open("gifs.json"))
# this section is important -- i don't know the reason but it doesn't work if you delete it :>>
intents = nextcord.Intents.default()
intents.message_content = True

# command line to start a prompt: !cat 'prompt'
bot = commands.Bot(command_prefix='!cat ', intents = intents)
# your personal discord bot token -- can access through discord developer portal
discord_token = 'your_discord_token'

# 
@bot.command(name='pic')
async def cat(ctx):
    # this api based command used the catapi -- read the .md file to get your own api
    response = requests.get('https://api.thecatapi.com/v1/images/search?&api_key=your_private_api_key')
    # since the json file has different keys and values, you need to specify which key you want to call.
    # in this case, only the url will be used -- but the orig json contains the title, url, width, and height of the element.
    image_link = response.json()[0].get('url') # call the index of the list, and specified the key in dict using 'get' method
    await ctx.send(image_link)

@bot.command(name='gifs', aliases=["cool", "feed", "sleep", "cute", "angry", "play", "random"])
# the aliases are based on the keys in json file
async def gif(ctx):
    # the invoked_with function is a built in function solely for specifying which aliase you used.
    await ctx.send(random.choice(links[ctx.invoked_with]))

@bot.command(name='hi')
async def SendMessage(ctx):
    # prompt for saying hi
    await ctx.send('Hello, human! I am the most useless discord bot in the server. I am here to grant you some cuteness with the power of cat :>')

@bot.event
    # terminal printing
async def on_ready():
    print(f"Logged in as: {bot.user.name}")

bot.run(discord_token)
    
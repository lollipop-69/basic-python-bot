import nextcord # importing nextcord Library to run the bot
from nextcord import Embed, Color # importing Embed and Color
from nextcord.ext import commands # importing the main component 

bot = commands.Bot(command_prefix = "?",case_insensitive = True, strip_after_prefix = True) # creating a bot variable to set a prefix for the bot

@bot.event # event to be triggered when the bot is ready
async def on ready():
    print("BOT IS READY")
  
@bot.command() # a simple ping command to know the websocket latency
async def ping(ctx):
    embed = Embed(title = "Latency", description = f"{round(bot.latency*1000)}",color = Color.random())
    await ctx.send(embed=embed)
    
bot.run("TOKEN") # running the bot using the application token of your bot

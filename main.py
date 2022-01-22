import nextcord
from nextcord import Embed, Color
from nextcord.ext import commands

bot = commands.Bot(command_prefix = "?",case_insensitive = True, strip_after_prefix = True)

@bot.event
async def on ready():
    print("BOT IS READY")
  
@bot.command()
async def ping(ctx):
    embed = Embed(title = "Latency", description = f"{round(bot.latency*1000)}",color = Color.random())
    await ctx.send(embed=embed)
    
bot.run("TOKEN")

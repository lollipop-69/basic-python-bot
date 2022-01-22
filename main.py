import nextcord # importing nextcord Library to run the bot
from nextcord import Embed, Color # importing Embed and Color
from nextcord.ext import commands # importing the main component 

bot = commands.Bot(command_prefix = "?",case_insensitive = True, strip_after_prefix = True) # creating a bot variable to set a prefix for the bot

@bot.event # event to be triggered when the bot is ready
async def on ready():
    print("BOT IS READY")
    
    
    
 

@bot.event

async def on_guild_join(guild):

    with open('./databases/prefixes.json','r') as f:

        prefixes=json.load(f)

    prefixes[str(guild.id)]='?'

    with open('./databases/prefixes.json','w') as f:

        json.dump(prefixes,f,indent=4)

@bot.event

async def on_guild_remove(guild):

    with open('./databases/prefixes.json','r') as f:

        prefixes=json.load(f)

    prefixes.pop(str(guild.id))

    with open('./databases/prefixes.json','w') as f:

        json.dump(prefixes,f,indent=4)

        

@bot.command(aliases = ['setprefix'])

@commands.guild_only()

@commands.has_permissions(administrator=True)

async def prefix(ctx,prefix):

    a = ctx.guild.get_member(bot.user.id)

    j = "Ghost Boy"

    nick = f"[{prefix}] {j}"

    await a.edit(nick=nick)

    with open('./databases/prefixes.json','r') as f:

        prefixes=json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('./databases/prefixes.json','w') as f:

        json.dump(prefixes,f,indent=4)

    jhg=discord.Embed(description=f'**Prefix of the bot for the server has been changed to {prefix}**',color=discord.Color.from_rgb(000,000,205))

    await ctx.send(embed=jhg)   
    
    
    
    
  
@bot.command() # a simple ping command to know the websocket latency
async def ping(ctx):
    embed = Embed(title = "Latency", description = f"{round(bot.latency*1000)}",color = Color.random())
    await ctx.send(embed=embed)
    
bot.run("TOKEN") # running the bot using the application token of your bot

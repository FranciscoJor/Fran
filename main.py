import discord 
from bot_logic import gen_pass
from discord.ext import commands
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hola")
@bot.command()
async def bye(ctx):
    await ctx.send("😎")
@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def repeat(ctx, times: int, content= "repeating..."):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


bot.run()

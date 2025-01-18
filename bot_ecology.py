import discord 
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)
text = "Claro! Aquí tienes los comandos que puedes realizar: $datos -Muestra datos curiosos sobre el impacto ambiental ; $consejos -da consejos de como reducir basura" 


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def ayuda(ctx):
    await ctx.send(text)




bot.run("MTMzMDI1Njg4MTc1OTAzMTQ0MA.GUNIk3.bJHTRTsiBcDsN4UDS6PyEf9ZIE1zkvdcp3a84Y")











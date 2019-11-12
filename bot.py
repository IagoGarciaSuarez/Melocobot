# bot.py
import os
import discord
import rpgbot
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


bot = commands.Bot(command_prefix = '-')
channel = 'bot-commands'

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content=='-saluda' and message.channel.name=='general':
        await message.channel.send('Hola, soy el KoalaBot. Me ha programado OneKoala para relizar funciones útiles y graciosas' +
        'y tenerlas todas en un único bot.')
    elif message.content=='-saluda' and message.channel.name!='general':
        await message.channel.send('No te has leído las normas? Sólo puedes utilizarme en el canal de comandos imonekSmile Este canal es: ' + message.channel.name)
    elif message.content=='-exit':
        await client.logout()

@bot.command(name = 'rpgbotstart')
async def rpgbotgame(message):
    


client.run(TOKEN)


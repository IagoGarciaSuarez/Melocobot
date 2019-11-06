# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content=='-saluda' and message.channel=='#general'
        await message.channel.send('Hola, soy el KoalaBot. Me ha programado OneKoala para relizar funciones útiles y graciosas y tenerlas todas en un único bot.')
    elif message.channel!='#general':
        await message.channel.send('No te has leído las normas? Sólo puedes utilizarme en el canal de comandos imonekSmile')


client.run(TOKEN)


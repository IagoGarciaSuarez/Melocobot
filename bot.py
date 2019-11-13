# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix = '-')
botChannelName = 'bot-commands'

@bot.command(name='botpg')
async def botpg(ctx):
    await botChannel.send('prueba correcta')


@bot.event
async def on_ready():
    global botChannel
    botChannel = discord.utils.get(bot.get_all_channels(), name=botChannelName)
    await botChannel.send('Listo para funcionar. Vuestros deseos son órdenes ( ° ͜ʖ °)\nUtiliza -help para ver los comandos disponibles.')


bot.run(TOKEN)


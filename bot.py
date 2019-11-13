# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix = '-')
channel = None


@bot.command(name='test')
async def test(ctx):
    
    await channel.send('prueba')


@bot.event
async def on_ready():
    #channel = discord.utils.get(ctx.guild.channels, name='bot-commands')
    #channel.send('Listo para funcionar. Vuestros deseos son órdenes ( ° ͜ʖ °)')
    for g in bot.get_all_channels():
        print('Channel: {}\tID: {}'.format(g.name, g.id))
    await bot.logout()
bot.run(TOKEN)


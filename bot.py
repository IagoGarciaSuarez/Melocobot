# bot.py
import os
import discord
from BotPG import Game_BotPG
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

prefix = '%'
bot = commands.Bot(command_prefix = prefix)
botChannelName = 'bot-commands'


def check(author):
    def inner_check(option): 
        if option.author != author:
            return False
        return True 
    return inner_check

@bot.command(name='botpg')
async def botpg(ctx, *arg):

    if not arg:
        response = Game_BotPG.gameStart(ctx.message.author.name, ctx.message.author.id)
        await botChannel.send(response[1])

    elif arg[0] == 'np':

        try:
            await botChannel.send('Escribe el nombre de tu personaje.')
            nombrePj = await bot.wait_for('message', check=check(ctx.author), timeout = 10)
            char = Game_BotPG.charCreation(nombrePj.content)
            await botChannel.send(char.__str__)
        
        except TimeoutError:
            await botChannel.send(f'<@{ctx.author.id}> No has escrito nada en el nombre.')

        


@bot.event
async def on_ready():
    global botChannel
    botChannel = discord.utils.get(bot.get_all_channels(), name=botChannelName)
    print('Bot preparado.')
    await botChannel.send(f'Listo para funcionar. Vuestros deseos son órdenes ( ° ͜ʖ °)\nUtiliza {prefix}help para ver los comandos disponibles.')

bot.run(TOKEN)


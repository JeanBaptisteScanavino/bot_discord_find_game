import discord
from dotenv import load_dotenv
import requests

import os


load_dotenv(dotenv_path="config")
client = discord.Client()

@client.event
async def on_ready():
    print('le bot est prêt')

@client.event
async def on_message(message):
    if message.content[0] == "!":
        await parse_message(message)


def parse_message(message):
    content = (message.content[1::]).split(' ')
    if content[0]  == 'Ping':
        return message.channel.send("Pong")
    elif content[0] == 'list':
        #useCase getList
        # game_list = ["Among Us", "The Forest", "Sea of Thieves", "Mario"]
        game_list = requests.get('http://127.0.0.1:8000/games')
        response  = "\n".join(game_list.json())
        return message.channel.send(f'La liste des jeux est :\n{response}')
    return message.channel.send("Je ne comprend pas le message")

client.run(os.getenv("TOKEN"))
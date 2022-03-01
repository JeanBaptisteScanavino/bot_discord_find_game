import discord
from dotenv import load_dotenv
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
        game_list = ["Among Us", "The Forest", "Sea of Thieves", "Mario"]
        response  = "\n".join(game_list)
        return message.channel.send(f'La liste des jeux est :\n{response}')
    return message.channel.send("Je ne comprend pas le message")

client.run(os.getenv("TOKEN"))
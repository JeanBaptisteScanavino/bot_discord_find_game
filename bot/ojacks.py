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
    if message.content == "Ping":
        await message.channel.send("Pong")


client.run(os.getenv("TOKEN"))

import os
from dotenv import load_dotenv
from personality import PERSONALITY

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

import discord
from google import genai

class Client(discord.Client):
  async def on_ready(self):
    print(f'big daddy is here')
  async def on_message(self, message):
    print("I received:", message.content)
    if message.author.bot:
      return
    if (message.content.startswith("hi jem")):
      trigger = "hi jem"
      prompt = message.content[len(trigger):].strip()
      reply = ask_gemini(prompt)
      await message.channel.send(reply)
      
from gemini import ask_gemini


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents = intents)
client.run(DISCORD_TOKEN)

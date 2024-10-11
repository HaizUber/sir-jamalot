import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Create an instance of Intents
intents = discord.Intents.all()
intents.messages = True  # Allow the bot to receive messages
intents.guilds = True    # Allow the bot to receive guild events
intents.voice_states = True  # Allow the bot to receive voice state updates

# Create a bot instance with the specified intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Define command 
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello Sir, {ctx.author}!")

# Run bot
bot.run(TOKEN)

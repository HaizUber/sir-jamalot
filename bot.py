import discord
from discord.ext import commands

# Create bot instance
bot = commands.Bot(command_prefix="!")

# Define command 
@bot.command()
async def hello(ctx):
    await ctx.send("Hello, {0.author}!".format(ctx))

# run bot
bot.run("YMTI5NDE2MjU4ODAzMjE3NjEzOA.GSgcAv.hFjHIZShOGkQLifCfwXKtbGI_mc3pkqJCTgbkA")

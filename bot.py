import discord
from discord import app_commands
from discord.ext import commands
import json
from os import path
import main

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='Zeta', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(
    name="message",
    description="Message Zeta!"
)
@app_commands.describe(msg = "Message you want to say!")
async def message(interaction: discord.Interaction, msg: str):
    ## interaction.message.author.id

    response = main.ChatMessage(msg, 'user', interaction.user.id)
    await interaction.response.send_message(response)

@bot.tree.command(
    name = "createhistory",
    description= "Creates history with Zeta!"
)
async def createhistory(interaction: discord.Interaction):
    await main.CreateHistory(interaction.user.id)
    await interaction.response.send_message("Created History!")

@bot.tree.command(
    name = "clearhistory",
    description= "Clears history with Zeta!"
)
async def clearhistory(interaction: discord.Interaction):
    main.ClearHistory(interaction.user.id)
    await interaction.response.send_message("Cleared History!")











































bot.run('TOKEN')

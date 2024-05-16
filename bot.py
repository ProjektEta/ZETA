import discord
from discord import app_commands
from discord.ext import commands
import json
from os import path
import main
import BotHandler

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

owner_id = 1053570332339998801

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='Zeta', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

    BotHandler.Mod(owner_id)

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return

    print(ctx.author.id)
    if BotHandler.isMod(ctx.author.id):
        if ctx.content == "$sync":
            try:
                synced = await bot.tree.sync()
                print(f"Synced {len(synced)} command(s)")
            except Exception as e:
                print(e) 

    return
    

@bot.tree.command(
    name="message",
    description="Message Zeta!"
)
@app_commands.describe(msg = "Message you want to say!")
async def message(interaction: discord.Interaction, msg: str):
    ## interaction.message.author.id
    channel_id = interaction.channel
    user = interaction.user

    response = await main.ChatMessage(msg, 'user', interaction.user.id)
    try:
        await interaction.response.send_message(response)
    except Exception as e:
        await channel_id.send(user.mention + "\n" + response)

@bot.tree.command(
    name = "createhistory",
    description= "Creates history with Zeta!"
)
async def createhistory(interaction: discord.Interaction):
    main.CreateHistory(interaction.user.id)
    await interaction.response.send_message("Created History!")

@bot.tree.command(
    name = "clearhistory",
    description= "Clears history with Zeta!"
)
async def clearhistory(interaction: discord.Interaction):
    main.ClearHistory(interaction.user.id)
    await interaction.response.send_message("Cleared History!")

@bot.tree.command(
    name = "upload",
    description="[MODERATOR ONLY] Uploads All Data to the Moderation website"
)
async def upload(interaction: discord.Interaction):
    if BotHandler.isMod():
        main.UploadData(interaction.user.id)
        await interaction.response.send_message("Uploaded Data")

@bot.tree.command(
    name = "mod",
    description="[OWNER] Mods a User"
)
@app_commands.describe(userid = "User you want to mod")
async def mod(interaction: discord.Interaction, userid: str):

    if interaction.user.id == owner_id:
        BotHandler.Mod(userid)
        await interaction.response.send_message("Modded User")
    return

@bot.tree.command(
    name = "unmod",
    description="[OWNER] UnMods a User"
)
@app_commands.describe(userid = "User you want to unmod")
async def unmod(interaction: discord.Interaction, userid: str):
    if interaction.user.id == owner_id:
        BotHandler.UnMod(userid)
        await interaction.response.send_message("UnModded User")
    return

bot.run('TOKEN')

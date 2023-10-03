import discord
import os
import configparser
import datetime
from discord.ext import commands
from discord import Intents

# Load configurations from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Retrieve GitHub configurations
github_token = config.get('GitHub', 'GithubToken')
repo_owner = config.get('GitHub', 'Username')
repo_name = config.get('GitHub', 'Repository')
bot_token = config.get('Discord', 'BotToken')

# Path to your project directory
project_directory = 'C:\\Users\\chand\\Desktop\\Chance\\CREST Bot'

# Recyclone session identifier (customize as needed)
session_identifier = 'RecycloneSession1'

# Recyclone Function
def generate_commit_message(session_id):
    # Customize this message as needed
    message = f"Recyclone Session {session_id} Commit"
    return message

def recyclone_checkpoint(session_id):
    #... (previous Recyclone function code here, ensure paths and commands are valid for your environment)

# Discord Bot
intents = Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.group()
async def recyclone(ctx):
    """
    A group command for Recyclone-related functionalities. 
    If no subcommand is invoked, this will send a usage message.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('Invalid Recyclone command passed...')

@recyclone.command()
async def init(ctx):
    """
    Manually trigger a Recyclone checkpoint.
    """
    try:
        # Ensure the user is an administrator or authorized to trigger Recyclone
        if ctx.message.author.guild_permissions.administrator:
            # Call Recyclone function
            recyclone_checkpoint('ManualCheckpoint')
            await ctx.send("Recyclone checkpoint created successfully.")
        else:
            await ctx.send("You do not have permission to create a checkpoint.")
    except Exception as e:
        await ctx.send(f"Error creating checkpoint: {str(e)}")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")

@bot.event
async def on_message(message):
    # Avoid processing messages sent by the bot itself
    if message.author == bot.user:
        return

    content = message.content

    # Add your previously existing logic here
    # ...

    await bot.process_commands(message)

# Use the bot token from config.ini
bot.run(bot_token)

import os
from typing import Final
from dotenv import load_dotenv
import discord
from discord.ext import commands
import webserver
from discord import Message

# Load environment variables
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Intents setup
intents = discord.Intents.default()
intents.message_content = True

# Create the bot client
client = commands.Bot(command_prefix="!", intents=intents)

# Load cogs (commands from separate files)
COGS = ['cogs.ask', 'cogs.faq', 'cogs.activities']

from utils.message_handler import send_message  # Import your message handler

@client.event
async def on_message(message: Message) -> None:
    """Handle both slash and traditional message-based commands."""
    
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Process traditional commands starting with `!`
    await client.process_commands(message)

    # Process special commands starting with `$` or `?`
    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')

    # Handle custom message-based commands if not empty
    if user_message.startswith('$') or user_message.startswith('?'):
        await send_message(message, user_message)

# Load Cogs when the bot is ready
@client.event
async def on_ready():
    print(f'{client.user} is now running!')
    for cog in COGS:
        try:
            await client.load_extension(cog)
            print(f'Loaded cog: {cog}')
        except Exception as e:
            print(f'Failed to load cog {cog}: {e}')

    # Sync slash commands
    try:
        synced = await client.tree.sync()
        print(f"Slash commands synced: {len(synced)} commands")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# MAIN ENTRY POINT
def main() -> None:
    webserver.keep_alive()
    client.run(TOKEN)

if __name__ == '__main__':
    main()

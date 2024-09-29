from typing import Final
import os
from dotenv import load_dotenv
import discord  # Import discord module
from discord import Intents, Client, Message
from discord.ext import commands
from responses import get_response
import webserver

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True  # NOQA

# Use commands.Bot instead of Client to support commands and slash commands
client = commands.Bot(command_prefix="!", intents=intents)


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    elif is_public := user_message[0] == '!':
        user_message = user_message[1:]
    else:
        return

    try:
        response: str = get_response(user_message)
        if is_private:
            await message.author.send(response)
        elif is_public:
            await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

    # Sync slash commands with the Discord server
    try:
        synced = await client.tree.sync()
        print(f"Slash commands synced: {len(synced)} commands")
    except Exception as e:
        print(f"Failed to sync commands: {e}")


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# Slash command definition
@client.tree.command(name="ask", description="Ask a question using the bot")
async def ask(interaction: discord.Interaction, question: str):
    try:
        # Defer the response to avoid timeout issues
        await interaction.response.defer()

        # Long-running task here (like fetching or processing data)
        response: str = get_response(question)
        
        # Send the actual response after processing
        await interaction.followup.send(response)
    except Exception as e:
        # Handle the error by sending an ephemeral (private) message
        await interaction.followup.send(f"Error: {e}", ephemeral=True)


# MAIN ENTRY POINT
def main() -> None:
    webserver.keep_alive()
    client.run(TOKEN)


if __name__ == '__main__':
    main()

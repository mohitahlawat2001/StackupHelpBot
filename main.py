from typing import Final
import os
from dotenv import load_dotenv
import discord
from discord import Intents, Message
from discord.ext import commands
from responses import get_response, get_response_normal
from scrap_responses import fetch_FAQs , fetch_recent_activities
import webserver

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True  # Enable the message content intent

# Use commands.Bot to support commands and slash commands
client = commands.Bot(command_prefix="!", intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if user_message[0] == '?':
        user_message = user_message[1:]
        response: str = get_response_normal(user_message)
        await message.author.send(response)
    elif user_message[0] == '$':
        user_message = user_message[1:]
        response: str = get_response_normal(user_message)
        await message.channel.send(response)

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

    # Process commands first
    await client.process_commands(message)  # Ensure commands are processed

    # After processing commands, you can send messages if needed
    await send_message(message, user_message)

# Define the traditional !ask command
@client.command(name="ask")
async def ask_command(ctx, *, question: str):
    """Handles the !ask command."""
    try:
        # Respond with the answer using get_response function
        response: str = get_response(question)
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Error: {e}")

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

# Slash command definition
@client.tree.command(name="faq", description="Fetch the FAQ list")
async def faq(interaction: discord.Interaction):
    try:
        # Defer the response to avoid timeout issues
        await interaction.response.defer()

        # Long-running task here (like fetching or processing data)
        faqs = fetch_FAQs()
        response = "\n".join(faqs)

        # Send the actual response after processing
        await interaction.followup.send(response)
    except Exception as e:
        # Handle the error by sending an ephemeral (private) message
        await interaction.followup.send(f"Error: {e}", ephemeral=True)

# Slash command definition
@client.tree.command(name="recent-activities", description="Fetch recent activities")
async def activities(interaction: discord.Interaction):
    try:
        # Defer the response to avoid timeout issues
        await interaction.response.defer()

        # Long-running task here (like fetching or processing data)
        activities = fetch_recent_activities()
        response = activities

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

# utils/message_handler.py
from discord import Message
from utils.responses import get_response_normal

async def send_message(message: Message, user_message: str):
    """Handles responses for message-based commands ($ or ?) and sends responses."""
    # Clean up the prefix
    user_message = user_message.strip()

    if not user_message:
        print('(Message was empty or improperly processed)')
        return

    # Handle commands starting with `?` (Direct Message)
    if user_message.startswith('?'):
        user_message = user_message[1:]  # Remove the `?` character
        response = get_response_normal(user_message)
        await message.author.send(response)

    # Handle commands starting with `$` (Channel Message)
    elif user_message.startswith('$'):
        user_message = user_message[1:]  # Remove the `$` character
        response = get_response_normal(user_message)
        await message.channel.send(response)

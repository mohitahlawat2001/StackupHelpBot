# utils/message_handler.py
from discord import Message
from utils.responses import get_response_normal

async def send_message(message: Message, user_message: str):
    """Handles direct message or channel responses based on the user input."""
    if not user_message:
        print('(Message was empty or intents were not enabled properly)')
        return

    if user_message.startswith('?'):
        user_message = user_message[1:]
        response = get_response_normal(user_message)
        await message.author.send(response)
    elif user_message.startswith('$'):
        user_message = user_message[1:]
        response = get_response_normal(user_message)
        await message.channel.send(response)

async def send_large_message(channel, content: str):
    """Helper function to send large messages split into chunks of 2000 characters."""
    if len(content) <= 2000:
        await channel.send(content)
    else:
        for i in range(0, len(content), 2000):
            await channel.send(content[i:i + 2000])
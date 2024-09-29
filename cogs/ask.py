from discord.ext import commands
from discord import app_commands, Interaction
from utils.responses import get_response
from utils.helper import send_large_message

class AskCommand(commands.Cog):
    """Cog for handling ask-related commands."""

    def __init__(self, client):
        self.client = client

    @commands.command(name="ask")
    async def ask_command(self, ctx, *, question: str):
        """Handles the traditional !ask command."""
        try:
            response = get_response(question)
            await ctx.send(response)
        except Exception as e:
            await ctx.send(f"Error: {e}")

    @app_commands.command(name="ask", description="Ask a question using the bot")
    async def ask_slash_command(self, interaction: Interaction, question: str):
        """Handles the slash ask command."""
        try:
            await interaction.response.defer()
            response = get_response(question)
            if len(response) > 2000:
                await interaction.followup.send("Response too long. Sending in parts...")
                await send_large_message(interaction.followup, response)
            else:
                await interaction.followup.send(response)
        except Exception as e:
            await interaction.followup.send(f"Error: {e}", ephemeral=True)

async def setup(client):
    await client.add_cog(AskCommand(client))

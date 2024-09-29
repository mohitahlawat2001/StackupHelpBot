from discord.ext import commands
from discord import app_commands, Interaction
from utils.scrap_responses import fetch_FAQs
from utils.helper import send_large_message

class FaqCommand(commands.Cog):
    """Cog for handling FAQ-related commands."""

    def __init__(self, client):
        self.client = client

    @commands.command(name="faq")
    async def faq_command(self, ctx):
        """Handles the traditional !faq command."""
        try:
            faqs = fetch_FAQs()
            response = "\n".join(faqs)
            await ctx.send(response)
        except Exception as e:
            await ctx.send(f"Error: {e}")

    @app_commands.command(name="faq", description="Fetch the FAQ list")
    async def faq_slash_command(self, interaction: Interaction):
        """Handles the slash faq command."""
        try:
            await interaction.response.defer()
            faqs = fetch_FAQs()
            response = "\n".join(faqs)
            if len(response) > 2000:
                await interaction.followup.send("Response too long. Sending in parts...")
                await send_large_message(interaction.followup, response)
            else:
                await interaction.followup.send(response)
        except Exception as e:
            await interaction.followup.send(f"Error: {e}", ephemeral=True)

async def setup(client):
    await client.add_cog(FaqCommand(client))

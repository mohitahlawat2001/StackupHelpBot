from discord.ext import commands
from discord import app_commands, Interaction
from utils.scrap_responses import fetch_recent_activities
from utils.helper import send_large_message

class ActivitiesCommand(commands.Cog):
    """Cog for handling recent activities-related commands."""

    def __init__(self, client):
        self.client = client

    @commands.command(name="recent-activities")
    async def activities_command(self, ctx):
        """Handles the traditional !recent-activities command."""
        try:
            activities = fetch_recent_activities()
            await ctx.send(activities)
        except Exception as e:
            await ctx.send(f"Error: {e}")

    @app_commands.command(name="recent-activities", description="Fetch recent activities")
    async def activities_slash_command(self, interaction: Interaction):
        """Handles the slash recent activities command."""
        try:
            await interaction.response.defer()
            response = fetch_recent_activities()
            if len(response) > 2000:
                await interaction.followup.send("Response too long. Sending in parts...")
                await send_large_message(interaction.followup, response)
            else:
                await interaction.followup.send(response)
        except Exception as e:
            await interaction.followup.send(f"Error: {e}", ephemeral=True)

async def setup(client):
    await client.add_cog(ActivitiesCommand(client))

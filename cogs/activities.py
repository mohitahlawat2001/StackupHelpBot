from discord.ext import commands
from discord import app_commands, Interaction
from utils.scrap_responses import fetch_recent_activities

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
            activities = fetch_recent_activities()
            await interaction.followup.send(activities)
        except Exception as e:
            await interaction.followup.send(f"Error: {e}", ephemeral=True)

async def setup(client):
    await client.add_cog(ActivitiesCommand(client))

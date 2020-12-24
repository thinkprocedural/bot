import discord
from discord.ext import commands


class Error(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # if command has local error handler, return
        if hasattr(ctx.command, "on_error"):
            return

        # get the original exception
        error = getattr(error, "original", error)

        # command not found
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                title="{}".format("Something went wrong"),
                description="",
                color=discord.Color(0xFF0000),
            )

            embed.add_field(name="Error", value="Command not found", inline=True)
            await ctx.send(embed=embed)
            return


def setup(client):
    client.add_cog(Error(client))

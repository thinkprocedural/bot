import discord
from discord.ext import commands

from ..variables import *
from ..handlers import *


class Error(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        Basic error handler
        """
        # if command has local error handler, return
        if hasattr(ctx.command, "on_error"):
            return

        # get the original exception
        error = getattr(error, "original", error)

        command = ctx.command
        if command == None:
            command = "Command"

        # command not found
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                title="{}".format("Command not found"),
                description="{} is not a valid command".format(ctx.message.content),
                color=color_errr,
            )
            await ctx.send(embed=embed, delete_after=delete_message_delay)
            await ctx.message.delete()
            return


def setup(client):
    client.add_cog(Error(client))

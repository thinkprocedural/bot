import discord
from discord.ext import commands

import re

from ..variables import *

errors_list = {
    "BadArgument": "Bad command arguments provided",
    "BotMissingPermissions": "Sorry I don't have permissions to do that",
    "CheckFailure": "Check failed",
    "CommandNotFound": "That is not a valid command",
    "CommandOnCooldown": "This command is in cooldown, please try again later",
    "DisabledCommand": "This command is disabled",
    "MissingPermissions": "Sorry you don't seem to have permissions to do that",
    "MissingRequiredArgument": "Some required arguments for this command are missing",
    "NoPrivateMessage": "This command can not be used in direct messages",
    "UserInputError": "Something is wrong with your input",
}


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

        # default error handler
        for error_name, error_description in errors_list.items():
            if isinstance(error, getattr(commands, error_name)):
                error_title = re.sub(r"\B([A-Z])", r" \1", error_name)
                embed = discord.Embed(
                    title="{}".format(error_title),
                    description="{}".format(error_description),
                    color=color_errr,
                )
                await ctx.send(embed=embed, delete_after=delete_message_delay)
                await ctx.message.delete()
                return


def setup(client):
    client.add_cog(Error(client))

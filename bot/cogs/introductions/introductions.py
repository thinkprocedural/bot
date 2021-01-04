import discord
from discord.ext import commands

from ..variables import *


class Introductions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        ctx = await self.client.get_context(message)

        # TODO: make this configurable
        if (
            message.channel.name == "introductions"
            and message.author.id != self.client.user.id
        ):
            user = message.author
            user_roles = user.roles

            if len(user_roles) == 1 and user_roles[0].name == "@everyone":
                # TODO: make this configurable
                member_role = [r for r in ctx.guild.roles if r.name == "Member"][0]
                await user.add_roles(member_role)


def setup(client):
    client.add_cog(Introductions(client))

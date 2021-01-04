import discord
from discord.ext import commands

from ..variables import *



class Introductions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.name == "introductions" and message.author.id != self.client.user.id: # TODO: perhaps make this configurable in the environment
            user = message.author
            user_roles = user.roles

            if len(user_roles) == 1 and user_roles[0].name == "@everyone":
                member_role = [r for r in self.client.guilds[0].roles if r.name == "Member"][0] # TODO: perhaps make member role configurable in the environment
                await user.add_roles(member_role)

def setup(client):
    client.add_cog(Introductions(client))

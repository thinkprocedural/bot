import discord
from discord.ext import commands

import os


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def invite(self, ctx):
        target = ctx.author
        invites = await target.guild.invites()
        invite_link = invites[0]

        if invite_link != None:
            await ctx.send(invite_link)
        else:
            pass


def setup(client):
    client.add_cog(Utils(client))

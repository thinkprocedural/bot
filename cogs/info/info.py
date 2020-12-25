import discord
from discord.ext import commands

from ..variables import *


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def info_bot(self, ctx):
        """
        Get information about the bot
        """
        embed = discord.Embed(
            title="About",
            description="Think Procedural - Houdini Discord community",
            color=color_main,
        )
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(
            name="Source", value="https://git.io/thinkprocedural", inline=False,
        )
        embed.set_footer(text=self.client.user.id)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def info_server(self, ctx):
        """
        Get information about the server
        """
        embed = discord.Embed(
            title="About",
            description="Think Procedural - Houdini Discord community",
            color=color_main,
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(
            name="Website", value="https://thinkprocedural.com", inline=False,
        )
        embed.add_field(
            name="Twitter", value="https://twitter.com/thinkprocedural", inline=False,
        )
        embed.set_footer(text=ctx.guild.id)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))

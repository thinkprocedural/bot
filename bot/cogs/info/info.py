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
        if isinstance(ctx.channel, discord.channel.DMChannel):
            return

        embed = discord.Embed(
            title="About the Bot",
            description="",
            color=color_main,
        )
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(
            name="{}".format(self.client.user),
            value=bot_description,
            inline=False,
        )
        embed.add_field(
            name="Source",
            value=bot_source_code,
            inline=False,
        )
        embed.set_footer(text=self.client.user.id)
        await ctx.send(embed=embed, delete_after=delete_message_delay)
        await ctx.message.delete()

    @commands.command(pass_context=True)
    async def info_server(self, ctx):
        """
        Get information about the server
        """
        if isinstance(ctx.channel, discord.channel.DMChannel):
            return

        embed = discord.Embed(
            title="About the Server",
            description="",
            color=color_main,
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(
            name="{}".format(ctx.guild),
            value="{}".format(""),
            inline=False,
        )
        embed.set_footer(text=ctx.guild.id)
        await ctx.send(embed=embed, delete_after=delete_message_delay)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Info(client))

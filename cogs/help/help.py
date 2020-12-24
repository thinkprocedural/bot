import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def info(self, ctx):
        embed = discord.Embed(
            title="Help", description="", color=discord.Color(0xFFFFFF),
        )
        embed.set_author(name="")

        embed.add_field(
            name="Title",
            value="Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nQuisque porttitor nunc viverra faucibus egestas.",
            inline=False,
        )

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))

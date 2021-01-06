import discord
from discord.ext import commands

import asyncio
import os
from ..variables import *


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def invite(self, ctx):
        """
        Get the latest invite link
        """

        target = ctx.author
        invites = await target.guild.invites()
        invite_link = invites[0]

        if invite_link != None:
            await ctx.send(invite_link)
        else:
            pass

    @commands.Cog.listener()
    async def on_message(self, message):
        ctx = await self.client.get_context(message)

        # give "Member" role after introduction
        if (
            message.channel.name == "introductions"
            and message.author.id != self.client.user.id
        ):
            user = message.author
            user_roles = user.roles

            if len(user_roles) == 1 and user_roles[0].name == "@everyone":
                member_role = [r for r in ctx.guild.roles if r.name == "Member"][0]
                await user.add_roles(member_role)

        # check jobs message for validation
        JOBS_PREFIXES = ["**[PAID]**", "**[UNPAID]**", "**[FOR HIRE]**"]
        if message.author.id != self.client.user.id:
            if message.channel.name == "jobs":
                if any(
                    [message.content.startswith(prefix) for prefix in JOBS_PREFIXES]
                ):
                    embed = discord.Embed(
                        title="{}".format("Done"),
                        description="{}".format("Your job post was sent successfully."),
                        color=color_done,
                    )
                    await ctx.send(embed=embed, delete_after=delete_message_delay)
                else:
                    embed = discord.Embed(
                        title="{}".format("Error"),
                        description="Your message doesn't seem to have the correct format, it will be deleted in 30 seconds.\nPlease try again using one of the following prefixes:\n{}".format(
                            "\n".join([f"`{prefix}`" for prefix in JOBS_PREFIXES])
                        ),
                        color=color_errr,
                    )
                    await ctx.send(embed=embed, delete_after=delete_message_delay)
                    await asyncio.sleep(30)
                    await message.delete()


def setup(client):
    client.add_cog(Utils(client))

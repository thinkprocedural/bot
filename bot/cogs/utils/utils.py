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
        if isinstance(ctx.channel, discord.channel.DMChannel):
            return

        target = ctx.author
        invites = await target.guild.invites()
        invite_link = invites[0]

        if invite_link != None:
            await ctx.send(invite_link)
        else:
            pass

    @commands.Cog.listener()
    async def on_message(self, message):
        # Bot should (for now) never react to its own messages
        if message.author.id == self.client.user.id:
            return

        ctx = await self.client.get_context(message)
        if isinstance(ctx.channel, discord.channel.DMChannel):
            embed = discord.Embed(
                title="{}".format("Hello there!"),
                # TODO: messages like the following description could be extracted to some config file, making the code a lot cleaner to read.
                description="{}".format(
                    "Thank you for messaging me, the bot, but I do not have a lot of functionality to show you via DM right now."
                    "\n\n"
                    "Here's a small Q&A."
                    "\n\n"
                    "**Why can't I post on the server channels?**\n"
                    "Users must use the `#introductions` channel first. Also see the `#read-me-first` channel."
                    "\n\n"
                    "**What am I allowed to post to the `#jobs` channel?**\n"
                    "If you're offering a paid or unpaid job, or are looking for a job, then shoot a message there. Be sure to use the correct tag, i.e. `**[PAID]**`, `**[UNPAID]**`, or `**[FOR HIRE]**`"
                    "\n\n"
                    "**What if I have another question?**\n"
                    "Always feel free to message one of the `@Moderator`s"
                ),
                color=color_main,
            )
            return await ctx.send(embed=embed)

        # give "Member" role after introduction
        if message.channel.name == "introductions":
            user = message.author
            user_roles = user.roles

            if len(user_roles) == 1 and user_roles[0].name == "@everyone":
                member_role = [r for r in ctx.guild.roles if r.name == "Member"][0]
                await user.add_roles(member_role)

        # check jobs message for validation
        JOBS_PREFIXES = ["**[PAID]**", "**[UNPAID]**", "**[FOR HIRE]**"]
        if message.channel.name == "jobs":
            if any([message.content.startswith(prefix) for prefix in JOBS_PREFIXES]):
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

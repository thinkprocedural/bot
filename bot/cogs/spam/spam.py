import os
import pathlib
import time
import asyncio

from discord.ext import commands

from ..variables import *

spam_log_file_clear_interval = 2
spam_log_file = pathlib.Path(os.getcwd()) / "bot" / "cogs" / "spam" / "spam_log.txt"


class Spam(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        # keep resetting file contents to clear out logs
        # so that the spam log is wowrking with "last X seconds"
        while True:
            await asyncio.sleep(spam_log_file_clear_interval)
            with open(spam_log_file, "w") as spam_log:
                spam_log.truncate(0)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.client.user.id:
            return

        ctx = await self.client.get_context(message)

        _timestamp = str(int(time.time()))
        _authorid = str(message.author.id)
        _channelid = str(message.channel.id)

        _log = _timestamp + "___" + _authorid + "___" + _channelid

        counter_messages = 0
        counter_channels = 0
        list_channels = []

        with open(spam_log_file, "r+") as file:
            file.writelines(f"{str(_log)}\n")

            for line in file.readlines():
                log_split = line.split("___")
                log_timestamp = log_split[0]
                log_authorid = log_split[1]
                log_channelid = log_split[2]

                # total number of messages sent by the user, in the last X seconds
                if log_authorid == str(message.author.id):
                    counter_messages += 1
                    list_channels.append(log_channelid)  # add channel id

                # number of unique channels the user has sent messages in
                counter_channels = len(set(list_channels))

        # print("{}, {}, {}".format(counter_messages, counter_channels, _log))

        reason = "[POTENTIAL SPAM]: `{}` has sent `{}` messages in `{}` channels, within 5 seconds".format(
            message.author.name, counter_messages, counter_channels
        )

        if counter_channels >= 3:
            # if the use has sent messages to more than X unique channels - in Y seconds
            # potential spam, ban user
            await message.author.ban(reason=reason, delete_message_days=7)
            """
            embed = discord.Embed(
                title="`{}`".format("[POTENTIAL SPAM]"),
                description=reason,
                color=color_errr,
            )
            await ctx.send(embed=embed)
            """

        """
        embed = discord.Embed(
            title="`{}`".format(counter_messages),
            description="`{}`\n`{}`\n`{}`".format(_timestamp, _authorid, _channelid),
            color=color_errr,
        )
        await ctx.send(embed=embed)
        """


def setup(client):
    client.add_cog(Spam(client))

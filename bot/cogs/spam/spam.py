import discord
import os, pathlib, time, hashlib

from discord.ext import commands

from ..variables import *


spam_log_file = str(
    pathlib.Path(
        os.path.join(
            os.path.abspath(os.getcwd()), "bot", "cogs", "spam", "spam_log.txt"
        )
    ).resolve()
)


class Spam(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.client.user.id:
            return

        ctx = await self.client.get_context(message)

        _timestamp = str(int(time.time()))
        _authorid = str(message.author.id)
        _channelid = str(message.channel.id)

        _log = _timestamp + " " + _authorid + " " + _channelid

        counter_messages = 0
        counter_channels = 0
        list_channels = []
        with open(spam_log_file, "r+") as file:
            file.writelines(f"{str(_log)}\n")
            for line in file.readlines():
                log_split = line.split(" ")
                log_timestamp = log_split[0]
                log_authorid = log_split[1]
                log_channelid = log_split[2]
                if log_authorid == str(message.author.id):
                    counter_messages += 1
                    list_channels.append(log_channelid)
                counter_channels = len(set(list_channels))

        # print("{}, {}, {}".format(counter_messages, counter_channels, _log))

        if counter_channels > 2:
            embed = discord.Embed(
                title="`{}`".format("[POTENTIAL SPAM]]"),
                description="`{}` has sent `{}` messages in `{}` channels, within 5 seconds".format(
                    message.author.name, counter_messages, counter_channels
                ),
                color=color_errr,
            )
            await ctx.send(embed=embed)

        # embed = discord.Embed(
        #     title="`{}`".format(counter_messages),
        #     description="`{}`\n`{}`\n`{}`".format(_timestamp, _authorid, _channelid),
        #     color=color_errr,
        # )
        # await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Spam(client))

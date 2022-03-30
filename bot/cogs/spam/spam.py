import os
import pathlib
import time
import asyncio

from discord.ext import commands

from ..variables import *

SPAM_LOG_FILE_CLEAR_INTERVAL = 2
LOG_DIR = pathlib.Path(os.getcwd()) / "logs"
SPAM_LOG_FILE = LOG_DIR / "spam_log.txt"

if not LOG_DIR.is_dir():
    LOG_DIR.mkdir(parents=True)


class Spam(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.log_channel = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.log_channel = await self.client.fetch_channel(os.getenv("LOG_CHANNEL_ID"))
        # keep resetting file contents to clear out logs
        # so that we are "tracking the last X seconds"
        while True:
            with open(SPAM_LOG_FILE, "w") as spam_log:
                spam_log.truncate(0)

            await asyncio.sleep(SPAM_LOG_FILE_CLEAR_INTERVAL)

    @commands.Cog.listener()
    async def on_message(self, message):
        # ctx = await self.client.get_context(message)
        if message.author.id == self.client.user.id:
            return

        _timestamp = str(int(time.time()))
        _authorid = str(message.author.id)
        _channelid = str(message.channel.id)
        _log = _timestamp + "," + _authorid + "," + _channelid

        counter_messages = 0
        counter_channels = 0
        list_channels = []

        with open(SPAM_LOG_FILE, "r+") as file:
            file.writelines(f"{str(_log)}\n")

            for line in file.readlines():
                log_split = line.split(",")
                log_authorid = log_split[1]
                log_channelid = log_split[2]

                # total number of messages sent by the user, in the last X seconds
                if log_authorid == str(message.author.id):
                    counter_messages += 1
                    list_channels.append(log_channelid)  # add channel id

                # number of unique channels the user has sent messages in
                counter_channels = len(set(list_channels))

        reason = f"[POTENTIAL SPAM]: `{message.author.name}` has sent `{counter_messages}` messages in `{counter_channels}` channels, within {SPAM_LOG_FILE_CLEAR_INTERVAL} seconds"

        if counter_channels >= 3:
            # if the user has sent messages to more than X unique channels - in Y seconds, potential spam, ban user
            await self.log_channel.send(reason)

            # TODO: re-enable after more thorough testing
            # await message.author.ban(reason=reason, delete_message_days=7)


def setup(client):
    client.add_cog(Spam(client))

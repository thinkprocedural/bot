import os
import logging

import discord
from discord.ext import commands


cogs = [
    # cogs list
    "cogs.error.error",
    "cogs.info.info",
    "cogs.init.init",
    "cogs.introductions.introductions",
    "cogs.logs.logs",
    "cogs.utils.utils",
]

TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")

LOGING_LEVEL = os.getenv("LOGING_LEVEL")
if LOGING_LEVEL is not None:
    LOGING_LEVEL = LOGING_LEVEL.upper()

LOGING_LEVEL_OPTIONS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "WARNING"]
if LOGING_LEVEL in LOGING_LEVEL_OPTIONS:
    print("Logging with:", LOGING_LEVEL)
    logging.basicConfig(level=LOGING_LEVEL)


# client initialize
client = commands.Bot(
    command_prefix=PREFIX,
    status=discord.Status.idle,
    activity=discord.Game(name="Initializing"),
)


@client.event
async def on_ready():
    print("=" * 50)
    print("{0.user}".format(client))

    activity = discord.Game(name=f"Houdini")
    await client.change_presence(
        status=discord.Status.online, activity=activity,
    )


if __name__ == "__main__":
    for extension in cogs:
        try:
            client.load_extension(extension)
        except Exception as error:
            print(f'# Could not be loaded: "{extension}"')


client.run(TOKEN)

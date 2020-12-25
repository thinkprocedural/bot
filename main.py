import os
import discord
from discord.ext import commands

cogs = [
    # cogs list
    "cogs.error.error",
    "cogs.help.help",
    "cogs.init.init",
    "cogs.logs.logs",
    "cogs.utils.utils",
]

DISCORD_TOKEN = os.getenv("TOKEN")
COMMAND_PREFIX = os.getenv("PREFIX")

client = commands.Bot(
    command_prefix=COMMAND_PREFIX,
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


client.run(DISCORD_TOKEN)

import os
import discord
from discord.ext import commands

cogs = []
token = os.getenv("TOKEN")

client = commands.Bot(
    command_prefix="!",
    status=discord.Status.idle,
    activity=discord.Game(name="Initializing"),
)


@client.event
async def on_ready():
    print("{0.user}".format(client))
    await client.change_presence(
        status=discord.Status.online, activity=discord.Game(name=f"Houdini")
    )


if __name__ == "__main__":
    for extension in cogs:
        try:
            client.load_extension(extension)
        except Exception as error:
            print(f"{extension} could not be activated. [{error}]")


client.run(token)

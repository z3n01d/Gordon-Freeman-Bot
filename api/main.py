import enum

from api.webserver import start_webserver

import discord
from discord import app_commands
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

class Games(enum.Enum):
    hl1 = 1
    hl2 = 2
    episode1 = 3
    episode2 = 4
    portal = 5
    portal2 = 6

if __name__ == "__main__":
    client = commands.Bot(command_prefix="g!", intents=discord.Intents.all())

    song_group = app_commands.Group(name="song",description="Grouping of song commands")
    
    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")
        client.tree.add_command(song_group)
        try:
            synced = await client.tree.sync()
            print(f"Synced {len(synced)} command(s).")
        except Exception as e:
            print(e)
    
    # Commands for songs
    @song_group.command(
        name="play",
        description="Plays a song"
        )
    @app_commands.describe(
        game="From which game you want your song to be",
        song="Name of a song"
    )
    async def song_play(
        interaction: discord.Interaction,
        game: Games,
        song: str
        ):
        await interaction.response.send_message(f"Game: {game}\nSong: {song}")
    
    start_webserver()

    client.run(DISCORD_TOKEN)
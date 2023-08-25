from discord.ext import commands
from information import Information
from file_management import *
from texts import Texts
from music import Music
from random_list import Random_list
import asyncio
import discord

intents = discord.Intents.default()
intents.message_content = True

token = ""
with open("token.txt") as file:
    token = file.read()

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description='Our Bot that can do everything',
    intents=intents,
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

async def main():
    remove_all_files_from_directory()
    async with bot:    
        await bot.add_cog(Music(bot))
        await bot.add_cog(Texts(bot))
        await bot.add_cog(Information(bot))
        await bot.add_cog(Random_list(bot))
        await bot.start(token)

asyncio.run(main())
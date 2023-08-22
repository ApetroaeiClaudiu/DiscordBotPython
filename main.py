# #py -3 main.py
# bot = MyBot(command_prefix='!', intents=intents)
# bot.run(token)

from discord.ext import commands
from important import Information
from truth import Texts
from music import Music
import asyncio
import discord
import utils

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
    utils.remove_all_files_from_directory()
    async with bot:    
        await bot.add_cog(Music(bot))
        await bot.add_cog(Texts(bot))
        await bot.add_cog(Information(bot))
        await bot.start(token)

asyncio.run(main())
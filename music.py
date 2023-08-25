
from discord.embeds import Embed
from discord.ext import commands
from discord import VoiceClient
from discord.ext.commands import Context
from constants import *
from messages import *
from file_management import *
from youtube import *
import discord
import collections
import asyncio

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.songs_queue = collections.deque([])

    async def play_next_song_callback(self, ctx):
        await send_playing_message(ctx, self.songs_queue[0]['title'])
        await self.play_next_song(ctx)

    def start_playing(self, ctx, source):
        ctx.voice_client.play(source['song'], after=lambda e: asyncio.create_task(self.play_next_song_callback(ctx)) if e is None else None)
        

    def play_next_song(self, ctx):
        if len(self.songs_queue) > 0:
            previous_song = self.songs_queue.popleft()
            remove_file_from_directory('Downloads', previous_song['title'] + '.mp3')
        
        if len(self.songs_queue) > 0:
            song = self.songs_queue[0]
            self.start_playing(ctx, song)
        else:
            asyncio.create_task(send_queue_empty_message(ctx))

    @commands.command()
    async def queue(self, ctx):
        if len(self.songs_queue) == 0:
            await ctx.send("No songs in the queue!")
        else:
            queue = [song['title'] for song in self.songs_queue]    
            queue_list = Embed(title="The songs waiting to be played:", color=0xEC33FF)

            for song in queue:
                queue_list.add_field(name=song, value='', inline=False)
            
            await ctx.send(embed=queue_list)
            
    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, prompt):
        try:
            async with ctx.typing():
                url = get_url(prompt)
                source = generate_source(url)
                
                if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                    self.songs_queue.append(source)
                    user = ctx.author.mention
                    
                    song = generate_new_song_message(source['title'], source['channel'], user)
                    await ctx.send(embed=song)
                else:
                    self.songs_queue.append(source)
                    self.start_playing(ctx, source)
        except Exception as exception:
            await ctx.send(errorMessage)

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
            try:
                ctx.voice_client.stop()
                await ctx.send("Skipping ...")
                self.play_next_song(ctx)
            except Exception as exception:
                await ctx.send(errorMessage)
        else:
            await ctx.send("No song is playing at the moment ...")

    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")
        
        if ctx.message.author.server_permissions.administrator:
            ctx.voice_client.source.volume = volume / 100
            await ctx.send(f"Changed volume to {volume}%")
        else:
            await ctx.send("You do not have the correct permissions to do that!")

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client.is_paused() :
            try:
                await ctx.send("Resumed !!")
                ctx.voice_client.resume()
            except Exception as exception:
                await ctx.send(errorMessage)
        else:
            await ctx.send("I wasn't playing anything before !!")

    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client.is_playing() :
            try:
                await ctx.send("Paused !!")
                ctx.voice_client.pause()
            except Exception as exception:
                await ctx.send(errorMessage)
        else:
            await ctx.send("Nothing is being played at the moment !!")

    @commands.command()
    async def stop(self, ctx):
        ctx.voice_client.disconnect()

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
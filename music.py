
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
import time

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.songs_queue = collections.deque([])
        self.user_cooldowns = {}

    def start_playing(self, ctx, source):
        ctx.voice_client.play(source['song'], after=lambda e: self.play_next_song(ctx) if e is None else None)
        try:
            asyncio.create_task(send_playing_message(ctx, source['title']))
        except Exception as exception:
            print(exception)

    def play_next_song(self, ctx):
        if len(self.songs_queue) > 0:
            previous_song = self.songs_queue.popleft()
            try:
                remove_file_from_directory('Downloads', previous_song['uuid'] + '.mp3')
            except Exception as exception:
                print(exception)
        
        if len(self.songs_queue) > 0:
            song = self.songs_queue[0]
            self.start_playing(ctx, song)
        else:
            asyncio.create_task(send_queue_empty_message(ctx))

    async def release_user_from_cooldown(self, user_id):
        await asyncio.sleep(10)  # Pauza timp de 10
        del self.user_cooldowns[user_id]  # Scoate utilizatorul din pauză

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
        if ctx.author.id in self.user_cooldowns and time.time() - self.user_cooldowns[ctx.author.id] < 60:
            await ctx.send(timeoutMessage)
            return
        
        self.user_cooldowns[ctx.author.id] = time.time()
        asyncio.create_task(self.release_user_from_cooldown(ctx.author.id))

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
            await ctx.send(exception)

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
            try:
                ctx.voice_client.pause()
                await ctx.send("Skipping ...")
            except Exception as exception:
                await ctx.send(exception)
        else:
            await ctx.send("No song is playing at the moment ...")
            return
        
        self.play_next_song(ctx)

    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")
        
        if ctx.author.guild_permissions.administrator:
            if volume < 1 or volume > 100:
                await ctx.send("Invalid value for the volume! Please choose a value between 1-100!")
            else:
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
                await ctx.send(exception)
        else:
            await ctx.send("I wasn't playing anything before !!")

    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client.is_playing() :
            try:
                await ctx.send("Paused !!")
                ctx.voice_client.pause()
            except Exception as exception:
                await ctx.send(exception)
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
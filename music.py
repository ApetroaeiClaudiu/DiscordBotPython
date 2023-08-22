
from discord.embeds import Embed
from discord.ext import commands
from discord import VoiceClient
from discord.ext.commands import Context
from constants import *
import utils
import discord
import collections

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.songs_queue = collections.deque([])

    def start_playing(self, ctx, source):
        ctx.voice_client.play(source['song'], after=lambda e: print(f'Player error: {e}') if e else None)

    def play_next_song(self, ctx):
        song = self.songs_queue[0]
        self.start_playing(ctx, song)

    def generate_new_song_message(self, title, channel, user):
        song = Embed(title="Music Player", description='A new song has been addded to the queue', color=0x990A0A)
        song.add_field(name='Music', value=title, inline=False)
        song.add_field(name='Author', value=channel, inline=False)
        song.add_field(name='Added by', value=user, inline=False)

        return song
    
    def generate_song_playing_message(self, title):
        song = Embed(title="Music Player", description='A song is playing', color=0x0A1E99)
        song.add_field(name='Music', value=title, inline=False)

        return song

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
                url = utils.get_url(prompt)
                source = utils.generate_source(url)
                
                if ctx.voice_client.is_playing():
                    self.songs_queue.append(source)
                    user = ctx.author.mention
                    
                    song = self.generate_new_song_message(source['title'], source['channel'], user)
            
                    await ctx.send(embed=song)
                else:
                    self.songs_queue.append(source)
                    ctx.voice_client.play(source['song'], after=lambda e: print(f'Player error: {e}') if e else None)
                    
                    song = self.generate_song_playing_message(source['title'])
            
                    await ctx.send(embed=song)
        except Exception as exception:
            await ctx.send(exception)

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client.is_playing():
            try:
                ctx.voice_client.stop()
                #retrieve the song that is playing right now and remove it from queue + the downloads directory
                # song = self.queue.popleft()
                # utils.remove_file_from_directory('Downloads', song[1] + '.mp3')
                self.songs_queue.popleft() 
                await ctx.send("Skipping ...")
                
                if len(self.songs_queue) == 0:
                    await ctx.send("No more songs in the queue ...")
                else:
                    self.play_next_song(ctx)
            except Exception as exception:
                await ctx.send(exception)
        else:
            self.songs_queue.popleft()
            await ctx.send("Skipping ...")
            if len(self.songs_queue) == 0:
                await ctx.send("No more songs in the queue ...")
            else:
                self.play_next_song(ctx)

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
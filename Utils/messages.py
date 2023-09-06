from discord.embeds import Embed
from Constants.colors import *

def generate_new_song_message(title, channel, user):
    song = Embed(title="Music Player", description='A new song has been addded to the queue', color=dark_red)
    song.add_field(name='Music', value=title, inline=False)
    song.add_field(name='Author', value=channel, inline=False)
    song.add_field(name='Added by', value=user, inline=False)

    return song
    
def generate_song_playing_message(title):
    song = Embed(title="Music Player", description='A song is playing', color=dark_blue)
    song.add_field(name='Music', value=title, inline=False)
    
    return song

async def send_playing_message(ctx, title):
    song = generate_song_playing_message(title)
    await ctx.send(embed=song)

async def send_queue_empty_message(ctx):
    await ctx.send("No more songs in the queue ...")
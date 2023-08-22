from discord.embeds import Embed

def generate_new_song_message(title, channel, user):
    song = Embed(title="Music Player", description='A new song has been addded to the queue', color=0x990A0A)
    song.add_field(name='Music', value=title, inline=False)
    song.add_field(name='Author', value=channel, inline=False)
    song.add_field(name='Added by', value=user, inline=False)
    return song
    
def generate_song_playing_message(title):
    song = Embed(title="Music Player", description='A song is playing', color=0x0A1E99)
    song.add_field(name='Music', value=title, inline=False)
    return song

async def send_playing_message(ctx, title):
    song = generate_song_playing_message(title)
    await ctx.send(embed=song)

async def send_queue_empty_message(ctx):
    await ctx.send("No more songs in the queue ...")
from pytube import YouTube
from pytube import Channel
import urllib.parse, urllib.request, re
import discord
import uuid

def get_url(prompt):
    query_string = urllib.parse.urlencode({'search_query': prompt})
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                htm_content.read().decode())
    url = 'http://www.youtube.com/watch?v=' + search_results[0]

    return url

def generate_source(url):
    song_uuid = str(uuid.uuid4())

    video = YouTube(
        url,
        use_oauth=True,
        allow_oauth_cache=True)
    
    curl = video.channel_url

    stream = video.streams.filter(only_audio=True).first()
    stream.download(filename=f"Downloads/{song_uuid}.mp3")

    channel = Channel(curl)
    channel_name = channel.channel_name

    source = {
        'song' : discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(source=f"Downloads/{song_uuid}.mp3")),
        'title' : video.title,
        'uuid' : song_uuid,
        'channel' : channel_name}

    return source
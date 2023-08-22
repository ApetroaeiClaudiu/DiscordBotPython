from pytube import YouTube
from pytube import Channel
import urllib.parse, urllib.request, re
import discord

def get_url(prompt):
    query_string = urllib.parse.urlencode({'search_query': prompt})
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                htm_content.read().decode())
    url = 'http://www.youtube.com/watch?v=' + search_results[0]

    return url

def generate_source(url):
    video = YouTube(url)
    curl = video.channel_url

    stream = video.streams.filter(only_audio=True).first()
    stream.download(filename=f"Downloads/{video.title}.mp3")

    channel = Channel(curl)
    channel_name = channel.channel_name

    source = {
        'song' : discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(source=f"Downloads/{video.title}.mp3")),
        'title' : video.title,
        'channel' : channel_name}

    return source
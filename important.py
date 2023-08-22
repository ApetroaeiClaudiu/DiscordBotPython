from discord import message
from discord.ext import commands
from discord.embeds import Embed

class Information(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def commandslist(self, ctx):
        embed_message = Embed(title="These are the available commands:", color=0x00CCFF)
        embed_message.add_field(name="!rules", value="Server rules", inline=False)
        embed_message.add_field(name="!play argument", value="Adds the required song to the queue", inline=False)
        embed_message.add_field(name="!skip", value="Skips the current song", inline=False)
        embed_message.add_field(name="!pause", value="Pauses the current song", inline=False)
        embed_message.add_field(name="!resume", value="Resumes the current song", inline=False)
        embed_message.add_field(name="!queue", value="Shows all the queued songs", inline=False)
        embed_message.add_field(name="!disconnect", value="Disconnects me from the voice channel :(", inline=False)
        embed_message.add_field(name="!compliment", value="I'm gonna say something cute about you <3", inline=False)
        embed_message.add_field(name="!insult", value="Are you sure about that?", inline=False)
        embed_message.add_field(name="!joke", value="I'm gonna show you the cringiest jokes ever", inline=False)
        await ctx.send(embed=embed_message)
        return

    @commands.command()
    async def rules(self, ctx):
        embed_message = Embed(title="Server rules", color=0xCC0066)
        embed_message.add_field(name="1)", value="You do not talk about Fight Club.", inline=False)
        embed_message.add_field(name="2)", value="You do not talk about Fight Club.", inline=False)
        await ctx.send(embed=embed_message)
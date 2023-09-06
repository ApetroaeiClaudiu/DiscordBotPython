from discord import message
from discord.ext import commands
from discord.embeds import Embed
import random

class Random_list(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.random_list = []

    @commands.command()
    async def add_list(self, ctx, *, item):
        self.random_list.append(item)  
        await ctx.send(f"Added '{item}' to the list.")


    @commands.command()
    async def random_elements(self, ctx, num: int):
        if num > 0 and num <= len(self.random_list):
            selected_elements = random.sample(self.random_list, num)
            result = "\n".join(selected_elements)
            await ctx.send(f"Random {num} elements from the list:\n{result}")
        else:
            await ctx.send("Invalid number of elements or list is empty.")

    @commands.command()
    async def clear_list(self, ctx):
        self.random_list.clear()
        await ctx.send("List has been cleared.")

    @commands.command()
    async def show_list(self, ctx):
        if self.random_list:
            result = "\n".join(self.random_list)
            await ctx.send(f"Current list:\n{result}")
        else:
            await ctx.send("The list is empty.")




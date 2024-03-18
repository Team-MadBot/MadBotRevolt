from classes.bot import MadBot
from revolt.ext import commands

class HelloWorldCog(commands.Cog):
    def __init__(self, bot: MadBot):
        self.bot = bot

    @commands.command()
    async def helloworld(self, ctx: commands.Context, text1: str, *, text2: str):
        await ctx.send(f"Hello world! {text2}! {text1}.")

def setup(bot: MadBot):
    bot.add_cog(HelloWorldCog(bot))

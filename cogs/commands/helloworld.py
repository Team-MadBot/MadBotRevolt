from classes.bot import MadBot
from revolt.ext import commands

class HelloWorldCog(commands.Cog):
    def __init__(self, bot: MadBot):
        self.bot = bot

    @commands.command()
    async def helloworld(self, ctx: commands.Context):
        await ctx.send("Hello world!")

def setup(bot: MadBot):
    bot.add_cog(HelloWorldCog(bot))

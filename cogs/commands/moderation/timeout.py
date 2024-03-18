import revolt
import datetime

from classes.bot import MadBot
from revolt.ext import commands

class TimeoutCog(commands.Cog):
    def __init__(self, bot: MadBot):
        self.bot = bot

    @commands.command(
        name="timeout",
        aliases=[
            "mute",
            "shut-up",
        ],
        usage="timeout @mxdcxt 300 nada"
    )
    async def timeout_cmd(
        self,
        ctx: commands.Context,
        member: revolt.User,
        duration: int,
        *,
        reason: str = None,
    ):
        length = datetime.timedelta(minutes=duration)
        await member.timeout(length=length)
        await ctx.message.reply(
            f"Участник {member.mention} замучен на {duration} секунд по причине: {reason or 'Не указана'}!"
        )

def setup(bot: MadBot):
    bot.add_cog(TimeoutCog(bot))

import aiohttp
import traceback
import os

from config import settings
from revolt import Message
from revolt.ext import commands

class MadBot(commands.CommandsClient):
    def __init__(self, token: str, session: aiohttp.ClientSession, prefix: str, *args, **kwargs):
        super().__init__(
            *args,
            token=token,
            session=session,
            **kwargs
        )
        self.prefix = prefix
    
    async def get_prefix(self, message: Message) -> str:
        return self.prefix

    def setup_hook(self):
        for path, _, files in os.walk("cogs"):
            for file in files:
                if not file.endswith(".py"):
                    continue
                egg = os.path.join(path, file)
                if egg in settings.cogs_ignore:
                    continue
                try:
                    self.load_extension(egg.replace(os.sep, ".")[:-3])
                except commands.NoEntryPointError:
                    continue
                except Exception as e:
                    print(f"При загрузке модуля {egg} произошла ошибка: {e}")
                    traceback.print_exc()
                else:
                    print(f"Модуль {egg} успешно загружен.")

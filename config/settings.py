import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")
cogs_ignore = []

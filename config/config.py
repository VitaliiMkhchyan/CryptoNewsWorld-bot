""" Конфиги бота """

from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN")
TIMEOUT_GET_DATA: int = 900

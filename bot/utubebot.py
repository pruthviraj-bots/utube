from pyrogram import Client
from .config import Config

class UtubeBot(Client):
    def __init__(self):
        super().__init__(
            "my_bot_session",  # A session name is required
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,  # Ensure this is set correctly
            plugins=dict(root="bot.plugins"),
            workers=6,
        )
        self.DOWNLOAD_WORKERS = 6
        self.counter = 0
        self.download_controller = {}
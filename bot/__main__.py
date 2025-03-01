import logging
import os
from flask import Flask, request
from .utubebot import UtubeBot
from .config import Config
from pyrogram import Client

app = Flask(__name__)

# Initialize the bot
bot = UtubeBot()

# Set up logging
logging.basicConfig(level=logging.DEBUG if Config.DEBUG else logging.INFO)
logging.getLogger("pyrogram").setLevel(
    logging.INFO if Config.DEBUG else logging.WARNING
)

# Define a route to handle webhook requests
@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    if update:
        bot.process_update(update)
    return '', 200

if __name__ == "__main__":
    # Remove any existing webhook
    bot.remove_webhook()

    # Set the new webhook
    webhook_url = f"{Config.WEBHOOK_URL}/webhook"
    bot.set_webhook(webhook_url)

    # Run the Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
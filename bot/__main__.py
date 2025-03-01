import os
from flask import Flask, request
from pyrogram import Client

# Initialize Flask app
app = Flask(__name__)

# Initialize Pyrogram Client
bot = Client(
    "utube_bot",
    api_id=os.getenv("API_ID"),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    if update:
        bot.process_update(update)
    return '', 200

if __name__ == "__main__":
    # Start the bot
    bot.start()

    # Set webhook
    webhook_url = f"{os.getenv('https://utube-c4qh.onrender.com')}/webhook"
    bot.set_webhook(url=webhook_url)

    # Run Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
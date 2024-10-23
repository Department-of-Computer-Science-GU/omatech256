from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Step 1: Define your command functions
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your Telegram bot. Type anything and I will respond.')

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f'You said: {update.message.text}')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Use /start to begin, or type anything to get an echo!')

# Step 2: Set up the bot
def main():
    # Replace 'YOUR_TELEGRAM_BOT_API_TOKEN' with the token you got from BotFather
    updater = Updater("8053996391:AAFlk6IEU0uq2QQXtPfvNGw7zzeRA-3EO14", use_context=True)

    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Add a message handler to respond to all text messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()

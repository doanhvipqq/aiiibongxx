import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from utils.logger import log
from handlers.chatbot import ChatbotHandler
from handlers.general import GeneralHandler
from keep_alive import keep_alive

# Load Environment
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    log.critical("Token not found in .env file! Exiting...")
    import sys
    sys.exit()

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.error(f"Exc in update: {context.error}")

def main():
    log.info("--- Initializing Antigravity Telegram Bot ---")
    
    # Start keep-alive web server for Render
    keep_alive()
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Handlers
    chatbot = ChatbotHandler()
    general = GeneralHandler()
    
    # Register Commands
    app.add_handler(CommandHandler("start", general.start))
    app.add_handler(CommandHandler("help", general.help))
    app.add_handler(CommandHandler("ping", general.ping))
    app.add_handler(CommandHandler("cleanup", general.cleanup)) 
    
    app.add_handler(CommandHandler("chat", chatbot.chat_command))
    app.add_handler(CommandHandler("profiles", chatbot.list_profiles))
    app.add_handler(CommandHandler("profile", chatbot.set_profile))
    
    # Message Handler (Chatbot)
    # Filters.text & ~Filters.COMMAND ensures we only reply to text that isn't a command
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chatbot.on_message))
    
    app.add_error_handler(error_handler)

    log.info("--- System Operational ---")
    app.run_polling()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log.critical(f"Fatal Error: {e}")

import time
import platform
import psutil
from telegram import Update
from telegram.ext import ContextTypes
import telegram
from utils.logger import log

class GeneralHandler:
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("🤖 Antigravity Bot Online. Gõ /help để xem danh sách lệnh.")

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_text = (
            "📚 **DANH SÁCH LỆNH**\n\n"
            "🔹 **Lệnh Cơ Bản:**\n"
            "/start - Khởi động bot\n"
            "/help - Xem danh sách lệnh này\n"
            "/ping - Kiểm tra trạng thái hệ thống\n"
            "/cleanup - Dọn dẹp tin nhắn\n\n"
            "🔹 **Lệnh AI Chatbot:**\n"
            "/chat <tin nhắn> - Chat với AI\n"
            "/profiles - Xem danh sách profile AI\n"
            "/profile <tên> - Đổi profile AI\n\n"
            "💡 **Tip:** Gửi tin nhắn trực tiếp để chat với AI, không cần dùng lệnh!\n\n"
            "🤖 _Bot được tạo ra bởi Bóng X_"
        )
        await update.message.reply_text(help_text, parse_mode="Markdown")


    async def ping(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        start_time = time.monotonic()
        msg = await update.message.reply_text("Calculating...")
        end_time = time.monotonic()
        
        latency = (end_time - start_time) * 1000
        
        # System Stats
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        
        text = (
            f"🏓 PONG! System Status\n"
            f"📡 Latency: `{round(latency, 2)}ms`\n"
            f"💻 CPU Load: `{cpu_usage}%`\n"
            f"🧠 RAM Usage: `{ram_usage}%`\n"
            f"🐍 Python: `{platform.python_version()}`\n"
            f"⚙️ Lib: `python-telegram-bot`"
        )
        
        await msg.edit_text(text, parse_mode="Markdown")

    async def cleanup(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        ADMIN_ID = 7509896689
        user_id = update.effective_user.id
        
        if user_id != ADMIN_ID:
            await update.message.reply_text("❌ Chỉ admin mới được dùng lệnh này!")
            return
        
        # Telegram bots can't delete their own messages easily in a bulk way like Discord
        # unless they are admins and tracking message IDs.
        # This is a basic implementation that might just delete the command message
        try:
            await update.message.delete()
            msg = await update.message.reply_text("🧹 Đã dọn dẹp (giả vờ thôi, Telegram khó xóa bulk lắm).")
            # await context.job_queue.run_once(lambda t: msg.delete(), 5) # Requires JobQueue
        except Exception as e:
            await update.message.reply_text(f"Lỗi cleanup: {e}")

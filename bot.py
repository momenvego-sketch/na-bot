import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

WELCOME = """أهلاً بك في زمالة المدمنين المجهولين ❤️

هنا تقدر تلاقي معلومات وروابط تساعدك في طريق التعافي.

اختر من القائمة:"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "💬 جروب واتساب للأعضاء",
                url="https://chat.whatsapp.com/GjK95H7HePf3ERdT95QFgj"
            )
        ],
        [
            InlineKeyboardButton(
                "📍 أماكن اجتماعات إقليم مصر",
                url="https://naegypt.org/ar/meetings"
            )
        ],
        [
            InlineKeyboardButton(
                "🌍 موقع الزمالة العالمي",
                url="https://m.na.org/"
            )
        ],
    ]

    await update.message.reply_text(
        WELCOME,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"NA Bot is running!")

    def log_message(self, format, *args):
        return


def run_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    server.serve_forever()


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is not set")

    threading.Thread(target=run_server, daemon=True).start()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

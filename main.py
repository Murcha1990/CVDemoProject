from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 👉 Вставьте сюда токен, который вы получили у BotFather
TOKEN = "8116849733:AAEeKnf5XdpqFhuTJZr9BV5SyUdZUrirW0E"

# Переменная для хранения последнего фото
last_photo_file_id = None

# Обработка команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋 Пожалуйста, пришлите мне фотографию 📷"
    )

# Обработка фотографий
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_photo_file_id

    # Берём самое большое (лучшее) качество фото
    photo = update.message.photo[-1]
    last_photo_file_id = photo.file_id

    await update.message.reply_text("Спасибо, очень красивая фотография! 🌟")

    # Для проверки выводим file_id в консоль
    print(f"Сохранено фото с file_id: {last_photo_file_id}")

def main():
    app = Application.builder().token(TOKEN).build()

    # Обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()

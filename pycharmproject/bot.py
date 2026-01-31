import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# Настройки
TOKEN = 8295486618
ADMIN_CHAT_ID = 7925732844

# Включим логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Команда /start
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr"Привет {user.mention_markdown_v2()}\! Я бот для приёма заявок на ремонт\. "
        "Напишите /newrequest чтобы создать заявку."
    )


# Команда /newrequest - запуск заявки
def new_request(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [["Да", "Нет"]]
    update.message.reply_text(
        "Опишите вашу проблему:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    # Сохраняем состояние "ожидание описания"
    context.user_data['state'] = 'waiting_for_description'


# Обработка текстовых сообщений
def handle_message(update: Update, context: CallbackContext) -> None:
    user_data = context.user_data
    state = user_data.get('state')

    if state == 'waiting_for_description':
        # Сохраняем описание
        user_data['description'] = update.message.text
        update.message.reply_text("Введите ваш контактный телефон:")
        user_data['state'] = 'waiting_for_phone'

    elif state == 'waiting_for_phone':
        # Сохраняем телефон
        user_data['phone'] = update.message.text
        user = update.effective_user

        # Формируем заявку
        request_text = (
            "🚨 *Новая заявка!*\n"
            f"👤 Пользователь: {user.full_name}\n"
            f"📱 Контакт: {user_data['phone']}\n"
            f"🔧 Описание:\n{user_data['description']}"
        )

        # Отправляем администратору
        context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=request_text,
            parse_mode="Markdown"
        )

        update.message.reply_text("✅ Заявка отправлена! С вами свяжутся в ближайшее время.")
        # Сбрасываем состояние
        user_data.clear()


# Ошибки
def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)



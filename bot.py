from config import BOT_TOKEN
import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    await update.message.reply_text('Введите ваши координаты(coord1, coord2)')


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, start)
    application.add_handler(text_handler)
    application.run_polling()


conv_handler = ConversationHandler(

    entry_points=[CommandHandler('start', start)],
    states={
        # 1: [CommandHandler('first', first_hall)],
        # 2: [CommandHandler('exit', to_exit), CommandHandler('second', second_hall)]
        # 3: [CommandHandler('first', first_hall)],
        # 4: [CommandHandler('exit', to_exit), CommandHandler('second', second_hall)]
    },

    # fallbacks=[CommandHandler('stop', )]
)

# application.add_handler(conv_handler)

if __name__ == '__main__':
    main()

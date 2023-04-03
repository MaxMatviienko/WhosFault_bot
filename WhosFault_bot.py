import random
import telegram
from telegram.ext import Updater, CommandHandler
from PIL import Image, ImageSequence

# список вариантов ответа
options = ["Навальный", "НАТА", "Буданов", "Байден", "Зеленский", "Бульба"]

# функция для выбора рандомного ответа и вывода анимации с рулеткой
def choose_response(update, context):
    # загрузка изображения с крутящейся рулеткой
    animation = Image.open('roulette.gif')

    # отправка сообщения с анимацией
    message = update.message.reply_animation(animation, caption='Кто же сегодня виноват?...')
    
    # выбор рандомного ответа и отправка сообщения
    response = random.choice(options)
    message.edit_caption(f'Ответ: {response}')

# создание объекта бота
bot = telegram.Bot(token='5804833363:AAFoh3jH4XCQGRViEcJ9Rj9RIT589n1i7iE')

# создание объекта обновлений
updater = Updater(token='5804833363:AAFoh3jH4XCQGRViEcJ9Rj9RIT589n1i7iE', use_context=True)

# добавление обработчика команды /choose
updater.dispatcher.add_handler(CommandHandler('choose', choose_response))

# запуск бота
updater.start_polling()
updater.idle()

from config import bot
from telebot import types
from podgon import podgon_func
import pred
data = []
current_question = 0
questions = [
    "Введите возраст",
    "Введите пол",
    "Введите тип боли в груди",
    "Введите значение кровяного давления в состоянии покоя (в мм рт.ст.)",
    "Введите уровень холестерина в мг/дл🧬",
    "Ваш уровень сахара в крови натощак > 120 мг/дл?📈",
    "Укажите результаты электрокардиографии в состоянии покоя🩻",
    "Введите максимальное значение частоты сердечных сокращений🩺",
    "Укажите есть ли стенокардия, вызванная физической нагрузкой🫀",
    "Укажите значение депрессии сегментата ST, вызванной физической нагрузкой относительно покоя",
    "Укажите наклон пикового сегмента ST при физической нагрузке",
    "Введите количество крупных сосудов, окрашенных при рентгеноскопии🩸",
    "Укажите значение талассемии💀"
]


@bot.message_handler(commands=["start"])
def start(message):
    global current_question
    current_question = 0
    bot.send_message(message.chat.id, f"{questions[current_question]}:")




@bot.message_handler(func=lambda message: True, content_types=["text"])
def echo(message):
    global current_question, data
    message_text = message.text

    if current_question < (len(questions)-1):
        data.append(message_text)
        current_question += 1


        if current_question == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Мужской')
            btn2 = types.KeyboardButton('Женский')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, f"{questions[current_question]}:", reply_markup=markup)


        elif current_question == 2:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Типичная стенокардия')
            btn2 = types.KeyboardButton('Атипичная стенокардия')
            btn3 = types.KeyboardButton('Иная боль')
            btn4 = types.KeyboardButton('Бессимптомная')
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, f"{questions[current_question]}:", reply_markup=markup)

        elif current_question == 3:
            bot.send_message(message.chat.id, f"{questions[current_question]}:", reply_markup=types.ReplyKeyboardRemove())

        elif current_question == 5:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Да✅')
            btn2 = types.KeyboardButton('Нет❌')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, f"{questions[current_question]}:", reply_markup=markup)

        elif current_question == 6:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('В норме')
            btn2 = types.KeyboardButton('Наличие аномалии зубца ST-T')
            btn3 = types.KeyboardButton('Наличие вероятной или определенной гипертрофии левого желудочка по критериям Эстеса')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f"{questions[current_question]}:", reply_markup=markup)



        elif current_question == 7:
            bot.send_message(message.chat.id, f"{questions[current_question]}:", reply_markup=types.ReplyKeyboardRemove())

        elif current_question == 8:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Да✅')
            btn2 = types.KeyboardButton('Нет❌')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, f"{questions[current_question]}:", reply_markup=markup)

        elif current_question == 9:
            bot.send_message(message.chat.id, f"{questions[current_question]}:", reply_markup=types.ReplyKeyboardRemove())

        elif current_question == 11:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('0')
            btn2 = types.KeyboardButton('1')
            btn3 = types.KeyboardButton('2')
            btn4 = types.KeyboardButton('3')
            btn5 = types.KeyboardButton('4')
            markup.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.chat.id, f"{questions[current_question]}:", reply_markup=markup)

        elif current_question == 12:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('0')
            btn2 = types.KeyboardButton('1')
            btn3 = types.KeyboardButton('2')
            btn4 = types.KeyboardButton('3')
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, f"{questions[current_question]}:", reply_markup=markup)


        elif current_question < (len(questions)):
            bot.send_message(message.chat.id, f"{questions[current_question]}:")
    else:
        data.append(message_text)
        podgon_func(data)
        output = pred.pred_func([data])
        print(output)
        if output[0] == 1:
            bot.send_message(message.chat.id, "Прогноз: \nУ вас наблюдаются сердечно-сосудистые заболевания")
            bot.send_video(message.chat.id, "https://tenor.com/ru/view/papich-папич-arthas-gif-20124926")
        elif output[0] == 0:
            bot.send_message(message.chat.id, "Прогноз: \nСердечно-сосудистых заболеваний не наблюдается")
            bot.send_video(message.chat.id, "https://tenor.com/ru/view/папич-dance-party-gif-17286024")





if __name__ == '__main__':
    bot.polling(non_stop=True)









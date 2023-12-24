from get_index import find_index

def podgon_func(data_f):
    #Подгоняем данные для пола под таблицу
    d = ['Женский', 'Мужской']
    word = data_f[1]
    data_f[1] = str(find_index(word, d))
    d.clear()

    #Подгоняем данные для типа боли в груди под таблицу
    d = ['Типичная стенокардия', 'Атипичная стенокардия', 'Иная боль', 'Бессимптомная']
    word = data_f[2]
    data_f[2] = str(find_index(word, d))
    d.clear()

    # Подгоняем данные для уровня сахара и стенокардии под таблицу
    d =['Нет❌', 'Да✅']
    word = data_f[5]
    data_f[5] = str(find_index(word, d))
    word = data_f[8]
    data_f[8] = str(find_index(word, d))
    d.clear()

    # Подгоняем данные для результатов электрокардиографии под таблицу
    d = ['В норме', 'Наличие аномалии зубца ST-T', 'Наличие вероятной или определенной гипертрофии левого желудочка по критериям Эстеса']
    word = data_f[6]
    data_f[6] = str(find_index(word, d))
    d.clear()

    return data_f
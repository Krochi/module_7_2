# Задача "Записать и запомнить":
# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
# strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением -
# записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
# info = [
#     'Text for tell.',
#     'Используйте кодировку utf-8.',
#     'Because there are 2 languages!',
#     'Спасибо!'
#     ]
#
# result = custom_write('test.txt', info)
# for elem in result.items():
#   print(elem)
#
# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')
#
#
# Примечания:
# Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
# Не забывайте закрывать файл вызывая метод close() у объектов файла.
# Помните, что при использовании символов не принадлежащих таблице ASCII, вы используете больше байт для записи символа.
# Соответственно для чтения и записи информации из/в файл(-f) потребуется другая кодировка - utf-8.

#Решение:

def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, "w", encoding='utf - 8') as file:
        for index, string in enumerate(strings):
            position = file.tell()
            file.write(string + '\n')
            strings_positions[(index + 1, position)] = string
    return strings_positions

info = [
 'Text for tell.',
 'Используйте кодировку utf-8.',
 'Because there are 2 languages!',
 'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
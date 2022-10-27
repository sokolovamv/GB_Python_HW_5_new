# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from itertools import count
import func_files

path = 'file2.txt'
path_total = 'file2_rle.txt'

# формируем файл на основе введенного текста и читаем его
func_files.write_file_w(path)
text = func_files.read_file_r(path)

# создание списка уникальных символов
unic_symbol = set(text)

# создание списка, куда будет записан текст rle
amount_symbol = []
for i in unic_symbol:
    count = 0
    for j in text:
        if i == j:
            count += 1   # количество каждых символов
    amount_symbol.append(i)
    amount_symbol.append(f'{count}')
text_rle = ''.join(amount_symbol)

# записываем rle текст в файл
func_files.write_file(path_total, text_rle)

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import func_files

path = 'file1.txt'
path1 = 'file1_answer.txt'

# формируем файл на основе введенного текста и читаем его
func_files.write_file_w(path)
text = func_files.read_file_r(path).split()

# создание нового списка
func_files.write_file(path1, ' '.join([i for i in text if 'абв' not in i]))
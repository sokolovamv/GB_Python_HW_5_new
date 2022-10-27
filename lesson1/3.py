# Создайте программу для игры в ""Крестики-нолики"".
import random

# функция, рисующая символ на экране, который вводит игрок
def print_playing(list_with_symbols, coords, symbol):
    # можно рисовать только в пустых ячейках
    if list_with_symbols[coords[0]][coords[1]] == '   ':
        list_with_symbols[coords[0]][coords[1]] = f' {symbol} '
    else:
        print('Там уже стоит символ, вы пропускаете ход')
    # рисуем матрицу
    for i in range(5):
        for j in range(5):
            print(list_with_symbols[i][j], end=' ')
        print()
    # возвращаем вложенный список 
    return list_with_symbols 

# ввод координат (только 1, 2, 3) и формирование самого символа
def create_symbol(list_playing, player, symbol_of_player):
    #  ввод и проверка координат
    coordinates = input("Введите координаты через пробел (номер строки (1,2,3), номер столбца(1,2,3))").split()
    while (int(coordinates[0]) not in [1, 2, 3]) or (int(coordinates[1]) not in [1, 2, 3]):
        coordinates = input("Введите координаты через пробел (номер строки (1,2,3), номер столбца(1,2,3))").split()
    # пока игра не закончилась (выиграли и закончилось поле) меняем ход игрокам и формируем символ
    while end_check(print_playing(list_playing, dictionary(coordinates),symbol_of_player)):
        if player == 1:
            player = 2
            symbol_of_player = 'O'
        else:
            player = 1
            symbol_of_player = 'X'
        # ввод и проверка координат
        coordinates = input("Введите координаты через пробел (номер строки (1,2,3), номер столбца(1,2,3))").split()
        while (int(coordinates[0]) not in [1, 2, 3]) or (int(coordinates[1]) not in [1, 2, 3]):
            coordinates = input("Введите координаты через пробел (номер строки (1,2,3), номер столбца(1,2,3))").split()

# провека на окончание игры
def end_check(play_list):
    #  выиграл какой-то игрок
    if (play_list[0][0] == play_list[0][2] == play_list[0][4]) and play_list[0][0] != '   ' or \
        (play_list[2][0] == play_list[2][2] == play_list[2][4]) and play_list[2][0] != '   ' or \
        (play_list[4][0] == play_list[4][2] == play_list[4][4]) and play_list[4][0] != '   ' or \
        (play_list[0][0] == play_list[2][2] == play_list[4][4]) and play_list[0][0] != '   ' or \
        (play_list[0][0] == play_list[2][0] == play_list[2][4]) and play_list[0][0] != '   ' or \
        (play_list[0][2] == play_list[2][2] == play_list[4][2]) and play_list[0][2] != '   ' or \
        (play_list[0][4] == play_list[2][4] == play_list[4][4]) and play_list[0][4] != '   ' or \
        (play_list[0][4] == play_list[2][2] == play_list[4][0]) and play_list[0][4] != '   ':
        print(f'Игра окончена')
        return False
    # не выиграл никто
    elif play_list[0][0] != '   ' and play_list[0][2] != '   ' and \
        play_list[0][4] != '   ' and play_list[2][0] != '   ' and \
        play_list[2][2] != '   ' and play_list[2][4] != '   ' and \
        play_list[4][0] != '   ' and play_list[4][2] != '   ' and \
        play_list[4][4] != '   ':
        print('Игра окончена, ничья')
        return False
    # продолжение игры
    else:
        print('Продолжаем игру')
        return True

# словарь соответствия ячеек и координат вложенного списка
def dictionary(in_coords):
    dict_coords = \
        {
            '1': 0,
            '2': 2,
            '3': 4
        }
    return [dict_coords[in_coords[0]], dict_coords[in_coords[1]]]

name_1 = input('Представьтесь игрок: ')
name_2 = input('Представьтесь игрок: ')
first_player = random.randint(1,2)
if first_player == 1:
    print(f'Первым ходит {name_1}')
else:
    print(f'Первым ходит {name_2}')
# начало игры
border_list = [['   ', '|', '   ', '|', '   '], \
                [' - ', '|', ' - ', '|', ' - '], \
                ['   ', '|', '   ', '|', '   '], \
                [' - ', '|', ' - ', '|', ' - '], \
                ['   ', '|', '   ', '|', '   ']]
create_symbol(border_list, 1, 'X')

    


# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

# Игра игрока против игрока
def player_vs_player(leftover_candy, max_candy, player):
    print(f'Первым ходит игрок {player}')
    amount_of_candy = [0, 0]    # количество конфет у каждого игрока
    while leftover_candy != 0:  # пока остаток конфет не равен 0 игра продолждается
        taken_candy = int(input("Сколько Вы берете конфет? "))
        while taken_candy > 28: # проверка на количество взятых конфет
            taken_candy = int(input("Выберите количество конфет не больше 28: "))
        if max_candy >= leftover_candy: # если количество оставшихся конфет меньше 28, то взять можно не больше этого значения
            taken_candy = leftover_candy
        leftover_candy -= taken_candy   # остаток конфет на столе
        if player == 1:
            amount_of_candy[0] += taken_candy   # количество конфет у первого игрока
            if sum(amount_of_candy) == total_candy: # проверка на окончание конфет
                return [player,amount_of_candy[0]]
            else:
                player = 2
        elif player == 2:
            amount_of_candy[1] += taken_candy # количество конфет у второго игрока
            if sum(amount_of_candy) == total_candy:  # проверка на окончание конфет
                print(amount_of_candy)
                return [player,amount_of_candy[1]]
            else:
                player = 1

# Игра против бота: меняется то, бот выбирает количество рандомом
def player_vs_bot(leftover_candy, max_candy, player):
    print(f'Первым ходит игрок {player}')
    amount_of_candy = [0, 0]
    while leftover_candy != 0:
        print(f'Осталось {leftover_candy} конфет')
        if player == 1:
            taken_candy = int(input("Сколько Вы берете конфет? "))
            while taken_candy > 28:
                taken_candy = int(input("Выберите количество конфет не больше 28: "))
        else:
            taken_candy = randint(1, max_candy)
            print(f'Бот взял {taken_candy} конфет')
        if max_candy >= leftover_candy:
            taken_candy = leftover_candy
        leftover_candy -= taken_candy
        if player == 1:
            amount_of_candy[0] += taken_candy
            if sum(amount_of_candy) == total_candy:
                print(amount_of_candy)
                return [player,amount_of_candy[0]]
            else:
                player = 2
        elif player == 2:
            amount_of_candy[1] += taken_candy
            if sum(amount_of_candy) == total_candy:
                print(amount_of_candy)
                return [player,amount_of_candy[1]]
            else:
                player = 1  


total_candy = 2021
step_candy = 28
print('В какую игру вы хотите поиграть. С ботом или со вторым игроком? ')
choice_play = int(input('Нажмите 1, если с ботом, нажмите 2, если с другим игроком: '))
first_player = randint(1,2)
# игра с ботом
if choice_play == 1:
    winner = player_vs_bot(total_candy, step_candy, first_player)
    # играем до тех пор, пока не выиграет первый игрок
    while winner[0] != 1:
        winner = player_vs_bot(total_candy, step_candy, first_player)
# игра с другим игроком 
elif choice_play == 2:
    winner = player_vs_player(total_candy, step_candy, first_player)
    # играем до тех пор, пока не выиграет первый игрок
    while winner[0] != 1:
        winner = player_vs_player(total_candy, step_candy, first_player)
print(f'Количество монет, которые взял первый игрок, чтобы выиграть: {winner[1]}')








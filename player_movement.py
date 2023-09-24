import random
import math
import subprocess
import os
import PlayingField

def clear_console():
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)

def player_movement(print_playing_field, arr, rows, column):
    pF = PlayingField(rows, column, 30)

    сheck_rows = rows
    check_column = column
    rows -= 1
    for j in range(column):
        if pF.field[rows][column] == 0:
            continue
        else:
            column = j
            pF.field[rows][column] = '\033[31m*\033[0m'
            break
    print('playing field: ')

    pF.print_playing_field()

    while(arr[rows][j] != -1):
        clear_console()


        if rows == 0:
            print("\033[33mYou WON!!!\033[0m")
            return 0

        move = input('Where should I go?: ')

        if move == 'w':
            if rows - 1 == -1:
                print('\n You can’t go there: \n')
                continue
            pF.field[rows][column] = '1'

            rows -= 1
            if arr[rows][column] == 0:
                print('You lost')
                return 0
            pF.field[rows][column] = '\033[31m*\033[0m'
            pF.print_playing_field()

        if move == 'a':
            if column - 1 == -1:
                print('\n You can’t go there: \n')
                continue
            pF.field[rows][column] = '1'

            column -= 1
            if pF.field[rows][column] == 0:
                print('You lost')
                return 0
            pF.field[rows][column] = '\033[31m*\033[0m'
            pF.print_playing_field()
        if move == 'd':
            if column + 1 == check_column:
                print('\n You can’t go there: \n')
                continue
            pF.field[rows][column] = '1'

            column += 1
            if pF.field[rows][column] == 0:
                print('You lost')
                return 0
            pF.field[rows][column] = '\033[31m*\033[0m'
            pF.print_playing_field()
        if move == 's':
            if rows + 1 == сheck_rows:
                print('\n You can’t go there: \n')
                continue
            arr[rows][column] = '1'

            rows += 1
            if pF.field[rows][column] == 0:
                print('You lost')
                return 0
            pF.field[rows][column] = '\033[31m*\033[0m'
            pF.print_playing_field()
        if move == 'e':
            if rows - 1 == -1 or column - 1 == check_column:
                print('\n You can’t go there: \n')
                continue
            arr[rows][column] = '1'

            column += 1
            rows -= 1
            if arr[rows][column] == 0:
                print('You lost')
                return 0
            arr[rows][column] = '\033[31m*\033[0m'
            #print_playing_field(arr, сheck_rows, check_column)
            pF.print_playing_field(arr, сheck_rows, check_column)
        if move == 'q':
            arr[rows][column] = 1
            if rows - 1 == -1 or column-1 == -1:
                print('\n You can’t go there: \n')
                continue
            arr[rows][column] = '1'

            column -= 1
            rows -= 1
            if arr[rows][column] == 0:
                print('You lost')
                return 0
            arr[rows][column] = '\033[31m*\033[0m'
            pF.print_playing_field(arr, сheck_rows, check_column)
# def input_matrix(arr, rows, column, chance):
#
#     array_size = rows * column
#
#     count_0 = int(array_size * (chance / 100))
#
#     count_1 = array_size - count_0
#
#     generated_array = [0] * math.floor(count_0) + [1] * math.floor(count_1)
#     print(generated_array)
#
#     random.shuffle(generated_array)
#     counter = 0
#
#     for i in range(rows):
#         for j in range(column):
#             arr[i][j] = generated_array[counter]
#             counter += 1
#
#     return arr

# def print_playing_field(arr, rows, column):
#     print()
#
#     for i in range(rows):
#         for j in range(column):
#             print(arr[i][j], end=' ')
#         print()
#     # Зміна кольору тексту на червоний
#     print("\033[31mЦей текст червоний.\033[0m")
#
#     # Зміна кольору тексту на жовтий
#     print("\033[33mЦей текст жовтий.\033[0m")

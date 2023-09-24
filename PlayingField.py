import random

class PlayingField:
    def __init__(self, rows, colums, chance):
        self.rows = rows
        self.colums = colums
        self.chance = chance
        self.field = [[0 * colums for _ in range(rows)]]

    def input_matrix(self):
        array_size = self.rows * self.colums
        count_0 = int(array_size * (self.chance / 100))
        count_1 = array_size - count_0
        generated_array = [0] * count_0 + [1] * count_1
        print(generated_array)
        random.shuffle(generated_array)
        counter = 0

        for i in range(self.rows):
            for j in range(self.colums):
                self.field[i][j] = generated_array[counter]
                counter += 1
        return self.field

    def print_playing_field(self):
        print()
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.field[i][j], end=' ')
            print()
        # Зміна кольору тексту на червоний
        print("\033[31mЦей текст червоний.\033[0m")

        # Зміна кольору тексту на жовтий
        print("\033[33mЦей текст жовтий.\033[0m")



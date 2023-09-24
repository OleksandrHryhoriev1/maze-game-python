import player_movement
import PlayingField
i = 11
j = 13
chance = 30




# playing_field = [[0] * j for _ in range(i)]
# print(playing_field)



pF.input_matrix()
for_print = pF.print_playing_field()
pF.print_playing_field()
player_movement.print_playing_field()

player_movement.player_movement(for_print, playing_field, i, j)















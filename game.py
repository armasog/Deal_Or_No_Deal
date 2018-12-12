import game_engine as ge

print('Welcome to Deal Or No Deal!')
ge.print_board()
print('Choose your case to keep throughout the game!')
player_case = ge.pick_case()
print('Great! Let\'s play Deal or No Deal!')
ge.print_board()

#  All possible rounds of gameplay are listed, however they will only run if ge.game_over is false
ge.play_round(6)
ge.play_round(5)
ge.play_round(4)
ge.play_round(3)
ge.play_round(2)
ge.play_round(1)
ge.play_round(1)
ge.play_round(1)
ge.play_round(1)
if not ge.game_over:
    print('Congratulations! You have finished the game with {}!'.format(ge.switch_case(player_case)))

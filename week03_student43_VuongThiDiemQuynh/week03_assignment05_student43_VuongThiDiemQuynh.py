#Write a program for 2-player rock, paper, scissors game

while True:
    player_1 = input("Player 1: Rock, paper or scissors: \n")
    player_2 = input('Player 2: Rock, paper or scissors: \n')

    if player_1 == player_2:
        print('Player 1: ', player_1)
        print('Player 2: ', player_2)
        print('Tie!')

    if player_1 == 'rock':
        if player_2 == 'paper':
            print('Player 1: ',player_1)
            print('Player 2: ', player_2)
            print('Player 2 wins!')
        if player_2 == 'scissors':
            print('Player 1: ', player_1)
            print('Player 2: ',player_2)
            print('Player 1 wins!')
    if player_1 == 'paper':
        if player_2 == 'rock':
            print('Player 1: ', player_1)
            print('Player 2: ', player_2)
            print('Player 1 wins')
        if player_2 == 'scissors':
            print('Player 1: ', player_1)
            print('Player 2: ', player_2)
            print('Player 2 wins!')
    if player_1 == 'scissors':
        if player_2 == 'rock':
            print('Player 1: ', player_1)
            print('Player 2: ', player_2)
            print('Player 2 wins!')
        if player_2 == 'paper':
            print('Player 1: ', player_1)
            print('Player 2: ', player_2)
            print('Player 1 wins!')
    play_again = input('Play again? (YES/NO): ').lower()
    if play_again != "yes":
        break
print('END')

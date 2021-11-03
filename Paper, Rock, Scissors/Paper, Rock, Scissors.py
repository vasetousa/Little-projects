import random

def Play():

    user = input("'r' for rock, 'p' for paper, 's' for scissors, (e) for ending the game: ")
    if user == 'e':
        print("Game is over!")
        return 'exit'
    pc = random.choice(['r', 'p', 's'])
    print(f'- The computer chose {mapper(pc)},')

    if user == pc:
        print(f'- You chose {mapper(user)}')
        print('Its a tie!')
        return 'tie'

    if is_win(user, pc):
        print(f'- You chose {mapper(user)} - wisely and you won!')
        return 'win'
    print(f'- You chose {mapper(user)} - poorly and you lost!')
    return 'loss'


def is_win(player, machine):
    # return True if player wins
    # 'p' > 'r', 'r' > 's', 's' > 'p'
    if (player == 'r' and machine == 's') or (player == 'p' and machine == 'r') or (player == 's' and machine == 'p'):
        return True


def mapper(pc):
    mapper_map = {'s': 'Scissors', 'p': "Paper", 'r': 'Rock'}
    return mapper_map[pc]



wins = 0
losses = 0
ties = 0
while True:
    result = Play()
    if result == 'exit':
        print(f'You have {wins} wins, {losses} losses and {ties} ties!')
        break
    elif result == 'tie':
        ties += 1
    elif result == 'win':
        wins += 1
    elif result == 'loss':
        losses += 1
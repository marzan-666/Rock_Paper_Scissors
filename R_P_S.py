import random

def play():
    user = input("What's Your choice? 'r' for Rock, 'p' for Paper, 's' for Scissor\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user,computer):
        return 'You Won...!!!'

    return 'You Lost...!!'

def is_win(player, opponent):
    # return true if player wins
    # r>s , p>r , s>p

    if(player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent =='p'):
        return True


print(play())


import random

options = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
inverted_options = {v: k for k, v in options.items()}

def get_user_choice():
    user_input = input('Input Rock, Paper, or Scissors: ')
    if user_input not in ['Rock', 'Paper', 'Scissors']:
        print('Not a valid option')
        return get_user_choice()  
    else:
        user_input = options[user_input]
        return user_input

def determine_winner(user_num, opp_num):
    if user_num == opp_num:
        return 'Draw!'
    elif (user_num - opp_num) % 3 == 1:
        return f'You win!, the computer chose {inverted_options[opp_num]}'
    else:
        return f'You Lost!, the computer chose {inverted_options[opp_num]}'

def play_game():
    user_num = get_user_choice()
    opp_num = random.randint(1, 3)
    print(determine_winner(user_num, opp_num))

def play_again():
    user_input = input('Play Again? (Yes/No): ')
    if user_input == 'Yes':
        play_game()
        play_again()
    elif user_input == 'No':
        print("Thanks for playing!")
    else:
        print('Not a valid option')
        play_again()

play_game()  
play_again()
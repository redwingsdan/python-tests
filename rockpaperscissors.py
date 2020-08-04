from random import randint

def compare_selections(choices, choice_names, player_selection, ai_selection, total_wins, total_losses):
    player_index = choices.index(player_selection)
    ai_index = choices.index(ai_selection)
    is_player_win = (player_index > ai_index or (player_index == 0 and ai_index == 2)) and not (player_index == 2 and ai_index == 0)
    if is_player_win:
        print('You win! ' + choice_names[player_index] + ' beats ' + choice_names[ai_index])
    else:
        print('You lose! ' + choice_names[ai_index] + ' beats ' + choice_names[player_index])
    return is_player_win

def start_rock_paper_scissors_game():

    choices = ['r', 'p', 's']
    
    choice_names = ['Rock', 'Paper', 'Scissors']

    ai_selection = choices[randint(0,2)]

    player_selection = None
    
    total_wins = 0
    total_losses = 0

    while player_selection == None:
        player_selection = input("Rock, Paper, Scissors? ").lower()
        if player_selection == ai_selection:
            player_index = choices.index(player_selection)
            print('Both played ' + choice_names[player_index])
        elif player_selection in choices:
            is_win = compare_selections(choices, choice_names, player_selection, ai_selection, total_wins, total_losses)
            if is_win:
                total_wins += 1
            else:
                total_losses += 1
        else:
            print('Invalid choice, try again')
            
        print('Current Record: Wins = ' + str(total_wins) + ' Losses = ' + str(total_losses))
        player_selection = None
        ai_selection = choices[randint(0,2)]
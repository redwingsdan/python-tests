import numbergame
import rockpaperscissors
import passwordgenerator
import diceroll
import ciphers

selection = input("Select Program:\n" +
"1. Number Guessing\n" +
"2. Rock, Paper, Scissors\n" + 
"3. Password Generator\n" + 
"4. Dice Rolling\n" + 
"5. Ciphers\n" + 
"")
if selection == str(1):
    numbergame.start_number_game()
elif selection == str(2):
    rockpaperscissors.start_rock_paper_scissors_game()
elif selection == str(3):
    passwordgenerator.start_password_generation(input('Password Length: '))
elif selection == str(4):
    diceroll.start_dice_roll()
elif selection == str(5):
    ciphers.convert_cipher()
else:
    print('Invalid input')
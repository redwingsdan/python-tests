import random

def shuffle(string):
    tempPass = list(string)
    random.shuffle(tempPass)
    return ''.join(tempPass)
   
def generate_char():
    number = random.randint(0,3)
    if number == 0:
        return chr(random.randint(65,90)) #uppercase
    elif number == 1:
        return chr(random.randint(97,122)) #lowercase
    elif number == 2:
        return chr(random.randint(48,57)) #digit
    else:
        return chr(random.randint(33,64)) #punctuation

def start_password_generation(total_characters):
    password = ''
    if not total_characters.isdigit():
        total_characters = 8
    for num in range(int(total_characters)):
        password += generate_char()
    password = shuffle(password)
    print('Generated password is: ' + password)
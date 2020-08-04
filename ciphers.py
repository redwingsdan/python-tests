
def convert_cipher():
    type = input('What type of cipher? ')
    if type == 'b':
        convert_binary_cipher()
    elif type == 'u':
        convert_unicode_cipher()
    else:
        print('Cipher type not supported')
        
def convert_binary_cipher():
    file_content = open('cipher1.txt', 'r')
    result_text = ''
    ascii_value = 0
    multVal = 128
    while 1:
        binary_character = file_content.read(1)
        if not binary_character:
            break
        ascii_value += int(binary_character) * int(multVal)
        if multVal == 1:
            result_text += chr(ascii_value)
            multVal = 128
            ascii_value = 0
        else:
            multVal /= 2
    print('Decoded Text: ' + result_text)
    file_content.close() 

def convert_unicode_cipher():
    file_content = open('cipher2.txt', 'r')
    result_text = file_content.read().encode('utf-8').decode('unicode-escape')
    print('Decoded Text: ' + result_text)
    file_content.close() 
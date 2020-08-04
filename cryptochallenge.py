import codecs
from binascii import hexlify, unhexlify

class InvalidMessageException(Exception):
    pass

#read in a file name and return the contents as a string
def read_file_data(file_name):
    file = open(file_name, 'r')
    return file.read()
#decode the hex string data into bytes (equivalent to unhexlify)
def convert_hex_str_to_bytes(hex_str):
    return codecs.decode(hex_str, 'hex')
#decode the hex data, then encode it into the base64 format, and then decode into a string
def hex_to_base_64(hex_data):
    return codecs.encode(convert_hex_str_to_bytes(hex_data), 'base64').decode()
#iterate through each character in the 2 byte arrays and xor them with each other
def xor_bytes(input_bytes1, input_bytes2):
    return bytes([byte1 ^ byte2 for (byte1, byte2) in zip(input_bytes1, input_bytes2)])
#return the matched xor data for a given encrypted hex value
def find_best_xor_match(data_hex):
    best_match = None
    ascii_text_chars = list(range(97, 122)) + [32] #determine a list of ascii characters to match
    #iterate through all 255 ascii characters for the encrpytion
    for i in range(1,255):
        xor_key = bytes([i]) #create a key from the character
        xor_key_str = xor_key * len(data_hex) #match the key length with the hex text
        xor_byte_data = xor_bytes(data_hex, xor_key_str) #xor the key with the hex text
        number_letters = sum([x in ascii_text_chars for x in xor_byte_data]) #score the resulting data by totaling the matching ascii characters (more ascii characters means likely a more readable string of text)
        #Use the best scored data for the guess
        if best_match == None or number_letters > best_match['number_letters']:
            best_match = {'message': xor_byte_data, 'number_letters': number_letters, 'key': xor_key}
    #Ensure the best answer is at least 70% readable, otherwise throw an exception
    if best_match['number_letters'] > 0.7*len(data_hex):
        return best_match
    else:
        raise InvalidMessageException('Best candidate message is: %s' % best_match['message'])
 
def challenge_1():
    file_data = read_file_data('hextext.txt')
    base_64_data = hex_to_base_64(file_data)
    print(base_64_data)
  
def challenge_2():
    file_data_1 = read_file_data('hextext2a.txt')
    file_data_2 = read_file_data('hextext2b.txt')
    data_1_hex = convert_hex_str_to_bytes(file_data_1)
    data_2_hex = convert_hex_str_to_bytes(file_data_2)
    xor_byte_data = xor_bytes(data_1_hex, data_2_hex)
    print(xor_byte_data.hex())
    
def challenge_3():
    file_data = read_file_data('hextext3.txt')
    data_hex = convert_hex_str_to_bytes(file_data)
    best_match = find_best_xor_match(data_hex)
    print('message: ' + str(best_match['message']))
    print('letters: ' + str(best_match['number_letters']))
    print('key: ' +  str(best_match['key']))
    
def challenge_4():
    data_list = []
    #Iterate through each line of a file and convert the values from hex and add them to the list
    with open('hextext4.txt') as file_content:
        for line in file_content:
            data_list.append(convert_hex_str_to_bytes(line.strip()))
    possible_matches = list()
    #Iterate through each data line and try to find a valid xor match
    #Non-valid matches will throw an exception (since they weren't encrypted)
    for (line_number, text) in enumerate(data_list):
        try:
            best_match_message = find_best_xor_match(text)['message']
        except InvalidMessageException:
            pass
        else:
            possible_matches.append({
                'line_number': line_number,
                'original_text': text,
                'message': best_match_message
            })
    if len(possible_matches) > 1:
        print("Error: more than one match")
    else:
        #Print the object formatted as key: value
        for (key, value) in possible_matches[0].items():
            print(f'{key}: {value}')

def challenge_5():
    file_data = read_file_data('hextext5.txt')
    #Convert file data and key to bytes
    byte_data = bytes(file_data, 'utf8')
    xor_key =  bytes('ICE', 'utf8')
    #get the xor to match at least the length of the message
    xor_key_str = xor_key*(len(byte_data)//len(xor_key) + 1) #message length / key length without remainder + 1 
    xor_byte_data = xor_bytes(byte_data, xor_key_str) #xor the key with the hex text
    print(xor_byte_data.hex())
    
challenge_5()
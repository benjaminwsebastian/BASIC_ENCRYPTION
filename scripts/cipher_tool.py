#!/bin/python
import json, argparse, sys

###########
## INPUT ##
###########

def get_args():
    parser = argparse.ArgumentParser(description="create data of degree n", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--c", type = str, required = True, help = "cipher file")
    parser.add_argument("--e", type = str, required = True, help = "english list file")
    parser.add_argument("--s", type = str, required = True, help = "symbol list file")
    parser.add_argument("--m", type = str, required = True, help = "message file")
    parser.add_argument("--t", type = str, required = True, help = "type: Enter either encrypt or decrypt")
    
    args = parser.parse_args()
    if args.t not in ["encrypt", "decrypt"]:
        print("Enter valid type: encrypt or decrypt")
        sys.exit()
    
    return args

def read_file_by_line(file_name):
    content = []
    for line in open(file_name, 'r'):
        content.append(line.strip().split(" "))
    return content

#################
## SUBROUTINES ##
#################

def process(mode, cipher_dict, message):
    global SPACEBAR
    new_message = []
    for line in message:
        new_line = []
        if mode == 'encrypt':
            if len(line) > 1:
                for word in line:
                    new_line.append(cipher_dict[word.lower()])
                    new_line.append(cipher_dict[SPACEBAR])
            else:
                newline.append(cipher_dict[word[0].lower()])
        else:
            line = line[0]
            n = 6 # length of each word - this can be easily changed depending on how you create the cipher in create_cipher.py
            line = [line[i:i+n] for i in range(0, len(line), n)] # split the line every 6 characters
            SPACEBAR = list(cipher_dict.keys())[list(cipher_dict.values()).index(SPACEBAR)] # get the spacebar symbol
            line = list(filter(lambda word: word != SPACEBAR, line))

            # decrypt each word in the line
            for word in line:
                new_line.append(cipher_dict[word])
                new_line.append(" ")
        new_message.append(new_line)
    return new_message
                    
##########
## MAIN ##
##########

# get CL arguments
args = get_args()
cipher_file = args.c
english_file = args.e
symbol_file = args.s
message_file = args.m
mode = args.t

SPACEBAR = "spacebar"

# read in files
cipher = {}
with open(cipher_file, 'r') as IN:
    cipher = json.load(IN)

english_words = read_file_by_line(english_file)
symbols = read_file_by_line(symbol_file)
message = read_file_by_line(message_file)


# determine direction based on mode
from_to_dict = {'encrypt' : { "from" : english_words,
                              "to" : symbols},

                'decrypt' : { "from" : symbols,
                              "to" : english_words}
                }

# create the cipher_dict with the cipher and lists
cipher_dict = {}
for pair in cipher[mode]:
    value1 = from_to_dict[mode]["from"][int(pair)][0]
    value2 = from_to_dict[mode]["to"][cipher[mode][pair]][0]
    cipher_dict[value1] = value2

# encrypt or decrypt (depending on the mode)
message = process(mode, cipher_dict, message)

# overwrite the message file with the decrypted file
with open(message_file, 'w') as OUT:
    for line in message:
        OUT.write("".join(line)+"\n")

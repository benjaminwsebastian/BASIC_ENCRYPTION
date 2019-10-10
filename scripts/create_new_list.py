#!/bin/python3
import itertools

# define the characters I want to use
char_map = {'a' : chr(741),
            'b' : chr(742),
            'c' : chr(743),
            'd' : chr(744),
            'e' : chr(745),
            'f' : chr(746),
            'g' : chr(747)
            }

words = []
## create permutations with replacement
for i,p in enumerate(itertools.product('abcdef', repeat = 6)):
    if i == 20000: break
    words.append("".join(p))

# print the new "word" list
out_file = "20k_not_english.txt"
with open(out_file, 'w') as OUT:
    for word in words:
        # map the list of letters to the characters defined by the char_map
        mapped_word = [char_map[letter] for letter in word]
        OUT.write("".join(mapped_word)+"\n")

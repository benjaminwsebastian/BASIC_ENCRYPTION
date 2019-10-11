### Basic encryption

This project is something I did in a little over 2 hours. It is the implementation of an idea I had the night before as I fell asleep.

Basically, this tool encrypts messages using a cipher. However, instead of mapping letters to letters (such as A->J, J->K, ...) I wanted to map a set of words into a set of symbols. I also wanted the encryption to look uniform and indistict.

To create the set of symbols I first had to choose a set of words. Initially I thought that the 1000 most used words would suffice, but they don't include a lot of the popular conjugations. So then I thought maybe the first 5000 most used words would work, but I had the same problem. So I settled for the first 20000 words and haven't had an issue yet.

Okay so I have a set of 20000 words, now I need to create a set of 20000 symbols. I decided that I was going to make symbols by combining weird unicode characters in short strings. I arbitrarily wanted the length of the symbols to be 6 so to minimize the number of unicode characters needed to have 20000 unique permutations of length 6 I needed to minimize n^r, where r is the length of the permutation (r=6) and n is the number of unicode characters (just permutation with replacement). It turns out that this n is 6 (with ~26000 extra unique symbols of length 6).

Next I picked out the characters I wanted to use (˥ ˩ ˧ ˦ ˧˨ ˨ ˩˨) and made the symbol list (/scripts/create_new_list.py - prints out the first n permutations with replacement of length l, chosen from of a set of k symbols). Then I created the cipher  (/scripts/create_cipher.py) which creates two lists of intergers, ranging from 0 to 1999 (because zero-based), shuffles the lists, pairs them together as a dictionary like so: dict[list1[i]] = list2[i], then dumps the dictionary into a json file.

Finally, once I had a cipher and two lists of 20000 words I could create an encryption/decryption tool (/scripts/cipher_tool.py). This tool takes in the two lists of words, the cipher, a message file, and whether to encrypt or decrypt.

#### Gist of cipher_tool.py
##### **Case 1: Encryption**
**Setup:** The first step after reading in the files is to create a cipher_dict. The cipher_dict is a dictionary that takes in English words as a keys and returns symbols. The cipher.json file we read in determines which words get paired with which symbols. Combining all these word:symbol pairs gives us the cipher_dict.
**Process:** Now we can simply loop through the message and print out whatever cipher_dict[current_word] gives us, making sure to put cipher_dict[SPACEBAR] inbetween each word.

##### **Case 2: Decryption**
**Setup:** The first step after reading in the files is to create a cipher_dict. This cipher_dict is, predictably, the opposite of the encrypting cipher_dict. It takes in a symbol and outputs an English word. The cipher.json file we read in determines which symbols get paired with which words. Combining all these symbol:word pairs gives us the cipher_dict.
**Process:** Decrypting is a little more complicated than encrypting. First-of-all, each line is a long continuous string of characters so we don't know where words stop or start -- just kidding we do: each word is 6 characters long -- After partitioning each line at every 6 characters we can filter out the spacebar symbols, then print out the message using the cipher_dict, making sure to put " " inbetween each word.

##### Example:

    $ cat message.txt
    Hi this is a basic encryption tool that I made this morning .
    $ python3 scripts/cipher_tool.py --c cipher.json --e 20k_english.txt --s 20k_symbols.txt --m message.txt --t encrypt
    $ cat message.txt
    ˥˩˧˥˩˦˧˨˥˨˥˩˦˧˨˨˧˨˧˨˥˨˥˩˦˨˩˨˦˨˧˨˥˨˥˩˥˩˥˪˥˩˧˨˥˨˥˩˦˨˧˥˩˦˧˨˥˨˥˩˦˦˩˪˪˨˧˨˥˨˥˩˥˨˦˨˪˧˧˨˥˨˥˩˦˥˪˨˥˩˧˨˥˨˥˩˦˩˧˧˪˨˧˨˥˨˥˩˥˨˧˪˪˧˧˨˥˨˥˩˧˥˩˥˨˩˧˨˥˨˥˩˦˧˨˨˧˨˧˨˥˨˥˩˧˨˦˨˥˧˧˨˥˨˥˩˧˧˥˦˪˨˧˨˥˨˥˩
    $ python3 scripts/cipher_tool.py --c cipher.json --e 20k_english.txt --s 20k_symbols.txt --m message.txt --t decrypt
    $ cat message.txt
    hi this is a basic encryption tool that i made to this morning .

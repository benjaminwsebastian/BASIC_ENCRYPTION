### Basic encryption

This project is something I did in a little over 2 hours. The night before I came up with the idea and fell asleep thinking about it.

Basically, this encrypts messages using a cipher. However, instead of mapping letters to letters (such as A->J, J->K, ...) I want to map words into a set of symbols. I also wanted the encryption to look uniform and indistict.

To create the set of symbols I had to first choose my set of words. Initially I thought that the 1000 most used words would suffice, but they don't include a lot of the popular conjugations. So then I thought maybe the first 5000 most used words would work, but I had the same problem. So I settled for the first 20000 words and haven't had an issue yet.

Okay so I have a set of 20000 words, now I need to create a set of 20000 symbols. I decided that I was going to make symbols by combining weird unicode characters in short strings. I arbitrarily wanted the length of the symbols to be 6 so to minimize the number of unicode characters needed to have 20000 unique permutations of length 6 I just need to minimize n^r, where r is the length of the permutation and n is the number of unicode characters (just permutation with replacement). It turns out this n is 6 (with ~26000 extra unique symbols of length 6).

To be continued when I wake up tomorrow...

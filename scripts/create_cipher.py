#!/bin/python3
import random, json

list1 = list(range(0, 20000))
list2 = list(range(0, 20000))

random.shuffle(list1)
random.shuffle(list2)

encrypt_dict = dict(zip(iter(list1), list2))
decrypt_dict = {v: k for k, v in encrypt_dict.items()}
cipher = {"encrypt" : encrypt_dict,
          "decrypt" : decrypt_dict
          }

out_file = "cipher.json"
with open(out_file, 'w') as OUT:
    json.dump(cipher, OUT)

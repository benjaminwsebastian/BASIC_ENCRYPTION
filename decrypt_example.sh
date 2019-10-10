#!/bin/bash

echo "make sure that you ran 'encrypt_example.sh' first"
python3 scripts/cipher_tool.py --c cipher.json --e 20k_english.txt --s 20k_symbols.txt --m message.txt --t decrypt

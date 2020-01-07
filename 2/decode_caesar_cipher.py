import sys

val = input('Enter caesar cipher: ')
key = 0

while key < 26:
    dec = ""
    for char in val:
        ord_char = ord(char)
        chr_num  = (((int(ord_char) - 97) + int(key)) % 26) + 97
        chr_char = chr(chr_num)
        dec = dec + chr_char
    print(dec)
    key = key + 1
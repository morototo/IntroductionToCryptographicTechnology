import sys

val = input('Enter caesar value: ')
key = input('Enter key value: ')

if not key.isdecimal():
    print('Key have to be integer.')
    sys.exit()

enc = ""

for char in val:
    ord_char = ord(char)
    chr_num  = (((int(ord_char) - 97) + int(key)) % 26) + 97
    chr_char = chr(chr_num)
    enc = enc + chr_char

print('Caesar cipher is:{}'.format(enc))
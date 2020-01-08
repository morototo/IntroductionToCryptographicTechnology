import random

def encrypt(text, original, encode):
    result = ''
    for letter in text:
        index = original.index(letter)
        result += encode[index]
    return result

plain = 'abcdefghijklmnopqrstuvwxyz' 
key   = ''.join(random.sample(plain, len(plain)))
plain_text = input('Enter your text: ')

cipher_text = encrypt(plain_text.lower(), plain, key)
print('Cipher text={} key={}'.format(cipher_text, key))
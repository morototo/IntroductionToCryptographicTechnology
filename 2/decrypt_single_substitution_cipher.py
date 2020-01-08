def decrypt(text, original, encode):
    result = ''
    for letter in text:
        index = original.index(letter)
        result += encode[index]
    return result

plain = 'abcdefghijklmnopqrstuvwxyz' 
encrypt_text = input('Enter your encrypt text: ')
key = input('Enter your key: ')

decrypt_text = decrypt(encrypt_text.lower(), key, plain)
print('Decrypt text={}'.format(decrypt_text))
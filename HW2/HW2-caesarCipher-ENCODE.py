#!/usr/bin/env python3

def encode(plaintext, offset):
    if (offset == ''):
        print('[\] ALERT: No offset entered, defaulting to 0.')
        offset = 0
    elif (not (offset.isnumeric())):
        if (offset.isalpha()):
            offset = offset.lower()
            offset = ord(offset) - ord('a')
            print(
                '[\] ALERT: Alphabetical offset entered. ' + 
                'Treating as if a=0 -> z=25.' +
                f'\n           Offset is equal to {offset}'
            )
        else:
            offset = ord(offset)
            print(
                '[\] ALERT: Non-integer, non-alphabetical offset entered. ' +
                f'Interpreting as ASCII value {offset}.'
            )

    ciphertext = ''

    for char in plaintext.lower():

        if (ord('a') <= ord(char) <= ord('z')):
            char_val = ord(char) + int(offset)

            while (char_val > ord('z')):
                char_val -= 26

            char = chr(char_val)

        ciphertext += char

    return ciphertext

print('Welcome!')
user_input = input("Please enter some text you'd like to encode: ")
user_offset = input("Please enter the offset: ")

print('ENCODING...')
ciphertext = encode(user_input, user_offset)
print('\n' + ciphertext)



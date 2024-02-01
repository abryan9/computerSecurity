#!/user/bin/env python3

import os

def decode(ciphertext):
    filepath = (__file__).removesuffix('HW2-caesarCipher-DECODE.py')
    file = open(filepath + 'decodeOutput.txt', 'w')
    outputList = []

    for offset in range(26):
        plaintext = ''

        for char in ciphertext.lower():
            if char.isalpha():
                char = chr(ord(char) + offset)
                while ord(char) > ord('z'):
                    char = chr(ord(char) - 26)
            
            plaintext += char

        if (not file.closed):
            file.write(plaintext + '\n\n')
        outputList.append(plaintext)

    return outputList


def analyze(bruteForceList):
    for string in bruteForceList:
        pass


outputList = decode(input('Please enter a ciphertext to decode: '))

print(
    '[+] Decoded cipehertexts uploaded to decodeOutput.txt\n' +
    '    Performing Frequency Analysis...'
    )

analyze(outputList)


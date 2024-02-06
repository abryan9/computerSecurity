#!/user/bin/env python3

import os

def decode(ciphertext):
    # Open a file and write all 26 offsets.
    filepath = (__file__).removesuffix('HW2-caesarCipher-DECODE.py') # Automates placing the file in the same directory as the python file.
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

    file.close()

    return outputList # Chose to create a list parallel to file writing because I would have to do so later regardless of if i initially read in from a file.


def sort(inputDict, iterations=5):
    # Takes a dictionary and returns a number of key-value pairs sorted by the lowest value key.
    outputDict = {}
    sortedKeys = sorted(inputDict.keys())
    for i in range(iterations):
        outputDict.update({sortedKeys[i]: inputDict[sortedKeys[i]]})

    return outputDict


def analyze(bruteForceList):
    freqDict = { # Initialize somewhere to store our input data's character frequency.
        'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 
        'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 
        's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0,
    }
    freqValsDict = { # Distribution of letters in the english language as a decimal.
        'a':0.0817, 'b':0.0129, 'c':0.0278, 'd':0.0425, 'e':0.1270, 
        'f':0.0223, 'g':0.0202, 'h':0.0609, 'i':0.0697, 'j':0.0015, 
        'k':0.0077, 'l':0.0403, 'm':0.0241, 'n':0.0675, 'o':0.0751, 
        'p':0.0193, 'q':0.0010, 'r':0.0599, 's':0.0633, 't':0.0906, 
        'u':0.0276, 'v':0.0098, 'w':0.0236, 'x':0.0015, 'y':0.0197, 'z':0.0007,
    }
    hammingWeights = []

    for string in bruteForceList:
        hammingDistance = 0 # I'm aware this is only a loose fit for Hamming Weights, but the name is good enough to follow along.
        for char in string:
            if char.isalpha():
                freqDict[char] += 1

        for letter in freqDict.keys():
            freqDict[letter] /= float(len(string))
            hammingDistance += abs(freqDict[letter] - freqValsDict[letter]) # This value represents the sum distance from English's character distribution.

        hammingWeights.append(hammingDistance) # List of all hamming weights that along with the bruteForceList create a key-value pair by referencing the same index across the two.

    if (len(bruteForceList) == len(hammingWeights)):
        print('[+] Hamming weights calculated...\n')

        stringsAndWeights = {} # Initialization for a dictionary with keys being the hamming distance of a given string from our brute force decoding.

        for i in range(len(hammingWeights)):
            if hammingWeights[i] in stringsAndWeights.keys(): # in the event that two strings create the same hamming distance (very unlikely),
                                                              # We need to store a list under the same key instead of a string.
                update = list(stringsAndWeights[hammingWeights[i]]).append(bruteForceList[i])
                stringsAndWeights.update({hammingWeights[i]: update})

            else:
                stringsAndWeights.update({hammingWeights[i]: bruteForceList[i]})

        topFive = sort(stringsAndWeights, 5)

        return topFive


outputList = decode(input('Please enter a ciphertext to decode: '))

print(
    '[+] Decoded cipehertexts uploaded to decodeOutput.txt\n' +
    '    Performing Frequency Analysis...'
    )

topFive = analyze(outputList)

for i in range(len(topFive.keys())):
    print(
        f'{i+1}: With a deviation of {list(topFive.keys())[i]} \n' +
        topFive[list(topFive.keys())[i]] + '\n'
    )
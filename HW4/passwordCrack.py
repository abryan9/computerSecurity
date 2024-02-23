#! user/bin/env python3

import hashlib

ABS_PATH = __file__.removesuffix('passwordCrack.py')
passwords = []

with open(ABS_PATH + 'abryan9-shapass') as sha:
    SHA_HASH = sha.readline().strip()

with open(ABS_PATH + 'abridged_rockyou.txt') as rockyou:
    for password in rockyou:
        passwords.append(password.removesuffix('\n'))

for attempt in passwords:
    passwordGuess = hashlib.sha256(attempt.encode("utf-8")).hexdigest()
    # print(type(passwordGuess))

    if passwordGuess == SHA_HASH:
        print(f"[+] PASSWORD CRACKED: {attempt}")
        quit()

print("[-] ERROR: Password not found in abridged rockyou")

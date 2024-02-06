# Homework 2 - Chapter 2 Part 1 #
### Alex Bryan
### Due Feb 4

---

## Problem 1: What are the two principal requirements for the secure use of symmetric encryption? ##
The two principal requirements for a secure symmetric encryption algorithm are a robust algorithm and secure key transmission between the sender and receiver.

---

## Problem 2: What properties must a hash function have to be useful for message authentication? ##
A hash function must be able to verify the authenticity of the data's source as well as check that the content has not been altered.

---

## Problem 3: Suppose someone suggests the following way to confirm that the two of you are both in possession of the same secret key. You create a random bit string the length of the key, XOR it with the key, and send the result over the channel. Your partner XORs the incoming block with the key (hopefully the same as yours) and sends it back. You check, and if what you receive is your original random string, you have verified that your partner has the same secret key, yet neither of you transmitted the key. Is there a flaw in this, and if so what is it? ##
There is a flaw in this method. If a passive attacker can moniter the data stream in both directions and XOR the two streams, the key will be the result of that operation.

---

## Problem 4: Suppose H(m) is a collision resistant hash function that maps a message of arbitrary bit length into an n-bit hash value. Is it true that, for all messages x,x' where x != x' we have H(x) != H(x')? Explain your answer. ##
No. If the length of the message is larger than n, then there is guaranteed to be a collision. As a result, there would always be at least one instance in this environment where H(x) == H(x').

---

## Problem 5: Caesar Ciphers ##
Caeser Cipher encryption and decription files are submitted as "HW2-caesarCipher-DECODE.py" and "HW2-caesarCipher-ENCODE.py".
import string
import math

alf = string.ascii_lowercase

def encode_caesar(plain, key):
    plain = plain.lower()
    enc = ''
    for letter in plain:
        index = alf.find(letter)
        if index == -1:
            enc += letter
            continue
        index += key
        if index > len(alf) - 1:
            index -= len(alf)
        enc += alf[index]
    return enc

def decode_caesar(plain, key):
    plain = plain.lower()
    dec = ''
    for letter in plain:
        index = alf.find(letter)
        if index == -1:
            dec += letter
            continue
        index -= key
        if index > len(alf) - 1:
            index += len(alf)
        dec += alf[index]
    return dec

def encode_vigenere(plain, key):
    plain = plain.lower()
    if len(plain) > len(key):
        mult = math.ceil(len(plain) / len(key))
        key *= mult
    enc = ''
    for i in range(0, len(plain)):
        caesar_key = alf.find(key[i])
        if caesar_key > len(alf) - 1:
            caesar_key -= len(alf)
        enc += encode_caesar(plain[i], caesar_key)
    return enc

def decode_vigenere(plain, key):
    plain = plain.lower()
    if len(plain) > len(key):
        mult = math.ceil(len(plain) / len(key))
        key *= mult
    dec = ''
    for i in range(0, len(plain)):
        caesar_key = alf.find(key[i])
        if caesar_key > len(alf) - 1:
            caesar_key -= len(alf)
        dec += decode_caesar(plain[i], caesar_key)
    return dec


e = encode_vigenere('teste', 'key')
print(e)
d = decode_vigenere(e, 'key')
print(d)
import random
# import hashlib

capital_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
        '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', '"', "'", ',', '.', '?',
        '/']


def password():
    i = 0
    passWD = []
    while i < 3:
        num = numbers[random.randint(0, 9)]
        calpha = capital_alpha[random.randint(0, 25)]
        salpha = small_alpha[random.randint(0, 25)]
        sym = symbols[random.randint(0, 28)]
        passwd = num + calpha + salpha + sym
        i += 1
        passWD.append(passwd)
    print(passWD[0] + passWD[1] + passWD[2])
    # hash_object = hashlib.md5(passWD.encode())
    # print(hash_object.hexdiget())


password()


def encode(x):
    pass


def pin(z):
    pass


def spend(y):
    pass



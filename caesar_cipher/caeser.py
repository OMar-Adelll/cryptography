SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(message, key):
    res = ""
    si = len(message)
    for i in range(0, si):
        if message[i] in SYMBOLS:
            idx = SYMBOLS.find(message[i])
            res = res + SYMBOLS[(idx + key) % 26]
        else:
            res = res + message[i]

    return res


message = "HELLO WORLD"
key = 3
print("Encrypted text is: ", encrypt(message, key))  # KHOOR ZRUOG

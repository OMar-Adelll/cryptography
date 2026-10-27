SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 26


def encrypt(message, key):
    res = ""
    si = len(message)
    for i in range(0, si):
        if message[i] in SYMBOLS:
            idx = SYMBOLS.find(message[i])
            res = res + SYMBOLS[(idx + key) % MOD]
        else:
            res = res + message[i]

    return res


def decrypt(message, key):
    res = ""
    si = len(message)
    for i in range(0, si):
        if message[i] in SYMBOLS:
            idx = SYMBOLS.find(message[i])
            res = res + SYMBOLS[((idx - key) % MOD + MOD) % MOD]
        else:
            res = res + message[i]

    return res


ms = input("Enter Your Name: ")
ky = int(input("Enter The key: "))

encrypted = encrypt(ms, ky)
print("The Encrypted message is: ", encrypted)

# ms - OMAR ADEL YOUSSEF
# ky - 7
# res - VTHY HKLS FVBZZLM

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 26


def encrypt(message, key):
    res = ""
    si = len(message)
    for i in range(0, si):
        if message[i] in SYMBOLS:
            idx = SYMBOLS.find(message[i])
            res += SYMBOLS[(idx + key) % MOD]
        else:
            res += message[i]

    return res


def decrypt(message):
    res = [""] * 26
    si = len(message)
    for i in range(0, si):
        if message[i] in SYMBOLS:
            idx = SYMBOLS.find(message[i])

            for k in range(MOD):
                res[k] += SYMBOLS[(idx - k) % MOD]
        else:
            for k in range(MOD):
                res[k] += message[i]

    return res


ms = "WKLV LV IXQ"
dec = decrypt(ms)

for i in range(26):
    print("key = ", i, " | text : ", dec[i])

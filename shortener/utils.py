import random 

def encode_base62(length=6):
    BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ''
    for _ in range(length):
        code = code + ''.join(random.choice(BASE62))

    return code 

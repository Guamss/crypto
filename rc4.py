import base64

def encode(sh):
	return base64.b16encode(bytes(sh, 'latin')).upper()

def decode(sh):
    return base64.b16decode(sh, casefold=True).decode('latin')

def rc4_init(key):
    S = [i for i in range(256)]
    j = 0

    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]
    return S

def bytes_to_text(byteList):
    s = ''
    for byte in byteList:
          s += chr(byte)
    return s

def rc4_encrypt(key, input):
    key_stream = []
    key = rc4_init(key)
    j = i = 0
    for x in range(256):
        i = (i + 1) % 256
        j = (j + key[i]) % 256
        key[i], key[j] = key[j], key[i]
        key_stream.append(key[(key[i] + key[j]) % 256])
    ciphertext = ''
    i = 0
    for char in input:
        enc = chr(ord(char) ^ key_stream[i])
        ciphertext += enc
        i+=1
    ciphertext = encode(ciphertext)
    return bytes_to_text(ciphertext)

def rc4_decrypt(key, input):
     return decode(rc4_encrypt(key, decode(input)))


key = "Secret_key"
result = rc4_encrypt(key, "MonsterMasters")
print(f"Encrypted text with RC4 : {result}")
print(f"Genuine text : {rc4_decrypt(key, result)}\nwith the key : {key}")
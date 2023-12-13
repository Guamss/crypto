def vernam(key:list, message:list):
    """Applique le code Vernam sur un message avec la clé key

    Args:
        key (list[int]): Clé d'encryption
        message (list[int]): Message à encrypter

    Returns:
        (list[int]): Message encrypté avec la clé key
    """
    encrypted = [None]*len(message)
    for i in range(len(message)):
        encrypted[i] = key[i%(len(key))]^message[i]
    return encrypted

key = [1, 0, 1]
M = [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1]
M_ = vernam(key, M)
assert M == vernam(key, M_)
print(f"Code Vernam avec la clé {key} sur le message {M} : {M_}")
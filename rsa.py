from decomposition_nombre_premier import *
from algorithme_euclide import *

def rsa_encrypt(n, p, M, e):
    """Crypte un message encrypté avec le RSA

    Args:
        n (int): entier pour determiner la clé publique N
        p (int): entier pour determiner la clé publique N
        M (int): Message à crypter
        e (int): nombre premier avec phi(N), fais partie de la clé publique

    Raises:
        Exception: Si n et p ne sont pas premier entre eux

    Returns:
        (int): Message encrypté
    """
    if bezout(n, p)[0] != 1:
        raise Exception("n et p ne sont pas premier entre eux")
    N = n*p
    M_prime = exponentiation_modulaire(M, e, N)
    return M_prime

def rsa_decrypt(n, p, M_prime, e):
    """Déchiffre un message encrypté avec le RSA

    Args:
        n (int): entier pour determiner la clé publique N
        p (int): entier pour determiner la clé publique N
        M_prime (int): Message encrypté
        e (int): nombre premier avec phi(N), fais partie de la clé publique

    Raises:
        Exception: Si n et p ne sont pas premier entre eux

    Returns:
        (int): Message décrypté
    """
    if bezout(n, p)[0] != 1:
        raise Exception("n et p ne sont pas premier entre eux")
    N = n*p
    phi_N = phi(N)
    bezout_coef_v = bezout(phi_N, e)[2]
    d = bezout_coef_v % phi_N # Si le coef V est négatif, alors on prend le reste positif de celui-ci 
    M = exponentiation_modulaire(M_prime, d, N)
    return M
    
print(rsa_encrypt(101, 103, 10331, 7))
print(rsa_decrypt(101, 103, rsa_encrypt(101, 103, 10331, 7), 7))

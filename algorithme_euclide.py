def bezout(a, b):
    """Détermine les coefficients de bezout avec le PGCD sous forme (PGCD, U, V)

    Args:
        a (int): Entier
        b (int): Entier

    Returns:
        (tuple): les coefs de bezout et le PGCD sous forme (PGCD, U, V)
    """
    xa, ya, xb, yb = 1, 0, 0, 1
    while b != 0:
        q=a//b
        a, xa, ya, b, xb, yb = b, xb, yb, a-q*b, xa-q*xb, ya-q*yb
    if a < 0:
        return -a, -xa, -ya
    return a, xa, ya

def base10_to_bin(x):
    x = list(bin(x))[2:]
    for i in range(len(x)):
        x[i] = int(x[i])
    return x[::-1]

def exponentiation_modulaire(x, p, Zn):
    """Détermine le reste de la division euclidienne de x^p par Zn

    Args:
        x (int): Un entier
        p (int): L'entier à la puissance de x entier
        Zn (int): Modulo de l'opération

    Returns:
        (int): Reste de la division euclidienne
    """
    x = x % Zn
    p = base10_to_bin(p)
    result = []
    result_f = 1
    j = 1
    k = 0
    for i in range(len(p)):
        if p[i] == 1:
            temp = (x**j)%Zn
            result.append(temp)
            result_f*= result[k]
            k+=1
        j= j*2
    return result_f%Zn




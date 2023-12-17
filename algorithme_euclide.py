def bezout2(a :int, b :int):
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


def bezout(a :int, b :int):
    """Permet de renvoyer le coefficient V de l'identité de bezout

    Args:
        a (int): C'est le dividende dans l'algorithme d'Euclide étendu
        b (int): C'est le dviseur dans l'algorithme d'Euclide étendu

    Returns:
        (int): Le coeffcient V de l'identité de bezout
    """
    r = 0
    a_tab = []
    b_tab = []
    while r !=1:
        r = a % b
        a_tab.append(a)
        b_tab.append(b)
        b, a = r, b
    v = -(a//b)
    u = 1
    for n in range(len(a_tab)-1, -1, -1):
        v = (1-u*a_tab[n])//b_tab[n]
        u = v
    return v


def exponentiation_modulaire(x :int, p :int, Zn :int):
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
            temp = (x**j) % Zn
            result.append(temp)
            result_f*= result[k]
            k+=1
        j= j*2
    return result_f % Zn
def decomposition_primaire(n :int):
    """
    Fonction renvoyant un dictionnaire de la décomposition primaire de n 
    sous forme de {2 : 3, 5 : 3} pour 2³ x 5³
    Args:
        n (int): Nombre à décomposer

    Returns:
        (dict): Dictionnaire de la décomposition primaire de n
    """
    nbr_premiers = {}
    n_cpy = n
    for i in range(2, n):
        puissance = 0
        while n_cpy % i == 0:
            puissance += 1
            n_cpy = n_cpy//i
        if i not in nbr_premiers.keys() and puissance > 0:
            nbr_premiers[i] = puissance
    return nbr_premiers or {n : 1}

def PGCD(a :int, b :int):
    """Détermine le PGCD de deux entier a et b

    Args:
        a (int): Le dividende dans l'algorithme d'Euclide
        b (int): Le diviseur dans l'algorithme d'Euclide

    Returns:
        (int): Le PGCD de a et b
    """
    r = 1
    while r != 0:
        r = a%b
        b, a = r, b
    return a

def phi(n :int):
    """Applique l'indicatrice d'Euler à n

    Args:
        n (int): Entier naturel non nul

    Raises:
        Exception: Quand le paramètre de la fonction 
        n'est pas un entier naturel non nul

    Returns:
        (int): Le résultat de la fonction
    """
    if n <= 0:
        raise Exception("Veuillez saisir un entier naturel non nul!")
    decomposition = decomposition_primaire(n)
    result = 1
    for key in decomposition:
        actual_nbr = key**decomposition[key]-key**(decomposition[key]-1)
        result = result*actual_nbr
    return result
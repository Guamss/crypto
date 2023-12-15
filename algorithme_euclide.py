import decomposition_nombre_premier

def bezout(a, b):
    xa, ya, xb, yb = 1, 0, 0, 1
    while b != 0:
        q=a//b
        a, xa, ya, b, xb, yb = b, xb, yb, a-q*b, xa-q*xb, ya-q*yb
    if a < 0:
        return -a, -xa, -ya
    return a, xa, ya

# print(bezout(242, 51))
# V = 19 => (51*19)%242 = 1 => 19 = d car inverse de e
# (eV)%242 = 1 => (ed)%242 = 1
# print((51*19)%242)

def base10_to_bin(x):
    x = list(bin(x))[2:]
    for i in range(len(x)):
        x[i] = int(x[i])
    return x[::-1]

def exponentiation_modulaire(x, p, Zn):
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




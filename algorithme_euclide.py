def bezout(a, b):
    xa, ya, xb, yb = 1, 0, 0, 1
    while b != 0:
        q=a//b
        a, xa, ya, b, xb, yb = b, xb, yb, a-q*b, xa-q*xb, ya-q*yb
    if a < 0:
        return -a, -xa, -ya
    return a, xa, ya

print(bezout(368, -117))
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    result = 0
    for _ in range(b):
        result = add(result, a)
    return result

def div(a,b):
    result = 0
    temp = a
    while temp >= b:
        temp = sub(temp, b)
        result = add(result, 1)
    return result

def simple_interest(P, R, T):
    pr = mul(P, R)
    prt = mul(pr, T)
    si = div(prt, 100)
    return si
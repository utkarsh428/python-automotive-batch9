def add(a,b):
    return a + b #adddition

def sub(a,b):
    return a - b #subtraction

def mul(a,b):
    result = 0
    for _ in range(b):
        result = add(result, a)
    return result  #multiplication using add()

def div(a,b):
    result = 0
    temp = a
    while temp >= b:
        temp = sub(temp, b)
        result = add(result, 1)
    return result #division using sub()

#simple interest calculation
def simple_interest(P, R, T):
    pr = mul(P, R)
    prt = mul(pr, T)
    si = div(prt, 100)
    return si
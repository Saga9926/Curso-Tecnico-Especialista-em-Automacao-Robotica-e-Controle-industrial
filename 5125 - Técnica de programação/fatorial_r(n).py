"""

def fatorial (n):
    if n ==0:
        return 1
    else:
        return n * fatorial (n-1)
print (fatorial(5))

"""
"""
def mult_r (mult1,mult2):
    if mult2 ==0:
        return 0
    else:
        return mult1 + mult_r(mult1,mult2-1) 
print (mult_r(5,4))
"""
"""
def pot_r(b,e):
    if e==0:
        return 1
    else:
        return b*pot_r(b,e-1)
print (pot_r (5,4))

"""
"""
def soma_n_r (lim_i,lim_s):
    if soma_n_r == 1:
        return 1
    return lim_i + lim_s

print(soma_n_r(3,5))
"""
"""
def fib (n):
    if n ==0:
        return 0
    elif n== 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
"""

def caixa (c):
    if 2^(c-1)==1:
        print (f"mover 1 caixa de {origem} à {destino}")
    elif 2^(c-1)>1:
        print (f"mover 2 caixas de {origem} à {auxiliar} e depois para {guimarães}")
        


"""
exercicio 1
"""
"""
a = 5
print (a)
b = 7
print (b)
c = a + b
print (c)
"""

"""
num=int(input("Qual sua idade?: "))
if num >=18:
    print ("Maior de idade ")
else:
    print ("Menor de idade ")
"""
"Exercicio 4"
"""
peso=int(input("Introduza seu peso: (KG)"))
altura= float(input("Introduza sua altura: (cm)"))

IMC= float(peso / altura**2 )
print ("Seu IMC é: ", IMC)

if IMC < 18.5:
    print ("baixo peso")
elif IMC<=25:
    print ("peso adequado")
elif IMC<=30:
    print ("sobrepeso")
else:
    print("obesidade")
"""
"Exercicio 5"
"""
produto=1
num= int (input("Introduza um número: "))
while num>0:
    produto= produto*num
    num=num-1
    print (produto)
"""
"""
def factorial_f (n):
    produto=1
    for i in range (n,0,-1):
        produto *= i
        print (produto)
    return (produto)

n=int(input("Introduza um número inteiro: "))

fact=factorial_f(n)

print ("O de{fatorial(n)} é {produto}.", fact)
"""
"""
def factorial_w (n):
    produto=1
    while n>0:
        produto= produto*n
        n=n-1
        print (produto)
    return (produto)

n= int(input("Digite um número: "))
fact=factorial_w (n)
print ("O fatorial de {factorial_w} é {produto}.", fact)
"""
"""
Desafio 1
"""
"""
def soma_w(valor_minimo, valor_maximo):
    soma=0
    min= valor_minimo
    while min <= valor_maximo:
        soma += min
        min += 1
    return soma
"""
"""
def soma_f(valor_minimo, valor_maximo):
    soma=0
    for min in range (valor_minimo, valor_maximo+1,3):
        soma += min
    return (soma)

def mult_w (m,n):
    mult=0
    num=0
    while n>0:
       mult=mult+m
       n=n-1
    return (mult)
"""
"""
def mult_f (m,n):
    multi=0
    for i in range (1,n+1):
        multi= multi+m
    return multi
"""
"""
def pot (b,e):
    pot=1
    while e>0:
        pot *=b
        e -= 1
    return pot
    
"""
"""
def pot_f (b,e):
    pot=1
    for i in range (e):
        pot *=b
    return pot
"""
"""
km_percorridos = int(input(" Quantos km seu carro percorre?: " ))
gasto_medio = float(input(" Qual seu gasto médio de gasolina(litros/100km): "))
preço_combustivel = float(input(" Qual o valor da gasolina?: "))
combustivel_gasto = float (gasto_medio * km_percorridos) / 100
print ("Você gasta: ", combustivel_gasto)
custo_total = int(combustivel_gasto * preço_combustivel)
print ("Você gastará: (€)", custo_total)
 
"""

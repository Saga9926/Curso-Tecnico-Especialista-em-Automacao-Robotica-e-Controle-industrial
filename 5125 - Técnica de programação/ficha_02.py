# Ficha de revisão de conteudos;
"""
#exercício 1:
def par (n):
    if n % 2==0:
        print ("número é par!")
        return 1
    else:
        print ("número é impar!")
        return 0
print ( par(5))
"""
"""
#exercício 2:
def semaforo (c):
    if c == "vermelho":
        print (" Passagem proibida")
    elif c == "amarelo":
        print (" transição para vermelho")
    elif c == "verde":
        print (" passagem autorizada")
    else:
        print (" cor inválida")
print (semaforo("roxo"))
"""
"""
#exercício 3:
def fact_w():
    fatorial = 1
    num=int(input("Digite um número: "))
    while num > 1:
        fatorial= fatorial* num
        num= num- 1
        print (fatorial)
print (fact_w())
"""
"""
#exercício 4:
def fact_f ():
    produto=1
    num=int(input("digite um número: "))
    for i in range(1, num+1):
        produto*=i
    return produto
resultado=fact_f()
print ("fatorial é: ", resultado)
"""
"""
#exercício 5:
def fact_r (n):
   if n == 1 or n == 0:
    return 1
    print (" digite um valor válido.")
   else:
        return n * fact_r(n-1)
resultado = fact_r(6)
print ("o fatorial é: ", resultado)
"""
"""
#exercício 6:
def f_lista(lista):
    quantidade=0
    soma=0
    for numero in lista:
        quantidade +=1
        soma +=1
    media = soma / quantidade if quantidade > 0 else 0
    return quantidade, soma, lista
lista = [1,2,3,4,5,6,7,8,9]
quantidade,soma,media=f_lista(lista)
print("Número de elementos: ", quantidade)
print("Soma dos elementos: ", soma)
print("Média dos elementos: ",media)
"""
        

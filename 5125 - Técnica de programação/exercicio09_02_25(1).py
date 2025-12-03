"""
revisão de conhecimentos
"""
"""
def maior_menor (v1,v2):
    if v1 > v2:
        return (" O valor 1 é maior que o valor 2")
    elif v1 < v2:
        return (" O valor 2 é maior que o valor 1")
    else:
        return ("O valor 1 é igual ao valor 2")
"""
def soma (v1,v2):
    v3=v1+v2
    return v3
    print ("o resultado é: ")
        
def sub (v1,v2):
    v3=v1-v2
    v1 == float
    v2 == float
    if v1>v2:
        v3=v1-v2
        return v3
        print ("O resultado é: ")
    else :
        v3=v2-v1
        return v3
        print ("O resultado é: ")
"""
Operação para dar apenas numeros inteiros positivos!
"""
def mult (v1,v2):
    v3=v1*v2
    v3==float
    v1==float
    v2==float
    return v3
    print (" o resultado é: ")

""""
def validar_nome (n1):
    print (n1)
    if len(n1)<6:
        return 0, "o nome é invalido, possui menos de 6 caracteres."
    tem_apenas_letras=True
    tem_espaço=False
    for char in n1:
        if not char.isalpha() and char != " ":
            tem_apenas_letras=False
        if char == " ":
            tem_espaço=True
    if not tem_apenas_letras:
        return 0, f" o nome é invalido, só pode possuir letras."
    if not tem_espaço:
        return 0, f"o nome é inválido, não pode possuir espaço."

    return 1, f"o nome é valido"

"""

#char/chr() é usada para converter um código numérico (valor Unicode) de volta para o caractere correspondente a esse valor.
#ex: chr(valor) -> valor é um número inteiro que representa um código Unicode válido, retorna o caractere que corresponde ao código Unicode fornecido.
def validar_nome (nome):
    if any(chr.isdigit() for chr in (nome)):
        return "o nome deve conter apenas letras"
    if len (nome)<=2:
        return "o nome deve ter mais que 2 caractéres."
    tem_apenas_letras=True
    tem_espaço=False
    for chr in (nome):
        if not chr.isalpha() and chr != " ":
            tem_apenas_letras=False
        if chr.isalpha() and chr == " ":
            tem_espaço=False
        if not tem_apenas_letras:
            return "o nome é invalido, só pode ter letras."
        if not tem_espaço:
            return "o nome é invalido, não pode conter espaços."

        return ("Nome validado")
print (validar_nome("claudio roberto"))


def validar_email (email):
    if (email) != type(str):
        return "email precisa de caracteres e/ou numeros"
print (validar_email(cuppz.jp@gmail.com))

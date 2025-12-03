"""
#Validar email
def validar_email (email):
#deixamos a variavel a 0 (val=0), para termos uma condição. Se não condizer ao que queremos, ele retorna a 0.
    val=0
    if email [-17:]!="@formacao.iefp.pt":
       print ("email invalido")
       return val
#valida "user" (neste caso é só digitos, atrás do @)
    print (email.index("@"))
    print (email[:email.index("@")])
    if not email[:email.index("@")].isdigit():
        print ("caracteres invalidos")
        return val
#Se passar no teste. retorna=1
    print ("tudo ok")
    #validação positiva
    val=1
    return val
print (validar_email("76122joao@formacao.iefp.pt"))

#funcionando :)

#Validar telefone

def validar_telefone (telefone):
    val=0
    if not telefone len(telefone)==9:
        print ("comprimento invalido")
        return val
    if not telefone.isdigit():
        print ("deve apenas conter dígitos")
        return val
    print (telefone[0])
    if not (telefone[0]=="2" or telefone[0]=="9"):
        print ("primeiro digito inválido")
        return val
    print ("tudo ok")
    val=1
    return val
print(validar_telefone(

"""

def validar_ISBN(codigo):
    val=0
#determinar o tamanho exato que preciso para validar o valor, netes caso será um tamanho de 13 caractéres.
    if len(codigo) != 13:
        print ("codigo inválido. O código precisa de 13 dígitos.")
        return val
#determinar se ele só tem números
    if not codigo.isdigit():
        print ("codigo inválido. Por favor insira apenas números.")
        return val
#agora determinamos a soma
    soma=0
#para i(variavel) no range (13) ou (len(codigo)).
    for i in range(13):
#se a variavel for divisivel por 2 e der 0, ele vai soma-la e multiplicar por 1;
#ex : i=9 (9 não é divisivel por 2, por isso ele entrará na condição else), soma= 0+9*3
# i=2 (2 é divisivel por 2, por isso ele entra na condição if), soma= 0+2*1
#no final ele soma os dois resultados (27+2=29)
        if i % 2 == 0:
            soma = soma + int(codigo[i])*1
        else:
            soma = soma + int(codigo[i])*3
        print (soma)
#aqui, se o total da soma, não for divisil por 10 e o resto não der 0, ele da invalido; se o inverso, dá válido.
    if soma % 10 != 0:
        print ("código inválido")
        return val
    else:
        val =1
        print ("código válido")
        return val
    
print (validar_ISBN('78945612353'))


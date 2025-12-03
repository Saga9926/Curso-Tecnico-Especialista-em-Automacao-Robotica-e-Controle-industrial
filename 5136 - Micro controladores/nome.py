def obter_input_texto(nome):
    while True:
        entrada = input(nome)
        if entrada.isalpha():
            return entrada
        else:
            print("Por favor, insira apenas texto.")
nome = obter_input_texto("qual o seu nome?: ")
print("Seu nome é:", nome)

def obter_input_numero(idade):
    while True:
        entrada = input (idade)
        if entrada.isdigit():
            return int(entrada)
        else:
            print ("Por favor, insira apenas números.")

idade = obter_input_numero("qual sua idade? ")
if idade >= 18:
    print ("vc é o maior, sua idade é de ", idade , "anos")
elif idade < 18:
    print ("vc é pequenininho, vc só tem", idade , "anos")
    print ("teremos que nos despedir aqui, ate logo.")
    quit()
else:
    print ("idade inválida")
        
continuar = input("Pretende continuar? ").lower()

if continuar in ['sim','s']:
     print ('obrigado, para continuar pressione qualquer tecla!')
     continuar = input ("")
elif continuar in ['não','n' ,'nao']:
     print ('obrigado, teremos que parar por aqui')
     quit()
else:
    print ("obrigado, para continuar pressione qualquer tecla!")  
    continuar = input("")   

gênero = print ("qual o seu gênero?")
def menu():
    print('''
           MENU: 
          
         [A] - MASCULINO
         [B] - FEMININO
         [C] - Prefiro_não_dizer
          ''')


menu()

while True:
    opção = input('Escolha uma opção: ').lower()
    if opção in ['A','a']: 
        print ("vc é um homão!!")
        break
    elif opção in ['B','b']:
        print ("vc é um mulherão da porra!!") 
        break
    elif opção in ['C','c']:
        print ("No reaction fr '-'")
        break
    

    
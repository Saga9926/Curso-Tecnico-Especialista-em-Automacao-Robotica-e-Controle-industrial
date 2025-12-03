nome = print ("qual o seu nome?")
nome = input ("")
print ("obrigado")
idade = print ("sua idade, agora?!")
idade = int(input (""))
if idade >= 18:
    print ("vc é o maior")
elif idade < 18:
    print ("vc é pequenininho")
else:
    if idade < 18:
        print ("vc é maior de idade")

gênero = print ("qual o seu gênero?")
def menu():
    print('''
           MENU: 
          
         [A] - MASCULINO
         [B] - FEMININO
         [C] - Prefiro não dizer
          ''')
    (input('Escolha uma opção: '))

menu()

Masculino = "A"
if Masculino ("A"):
    print ("vc é um homão")
Feminino = "B"
if Feminino ("B"):
        print ("mulherão da porra")
Prefiro_não_dizer = "C"
if Prefiro_não_dizer ("C"):
        print ("no react")

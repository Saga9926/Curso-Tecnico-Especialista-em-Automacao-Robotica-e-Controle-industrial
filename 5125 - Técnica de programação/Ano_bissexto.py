"""
ano1=int (input("diz o ano:")
if ano1 % 4 == 0 and (ano1 % 100 != 0 or ano1 % 400 == 0):
print ("ano é bissexto")
else:
print("ano não é bissexto")
"""
"""
ano1=int (input("diz o ano:")
if ano1 % 400 ==0:
print ("ano é bissexto")
elif ano1 % 100 == 0:
print("ano não é bissexto")
elif ano1 % 4 == 0:
print ("ano é bissexto")
else:
print("ano não é bissexto)
"""
def anobissexto (ano1):
    if ano1 % 400 ==0:
        return f"{ano1} é bissexto"
    elif ano1 % 100 ==0:
        return f"{ano1} não é bissexto"
    elif ano1 % 4 ==0:
        return f"{ano1} é bissexto"
    else:
        return f"{ano1} não é bissexto"
ano1=int(input("diz o ano:"))
print (anobissexto(ano1))

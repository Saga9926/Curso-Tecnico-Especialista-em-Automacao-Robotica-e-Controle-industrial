km_percorridos = int(input(" Quantos km seu carro percorre?: " ))
gasto_medio = float(input(" Qual seu gasto médio de gasolina(litros/100km): "))
preço_combustivel = float(input(" Qual o valor da gasolina?: "))
combustivel_gasto = float (gasto_medio * km_percorridos) / 100
print ("Você gasta: ", combustivel_gasto)
custo_total = int(combustivel_gasto * preço_combustivel)
print ("Você gastará: (€)", custo_total)
 

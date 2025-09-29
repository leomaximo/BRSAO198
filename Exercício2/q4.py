'''4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
'''

dist = float(input("Digite a distancia total percorrida: "))
combust = float(input("Digite o cumbustível total gasto: "))
print("O consumo médio (km/l) é de ", round(dist/combust, 2) , "com a distancia total percorrida sendo ", dist , "e o consumo total de ", combust)
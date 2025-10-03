'''
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
'''

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)

if(imc < 18.5):
    print("A classificação do seu IMC é abaixo do peso")
elif(imc < 25):
    print("A classificação do seu IMC é Peso normal")
elif(imc < 30):
    print("A classificação do seu IMC é Sobrepeso")
else:
    print("A classificação do seu IMC é Obeso")


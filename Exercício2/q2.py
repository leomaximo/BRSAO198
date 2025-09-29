'''2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
'''

valor = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o valor do desconto em porcentagem: "))
print("O valor final do produto é", valor - (valor * (desconto/100)), "reais com o valor inicial sendo", valor , " e com o deconto de ", desconto,"%")
'''1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.'''
txdolar = 5.2
txeuro = 6.15
reais = float(input("Digite o valor em reais:"))
print("O valor RS", reais, " equivale a", round((reais / txdolar),2), "dolares e a", round((reais / txeuro),2) ," euros")
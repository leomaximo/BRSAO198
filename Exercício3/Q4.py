'''
4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
'''


ano = float(input("Digite um ano:"))
if( ano % 4):
    print("O ano não é bissexto")
else:
    print("O ano é bissexto")
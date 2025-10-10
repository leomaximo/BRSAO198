'''
Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
'''


par = 0 
impar = 0

aux = 1
while aux:
    num = int(input("Digite um número:   "))
    if num % 2:
        impar = impar + 1
    else:
        par = par + 1

    aux = int(input("Digite 0 se quiser parar ou digite qualquer outro numero se quiser continuar testando numeros."))

print("Foram ",par," numero pares e",impar,  "numero impares")  
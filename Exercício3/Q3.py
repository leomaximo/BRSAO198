'''
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

'''

def CelsiusFahrenheit(celsius):
    return ((celsius * 1.8) + 32)

def CelsiusKelvin(celsius):
    return celsius + 275.15

def FahrenheitCelsius(farenh):
    return ( (farenh - 32)/1.8 )

def FahrenheitKelvin(farenh):
    return ( ((farenh - 32)/1.8 ) + 275.15)

def KelvinCelsius(kelvin):
    return kelvin - 275.15

def kelvinFarenheit(kelvin):
    cel = KelvinCelsius(kelvin)
    return CelsiusFahrenheit(cel)


temp = float(input("Digite a temperatura"))
unidadeOrigem = float(input("Digite 1 se sua unidade de origem é Celsius \n" \
"2 se é Farenheit \n" \
"3 se é Kelvin \n"))
if(unidadeOrigem == 1):
    aux = float(input("Digite 1 se quer transformar para Fahrenheit \n" \
    "Digite 2 para trnasformar para kelvin \n"))
    if(aux == 1):
        print("A temperatura me celsius é ",temp," e em Fahrenheit é ", CelsiusFahrenheit(temp))
    elif(aux == 2):
        print("A temperatura me celsius é ",temp," e em Kelvin é ", CelsiusKelvin(temp))
    else:
        print("Número inexistente")

if(unidadeOrigem == 2):
    aux = float(input("Digite 1 se quer transformar para Celsius \n" \
    "Digite 2 para trnasformar para kelvin \n"))
    if(aux == 1):
        print("A temperatura me Fahrenheit é ",temp," e em Celsius é ", FahrenheitCelsius(temp))
    elif(aux == 2):
        print("A temperatura me Fahrenheit é ",temp," e em Kelvin é ", FahrenheitKelvin(temp))
    else:
        print("Número inexistente")

if(unidadeOrigem == 3):
    aux = float(input("Digite 1 se quer transformar para Fahrenheit \n" \
    "Digite 2 para trnasformar para Celsius \n"))
    if(aux == 1):
        print("A temperatura me Kelvin é ",temp," e em Fahrenheit é ", kelvinFarenheit(temp))
    elif(aux == 2):
        print("A temperatura me Kelvin é ",temp," e em Celsius é ", KelvinCelsius(temp))
    else:
        print("Número inexistente")
        

        






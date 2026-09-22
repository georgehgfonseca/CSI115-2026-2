# Escreva um programa Python que leia o valor em reais (BRL) e exiba o valor convertido
# para dólares americanos (USD) considerando a taxa de conversão::
# USD =BRL/5.32
reais = float(input("Valor em BRL: "))
dolares = reais * 5.32
print(f"Valor em dolares: {dolares:.2f} USD")
# Escreva um programa Python que leia o peso e a altura do usuário e calcule seu IMC:
# IMC = peso / (altura ^ 2)
# posteriormente, informe a qual faixa o usuário pertence, sendo que:

# IMC entre 18.5 e 25.0: peso normal;
# IMC acima de 25.0: sobrepeso;
# IMC abaixo de 18.5: abaixo do peso
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / (altura * altura)

if imc > 25:
    print("Sobrepeso")
elif imc < 18.5:
    print("Abaixo")
else:
    print("Peso normal")
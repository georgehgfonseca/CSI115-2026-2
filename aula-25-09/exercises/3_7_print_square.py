# Escreva um programa Python que leia um tamanho n e imprima o seguinte quadrado
# formado por asteriscos (para n = 4):

# * * * *
# *     *
# *     *
# * * * *
n = int(input("Informe o lado do quadrado: "))

# separe em uma funcao o codigo que imprime o quadrado
def print_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                print(" * ", end="")
            else:
                print("   ", end="")
        print()

print_square(n)

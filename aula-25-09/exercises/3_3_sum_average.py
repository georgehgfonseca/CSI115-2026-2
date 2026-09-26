# Faça um programa que leia 5 números usando laço de repetição e informe a soma e a
# média dos números sem usar as funções sum e avg.
n = 5
sum = 0

# armazenar esses valores numa lista
nums = []

for i in range(n):
    num = float(input(f"Informe o {i + 1}o numero: "))
    nums.append(num)

for num in nums:
    sum += num

print(f"Soma eh {sum}")
print(f"Media eh {sum / n}")
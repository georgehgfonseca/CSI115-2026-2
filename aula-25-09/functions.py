# pode definir valores padrao para cada parametro
def soma(a=0, b=0):
    return a + b

# print(soma(5, 6)) # 11
# print(soma(5)) # 5
# print(soma()) # 0

# Pode ser recursiva
def fatorial(n: int) -> int:
    if n == 1:
        return 1
    return fatorial(n - 1) * n

print(fatorial(5)) # 120

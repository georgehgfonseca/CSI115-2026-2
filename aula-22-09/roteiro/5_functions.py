# funções são blocos de código que podem ser reutilizados. Elas são úteis para organizar o código e evitar repetição.
def is_approved(grade, absences):
    if grade >= 6 and absences <= 0.25:
        return True
    return False

print(is_approved(7, 0.2)) # True
print(is_approved(5, 0.1)) # False

# assert pode ser usado para criar testes automatizados. Ele verifica se uma condição é verdadeira e, se não for, lança um erro.
assert is_approved(8, 0.3) == False

# funções recursivas são funções que chamam a si mesmas. Elas são úteis para resolver problemas que podem ser divididos em subproblemas menores, como a sequência de Fibonacci.
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
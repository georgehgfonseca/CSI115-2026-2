a = [1, 2, 3]
# por referencia (colecoes, objetos)
b = a

a[0] = 4 # tambem altera em b
# print(b) # [4, 2, 3]

# quero uma copia
a = [1, 2, 3]
b = a.copy()
a[0] = 4
# print(b) # [1, 2, 3]

def incrementa(x):
    x += 1
    return x

a = 5
print(incrementa(a)) # 6
print(a) # 5
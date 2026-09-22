notas = [8, 6, 3, 7, 10, 1]

# print(notas[0]) # 8
# print(notas[-1]) # 1
# print(notas[0:2]) # [8, 6] posicoes de 0 a 2 exceto o 2 (exclusive)

notas.append(9) # O(1)
notas.append(["Banana", "Uva", "Pera"])

# print(5 in notas) # False O(n)
notas.insert(0, 4) # O(n)

notas.pop() # remove o ultimo elemento O(1)
notas.pop(2) # remove o elemento da posicao 2 O(n)

# range(inicio=0, fim, passo=1)
#for value in range(1, 10, 1):
#    print(value)

# print(f"notas contem {len(notas)} elementos")
# print(notas)
# for nota in notas:
#     print(nota)
 
for i in range(len(notas)): 
    print(f"posicao {i} - valor: {notas[i]}")

matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9],
          [10, 11, 12]]

for i in range(len(matrix)): # 0 --- 3
    for j in range(len(matrix[i])): # 0 -- 2
        print(f"posicao {i}, {j} - valor: {matrix[i][j]}")

# Listas são coleções ordenadas de elementos, que podem conter elementos duplicados.
notas = [8, 6, 4, 7, 9, 10, 2]
notas.append(5) # adiciona no final da lista em O(1)
notas = notas[1:] # remove o primeiro elemento da lista em O(n)
notas.remove(5) # remove o elemento 5 da lista em O(n)
notas.append("Banana") # pode conter tipos diferentes de elementos, mas não é recomendado
notas.pop() # remove o último elemento da lista em O(1)

print(notas[-1]) # último elemento
print(notas[0:2]) # elementos do índice 0 até o índice 2 (exclusivo)
print(5 in notas) # False custa O(n)

for nota in notas: # iteração sobre os elementos da lista
    print(nota)

for i in range(len(notas)):
    print(notas[i])

# listas podem ser multidimensionais, ou seja, listas de listas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])
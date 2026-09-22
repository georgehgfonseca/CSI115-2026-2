notas = [5, 6, 3, 6, 8]
notas[0]

# pares chave:valor {chave:valor}
# nao eh ordenado e nao permite duplicata, nao acessa por indice
pessoas = {
    "Alice": 20,
    "Bob": 21,
    "Carlos": 18,
}

pessoas["Diogo"] = 20 # se nao existe, cria nova chave com valor
pessoas["Alice"] = 30 # se ja existe, sobrescreve o valor


nomes = ["Alice", "Bob", "Carlos"]
valores = [20, 21, 18]

# acessar valor por chave em O(1) independente do tamano do dicionario
# ex. qual o valor para Bob?
print(pessoas["Bob"]) # 21

# remove chave do dicionario
pessoas.pop("Carlos")
print(pessoas)


# grafo
friends = {"Alice": {"Bob", "Carlos"},
           "Bob": {"Alice"},
           "Carlos": {"Alice", "Diogo"},
           "Diogo": {"Carlos"}}

print(friends)

g = {0: {1, 2},
     1: {0},
     2: {0, 3},
     3: {2}}
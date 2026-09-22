# Dicionários (dicts) são coleções de pares chave-valor. Eles são úteis para armazenar e recuperar dados de forma eficiente.
pessoas = {"Alice": 25, "Bob": 30, "Charlie": 35}
pessoas["David"] = 40 # adiciona um novo par chave-valor em O(1)
pessoas["Alice"] = 26 # atualiza o valor da chave "Alice" em O(1)
pessoas.pop("Bob") # remove a chave "Bob" do dicionário em O(1)

print(pessoas["Charlie"]) # imprime o valor da chave "Charlie"
print("Alice" in pessoas) # True custa O(1)
print("David" in pessoas) # True custa O(1)

for pessoa in pessoas: # iteração sobre os pares chave-valor do dicionário
    print(f"{pessoa}: {pessoas[pessoa]}")

# dicts podem ser usados para representar grafos, ex.:
friends = {"Alice": {"Bob", "Charlie"}, "Bob": {"Alice"}, "Charlie": {"Alice"}}

print(friends["Alice"])  # imprime os amigos de Alice
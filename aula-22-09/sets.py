notas = [8, 6, 3, 7, 10, 1]
print(5 in notas) # O(n)

# nao aceita valores duplicados, ordem nao e importante
cidades = {"JM", "OP", "BH", "SP"}
print(cidades)

print("RJ" in cidades) # False O(1)
cidades.add("RJ")
cidades.discard("SP") # Remvoe o elemento SP se existir em O(1)

for cidade in cidades:
    print(cidade)

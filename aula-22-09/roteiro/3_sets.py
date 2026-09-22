# Conjuntos (sets) são coleções de elementos únicos e não ordenados. Eles são úteis para operações de teste de pertinência, eliminação de duplicatas e operações matemáticas como união, interseção e diferença.
cidades = {"JM", "SP", "RJ", "BH", "OP"}
cidades.add("BV") # adiciona no final do conjunto em O(1)
cidades.discard("BV") # remove o elemento "BV" do conjunto em O(1)
cidades.add("JM") # não é possível adicionar elementos duplicados, então "JM" não será adicionado novamente

print("BV" in cidades) # True custa O(1)
print("JM" in cidades) # False custa O(1)

for cidade in cidades: # iteração sobre os elementos do conjunto
    print(cidade)
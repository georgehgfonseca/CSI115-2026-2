nota = float(input("Informe a nota: "))
faltas = int(input("Informe o número de faltas: "))
nome = input("Informe o nome do aluno: ")

print("Aluno:", nome, "\n", "Nota:", nota, "\n", "Faltas:", faltas)
print(f"Aluno: {nome}\nNota: {nota:.2f}\nFaltas: {faltas}")

# identação define anihamento de blocos de código
if nota >= 6 and faltas <= 18:
    print("Aprovado")
else:
    print("Reprovado")
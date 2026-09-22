# Faça um Programa que pergunte quanto você ganha por hora e o número de horas tra
# balhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que
# são descontados 15% para o Imposto de Renda, 10% para o INSS e 2% para o sindicato,
# faça um programa que informe:

# O salário bruto.
# Quantia paga ao INSS.
# Quantia para ao sindicato.
# O salário líquido.
valor_hora = float(input("Informe o valor da hora trabalhada: "))
horas = float(input("Informe o numero de horas: "))
salario = horas * valor_hora

print(f"Salario bruto: {salario}")
ir = salario * 0.15
inss = salario * 0.1
sindicato = salario * 0.02
salario_liquido = salario - ir - inss - sindicato

print(f"- IR: {ir}")
print(f"- INSS: {inss}")
print(f"- Sindicato: {sindicato}")
print(f"- Salario liquido: {salario_liquido}")
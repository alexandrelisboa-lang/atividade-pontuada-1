import os
os.system("cls")

# ENTRADA
print("EMPRESTIMO")

renda = float(input("digite sua Renda mensal: R$ "))
valor_emprestimo = float(input("digite o Valor total do empréstimo: R$ "))
parcelas = int(input(" digite seu Número de prestações: "))

valor_prestacao = valor_emprestimo / parcelas


condicao1 = valor_emprestimo <= (renda * 10)
condicao2 = valor_prestacao <= (renda * 0.30)

if condicao1 and condicao2:
    print("Empréstimo concedido!")
else:
    print("Empréstimo negado!")
    if not condicao1:
        print("- Valor total excede 10x a renda.")
    if not condicao2:

        print("- Valor da prestação excede 30% da renda.")

import os
os.system("cls")

# ENTRADA
print("POSTO")

litros = float(input("Quantidade de litros: "))
tipo = input("Tipo (A-alcool, G-gasolina): ")

preco_alcool = 3.79
preco_gasolina = 6.59

if tipo == 'alcooll':
    total_bruto = litros * preco_alcool
    desc = 0.03 if litros <= 20 else 0.05
    valor_final = total_bruto * (1 - desc)
    
elif tipo == 'gasolina':
    total_bruto = litros * preco_gasolina
    desc = 0.04 if litros <= 20 else 0.06
    valor_final = total_bruto * (1 - desc)


print(f"Valor a pagar: R$ {valor_final:.2f}")

print("fim")

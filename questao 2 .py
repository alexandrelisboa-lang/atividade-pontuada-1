import os
os.system("cls")

#ENTRADA

print("    SOLICITANDO DADOS     ")

nome=input("por favor digite seu nome: ")
sexo=input("por favor digite seu sexo: ")
est_civil=input("por favor digite seu est civil: ")

#PROCESSAMENTO

if sexo == "F" and est_civil == "casada":
    tempo=int(input("quanto tempo de casada (anos)?  "))
    print(f" seu nome e{nome} \no seu sexo e {sexo}\ n seu estado civiel e {est_civil}\no seu tempo de casada e {tempo}")
    
#SAIDA
else:
    print("        RESUMO      ")
    print(f"seu nome e {nome} \no seu sexo e {sexo} \nseu estado civil e {est_civil}")
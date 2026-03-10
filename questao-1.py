import os
os.system("cls")

#ENTRADA
print( "valores A,B,C")

n1= int(input("por favor digite um numero: "))
n2= int(input("por favor digite o segundo numero: "))
n3= int(input("por favor digite  terceiro numero: "))

#PROCESSAMENTO
soma= n1+n2

if soma < n3:
    print(f"a soma({soma})) do primeiro numero ({n1}) mais o segundo numero ({n2}) e menor que o terceiro numero ({n3})")
elif soma > n3:
    print(f"a soma ({soma}) do primeiro numero ({n1}) mais o segundo numero ({n2}) e maior que o terceiro numero ({n3})")
    

print ("      fim      ")
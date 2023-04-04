#Escreva um programa que inverta os caracteres de um string.
#declaramos as variaveis
nome = "thiago"
inverter = ""

#o laço for lê o tamanho da sting e salva na varialvel inverter os caracteres da string do ultimo ao primeiro
for i in range(len(nome)-1, -1, -1):
    inverter += nome[i]

print(f"A nome invertido é: {inverter}")
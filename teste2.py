# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

with open('tabeladados.json') as myfile:
    dados = json.load(myfile)

#O menor valor de faturamento ocorrido em um dia do mês;
menor_valor = float('inf')
for dia in dados:
    if dia['valor'] < menor_valor:
        menor_valor = dia['valor']

print(f"Menor valor de faturamento: {menor_valor:.2f}")

#O maior valor de faturamento ocorrido em um dia do mês;
maior_valor = float('-inf')
for dia in dados:
    if dia['valor'] > maior_valor:
        maior_valor = dia['valor']

print(f"Maior valor de faturamento: {maior_valor:.2f}")

# Calculando a média mensal de faturamento
soma_valores = 0
for dia in dados:
    soma_valores += dia['valor']

media_mensal = soma_valores / len(dados)

# Encontrando o número de dias em que o valor de faturamento foi superior à média mensal
dias_acima_media = 0
for dia in dados:
    if dia['valor'] > media_mensal:
        dias_acima_media += 1

print(f"Número de dias acima da média mensal: {dias_acima_media}")

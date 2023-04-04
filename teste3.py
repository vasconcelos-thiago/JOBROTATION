#criamos um objeto lista com os dados fornecidos
faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
# a função abaixo (sum) é usada para somar os valores do elementos de um Set 
total = sum(faturamento_mensal.values())

#o laço for itera os valores na lista e a variavel porcento recebe o valor do calculo de porcentagem 
for estado, valor in faturamento_mensal.items():
    porcento = (valor / total)*100
    print(f"{estado}: {porcento:.2f}%")

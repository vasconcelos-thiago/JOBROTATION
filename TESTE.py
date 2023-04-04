#  Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência

#digite um numero inteiro para começar
numero = int(input("Digite um numero: "))

#aqui declaramos as nossas variaveis e nosso objeto do tipo lista
num1 = 0
num2 = 1
fibo = [num1, num2]

# aqui usamos o laço while para iterar enquanto a nossa condição for verdadeira
while True:
    num3 = num1 + num2
    if num3 > numero:
        break
    fibo.append(num3)
    num1, num2 = num2, num3

#aqui exibimos o resultado final  
if numero in fibo:
    print(numero, "faz parte da sequencia de fibonacci")
else:
    print(numero, "não faz parte da sequencia de fibonacci")

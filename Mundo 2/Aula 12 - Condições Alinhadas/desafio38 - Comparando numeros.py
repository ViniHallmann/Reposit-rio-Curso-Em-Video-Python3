###Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
num = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num > num2:
    print(f'O número {num} é maior que o número {num2}')
elif num < num2:
    print(f'O número {num2} é maior que o número {num}')
elif num == num2:
    print(f'Os dois números são iguais')
'''4. Crie um programa que sorteia, aleatoriamente, um número inteiro menor que 100.
Dica: use a função randrange() da biblioteca random. Essa função recebe como parâmetro o valor limite para a escolha aleatória ou um intervalo se passado o limite mínimo e máximo. Por exemplo, randrange(5) gera valores inteiros menores que 5.'''

from random import randrange

print(f'O número sorteado é {randrange(100)}')
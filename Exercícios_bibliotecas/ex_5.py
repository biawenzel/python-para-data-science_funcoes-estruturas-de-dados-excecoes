'''5. Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.
Dica: use a função pow() da biblioteca math'''

from math import pow

x = int(input('Digite o 1º número: '))
y = int(input('Digite o 2º número: '))

print(f'O resultado de {x} elevado a {y} é {pow(x, y)}')
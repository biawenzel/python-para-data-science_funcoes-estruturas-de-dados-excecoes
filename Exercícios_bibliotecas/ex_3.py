'''3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]'''

from random import choice

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
print(f"Número escolhido: {choice(lista)}")

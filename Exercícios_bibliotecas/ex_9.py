'''9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte: numeros = [2, 8, 15, 23, 91, 112, 256].
No final, informe quais números possuem raízes inteiras e seus respectivos valores.
• Dica: use a comparação entre a divisão inteira (//) da raiz por 1 com o valor da raiz para verificar se o número é inteiro. Por exemplo:
num = 1.5
num_2 = 2
print(f'{num} é inteiro? :', num // 1 == num)
print(f'{num_2} é inteiro? :', num_2 // 1 == num_2)
• Saída:
1.5 é inteiro? : False
2 é inteiro? : True'''

from math import sqrt

numeros = [2, 4, 8, 15, 23, 91, 112, 256]
raiz = []

for num in numeros:
    raiz.append(sqrt(num))
    
for i in range(len(raiz)):
    if raiz[i] // 1 == raiz[i]:
        print(f'A raiz quadrada inteira do numero {numeros[i]} é {int(raiz[i])}')
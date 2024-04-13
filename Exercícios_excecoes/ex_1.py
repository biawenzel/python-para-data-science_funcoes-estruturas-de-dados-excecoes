'''1. Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses números. O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.
Teste o programa com o segundo valor numérico do input igual a 0. Também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem.'''

numero1 = float(input(f'Digite o número dividendo: '))
numero2 = float(input(f'Digite o número divisor: '))

try:
    resultado = numero1/numero2
    print(f'{numero1}/{numero2} = {resultado}')
except ZeroDivisionError as e:
    print(type(e),': Impossível dividir por zero.')
finally:
    print('Operação encerrada.')
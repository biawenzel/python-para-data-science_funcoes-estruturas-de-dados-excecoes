'''3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
Utilize o return na função e salve a nova lista na variável mult_3.'''

numeros = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
mult_3 = []

def multiplos_3(lista):
    for i in range(len(lista)):
        if lista[i] % 3 == 0:
            mult_3.append(lista[i])
    return mult_3

mult_3 = multiplos_3(numeros)
print(mult_3)
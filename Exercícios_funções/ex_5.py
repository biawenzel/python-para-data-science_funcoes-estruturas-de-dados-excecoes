'''5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.
Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:
"Nota da manobra: [media]"'''

lista_notas = []
media = 0

for i in range(1, 6):
    nota = float(input(f"Digite a {i}ª nota: "))
    lista_notas.append(nota)

maior_nota = max(lista_notas)
menor_nota = min(lista_notas)
for i in range(len(lista_notas)):
    if (lista_notas[i] != maior_nota) and (lista_notas[i] != menor_nota):
        media += lista_notas[i]
    
print(f'Nota da manobra: {(media/3)}')
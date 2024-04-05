'''6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:
- maior nota
- menor nota
- média
- situação (Aprovado(a) ou Reprovado(a))
Para testar o comportamento da função, os dados podem ser exibidos em um texto: "O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"'''

lista_notas = []

for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    lista_notas.append(nota)

def desempenho(lista):
    maior_nota = max(lista_notas)
    menor_nota = min(lista_notas)
    media = sum(lista_notas)/len(lista_notas)

    if media >= 6:
        situacao = "Aprovado(a)"
    else:
        situacao = "Reprovado(a)"
    return maior_nota, menor_nota, media, situacao

maior_nota, menor_nota, media, situacao = desempenho(lista_notas)

print(f'O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior_nota} pontos e a menor nota de {menor_nota} pontos e foi {situacao}')
'''7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]
O texto exibido ao fim deve ser parecido com: "Nome completo: Ana Silva"
Dica: utilize a função map para mapear os nomes e sobrenomes e as funções de string para tratar o texto.'''

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nome_completo = map(lambda nome, sobrenome: f'{nome.capitalize()} {sobrenome.capitalize()}', nomes, sobrenomes)

for i in nome_completo:
    print(f'Nome completo: {i}')
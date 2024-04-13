# Python para Data Science - funções, estruturas de dados e exceções

## Exercícios - Bibliotecas

1. Escreva um código para instalar a versão 3.7.1 da biblioteca matplotlib.

2. Escreva um código para importar a biblioteca numpy com o alias np.

3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.\
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

4. Crie um programa que sorteia, aleatoriamente, um número inteiro menor que 100.\
Dica: use a função randrange() da biblioteca random. Essa função recebe como parâmetro o valor limite para a escolha aleatória ou um intervalo se passado o limite mínimo e máximo. Por exemplo, randrange(5) gera valores inteiros menores que 5.

5. Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.\
Dica: use a função pow() da biblioteca math

6. Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.

7. Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.

"Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"

8. Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:

frutas = ["maçã", "banana", "uva", "pêra", "manga", "coco", "melancia", "mamão", "laranja", "abacaxi", "kiwi", "ameixa"]

9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte:

numeros = [2, 8, 15, 23, 91, 112, 256]

No final, informe quais números possuem raízes inteiras e seus respectivos valores.

Dica: use a comparação entre a divisão inteira (//) da raiz por 1 com o valor da raiz para verificar se o número é inteiro. Por exemplo:

num = 1.5\
num_2 = 2\
print(f'{num} é inteiro? :', num // 1 == num)\
print(f'{num_2} é inteiro? :', num_2 // 1 == num_2)

Saída:

1.5 é inteiro? : False\
2 é inteiro? : True

10. Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.\
Dica: use a variável pi e o método pow() da biblioteca math. O cálculo da área de um círculo é de: A = π*r^2 (lê-se pi vezes raio ao quadrado).

## Exercícios - Funções

1. Escreva um código que lê a lista abaixo e faça:\
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
- A leitura do tamanho da lista
- A leitura do maior e menor valor
- A soma dos valores da lista
- Ao final exiba uma mensagem dizendo:
"A lista possui [tam] números em que o maior número é [maior] e o menor número é [menor]. A soma dos valores presentes nela é igual a [soma]"\
Dica: use as funções embutidas presentes na documentação do Python.

2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

Tabuada do 7:\
7 x 0 = 0\
7 x 1 = 7\
[...]\
7 x 10 = 70

3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:\
[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]\
Utilize o return na função e salve a nova lista na variável mult_3.

4. Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.

5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.\
Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:\
"Nota da manobra: [media]"

6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:
- maior nota
- menor nota
- média
- situação (Aprovado(a) ou Reprovado(a))\
Para testar o comportamento da função, os dados podem ser exibidos em um texto:\
"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"

7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:
- nomes = ["joão", "MaRia", "JOSÉ"]
- sobrenomes = ["SILVA", "souza", "Tavares"]

O texto exibido ao fim deve ser parecido com:\
- "Nome completo: Ana Silva"\
Dica: utilize a função map para mapear os nomes e sobrenomes e as funções de string para tratar o texto.

8. Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.

Para teste, utilize as seguintes listas de gols marcados e sofridos:
- gols_marcados = [2, 1, 3, 1, 0]
- gols_sofridos = [1, 2, 2, 1, 3]

Provável texto exibido:\
"A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"

9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.\
"Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"

10. Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.

Dica: utilize as funções lambda e filter() para filtrar essas palavras. Lembrando que a função embutida filter() recebe uma função (no nosso exemplo uma função lambda) e filtra um iterável de acordo com a função. Para tratar a frase use replace() para trocar a ',' '.', '!' e '?' por espaço.

Use a frase "Aprender Python aqui na Alura é muito bom" para testar o código.

## Exercícios - Estruturas de dados

1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:\
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:\
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

3. A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.

4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:\
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] e os valores estão em despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].

6. Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores de venda para que você ajude a realizar a filtragem dos dados a partir de um código:\
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]\
Crie uma lista usando list comprehension para filtrar os valores de 2022 e que sejam maiores que 6000.

7. Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da seguinte maneira:
- Glicose igual ou inferior a 70: 'Hipoglicemia'
- Glicose entre 70 a 99: 'Normal'
- Glicose entre 100 e 125: 'Alterada'
- Glicose superior a 125: 'Diabetes'
A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia em cada tupla.\
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

8. Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas:
- id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
- quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
- preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é obtida multiplicando a quantidade pelo preço unitário. Além disso, a tabela precisa conter um cabeçalho indicando as colunas: 'id', 'quantidade', 'preco' e 'total'.\
Crie uma lista de tuplas em que cada tupla tenha id, quantidade, preço e valor total, na qual a primeira tupla é o cabeçalho da tabela.

9. Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação de qual é o Estado a que pertence: estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG'].\
A empresa sempre está abrindo novas filiais, de modo que a tabela está constantemente recebendo novos registros e o gestor gostaria de possuir a informação atualizada da quantidade de filiais em cada Estado.\
A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com a chave sendo o nome de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.
- Dica: Você pode fazer um passo intermediário para gerar uma lista de listas em que cada uma das listas possui o nome de apenas um Estado com valores repetidos.

10. Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade de pessoas colaboradoras e o(a) gestor(a) gostaria de ter um agrupamento da soma dessas pessoas para cada estado. As informações contidas na tabela são:\
funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

A partir da lista de tuplas, crie um dicionário em que as chaves são os nomes dos Estados únicos e os valores são as listas com o número de colaboradores(as) referentes ao Estado. Crie também um dicionário em que as chaves são os nomes dos Estados e os valores são a soma de colaboradores(as) por Estado.
- Dica: Você pode fazer um passo intermediário para gerar uma lista de listas em que cada uma das listas possui apenas os valores numéricos de funcionários(as) de cada Estado.

## Exercícios - Exceções

1. Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses números. O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.\
Teste o programa com o segundo valor numérico do input igual a 0. Também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem.

2. Faça um programa que solicite à pessoa usuária digitar um texto que será uma chave a ser pesquisada no seguinte dicionário: idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, armazenando o resultado do valor em uma variável. O código deve conter um tratamento de erro KeyError, imprimindo a informação 'Nome não encontrado', caso ocorra o erro; e imprimir o valor caso não ocorra nenhum.\
Teste o programa com um nome presente em uma das chaves do dicionário e com um que não esteja no dicionário para verificar a mensagem de erro.

3. Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.

4. Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um das listas, formando uma lista de tuplas de 3 elementos, no qual o primeiro e segundo elemento da tupla são os valores na posição i das listas e o terceiro elemento é a soma dos valores na posição i das listas.\
A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar como resultado a lista de tuplas. Caso as listas enviadas como parâmetro tenham tamanhos diferentes, a função deve retornar um IndexError com a frase: 'A quantidade de elementos em cada lista é diferente.'
- Dados para testar a função:\
Valores sem erro:\
lista1 = [4,6,7,9,10]\
lista2 = [-4,6,8,7,9]

Listas com tamanhos diferentes:\
lista1 = [4,6,7,9,10,4]\
lista2 = [-4,6,8,7,9]

Listas com valores incoerentes:\
lista1 = [4,6,7,9,'A']\
lista2 = [-4,'E',8,7,9]

5. Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste. Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.\
Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, você deve lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida". O cálculo das 3 notas só será realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes. Se não for lançada a exceção, será exibida uma lista com as notas em cada teste.\
- Os dados para o teste do código são:\
Gabarito da prova:\
gabarito = ['D', 'A', 'B', 'C', 'A']
- Abaixo temos 2 listas de listas que você pode usar como teste\
Notas sem exceção:\
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

Notas com exceção:\
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

- Dica: Para verificar se uma entrada da lista não está entre as alternativas possíveis, use a estrutura lista[i] not in ['A','B','C','D']. Por exemplo, 1 not in [2,3,4]... Saída: True.

6. Você está trabalhando com processamento de linguagem natural (NLP) e, dessa vez, sua líder requisitou que você criasse um trecho de código que recebe uma lista com as palavras separadas de uma frase gerada pelo ChatGPT.\
Você precisa criar uma função que avalia cada palavra desse texto e verificar se o tratamento para retirar os símbolos de pontuação (',' '.', '!' e '?') foi realizado. Caso contrário, será lançada uma exceção do tipo ValueError apontando o 1º caso em que foi detectado o uso de uma pontuação por meio da frase "O texto apresenta pontuações na palavra "[palavra]".". Essa demanda é voltada para a análise do padrão de frases geradas pela inteligência artificial.
- Dica: Para verificar se uma ou mais das pontuações estão presentes em cada palavra, utilize a palavra chave or na condição if. Por exemplo, 'a' in 'alura' or 'b' in 'alura'… Saída: True
- Os dados para o teste do código são:\
Lista tratada:\
lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil', 'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde', 'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

Lista não tratada:\
lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil', 'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde', 'análise', 'de', 'dados', 'até', inteligência', 'artificial!']

7. Você foi contratado(a) como uma pessoa cientista de dados para auxiliar um laboratório que faz experimentos sobre o comportamento de uma cultura de fungos. O laboratório precisa avaliar constantemente a razão (divisão) entre os dados de pressão e temperatura do ambiente controlado recolhidos durante a experimentação para definir a melhor condição para os testes.\
Para cumprir com a demanda, você precisa criar uma função divide_colunas que recebe os dados das colunas de pressão e temperatura (que vem no formato de listas) e gerar uma nova coluna com o resultado da divisão. Os parâmetros da função são as duas listas e você deve tratar dentro dela ao menos 2 tipos de exceções:
- Verificar se as listas têm o mesmo tamanho (ValueError)
- Verificar se existe alguma divisão por zero (ZeroDivisionError)\
Para testar a função, vamos realizar a divisão entre duas listas de dados coletados no experimento, com os valores de pressão e temperatura do ambiente controlado.\
- Como teste, use os seguintes dados:

Dados sem exceção:\
pressoes = [100, 120, 140, 160, 180]\
temperaturas = [20, 25, 30, 35, 40]

Dados com exceção:\
(a) Exceção de ZeroDivisionError\
pressoes = [60, 120, 140, 160, 180]\
temperaturas = [0, 25, 30, 35, 40]

(b) Exceção de ValueError\
pressoes = [100, 120, 140, 160]\
temperaturas = [20, 25, 30, 35, 40]

- Dica: Você pode usar zip() para parear os dados da lista_1 com a lista_2. Crie uma estrutura try-except que caso uma das exceções sejam lançadas, podemos ver o tipo de erro na saída.
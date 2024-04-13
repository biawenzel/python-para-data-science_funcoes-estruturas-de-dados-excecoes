'''7. Você foi contratado(a) como uma pessoa cientista de dados para auxiliar um laboratório que faz experimentos sobre o comportamento de uma cultura de fungos. O laboratório precisa avaliar constantemente a razão (divisão) entre os dados de pressão e temperatura do ambiente controlado recolhidos durante a experimentação para definir a melhor condição para os testes. Para cumprir com a demanda, você precisa criar uma função divide_colunas que recebe os dados das colunas de pressão e temperatura (que vem no formato de listas) e gerar uma nova coluna com o resultado da divisão. Os parâmetros da função são as duas listas e você deve tratar dentro dela ao menos 2 tipos de exceções:
Verificar se as listas têm o mesmo tamanho (ValueError)
Verificar se existe alguma divisão por zero (ZeroDivisionError)
Para testar a função, vamos realizar a divisão entre duas listas de dados coletados no experimento, com os valores de pressão e temperatura do ambiente controlado.
Como teste, use os seguintes dados:
- Dados sem exceção: pressoes = [100, 120, 140, 160, 180]; temperaturas = [20, 25, 30, 35, 40]
- Dados com exceção:
1) Exceção de ZeroDivisionError: pressoes = [60, 120, 140, 160, 180]; temperaturas = [0, 25, 30, 35, 40]
2) Exceção de ValueError: pressoes = [100, 120, 140, 160]; temperaturas = [20, 25, 30, 35, 40]
- Dica: Você pode usar zip() para parear os dados da lista_1 com a lista_2. Crie uma estrutura try-except que caso uma das exceções sejam lançadas, podemos ver o tipo de erro na saída.'''

pressoes_sem_ex = [100, 120, 140, 160, 180]; temperaturas_sem_ex = [20, 25, 30, 35, 40]
pressoes_zerodiv = [60, 120, 140, 160, 180]; temperaturas_zerodiv = [0, 25, 30, 35, 40]
pressoes_value = [100, 120, 140, 160]; temperaturas_value = [20, 25, 30, 35, 40]

def divide_colunas(pressao, temp):
    try:
        if len(pressao) != len(temp):
            raise ValueError('As listas são de tamanhos diferentes')
        resultados = [round(a/b, 2) for a, b in zip(pressao, temp)]
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(f'{e}: A 2ª lista não pode possuir um valor igual a 0')
    else:
        print(resultados)
    
#divide_colunas(pressoes_sem_ex, temperaturas_sem_ex)
#divide_colunas(pressoes_zerodiv, temperaturas_zerodiv)
divide_colunas(pressoes_value, temperaturas_value)
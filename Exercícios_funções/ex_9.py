'''9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para uma das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.
- O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. Os gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.
- Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).
- Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.
"Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"'''

diaria = 150
consumo_gasolina = 14
preco_gasolina = 5
gastos_extras = [200, 400, 250, 300] #Salvador, Fortaleza, Natal e Aracaju
distancias = [850, 800, 300, 550] #Salvador, Fortaleza, Natal e Aracaju

cidade = input('Digite o destino da viagem (Salvador, Fortaleza, Natal ou Aracaju): ')
dias = int(input(f'Quantos dias deseja ficar em {cidade}? '))

def gasto_hotel(dias):
    total_hotel = dias * diaria
    return total_hotel

def gasto_gasolina(cidade, distancias):
    for i in range(len(distancias)):
        if cidade == "Salvador":
            distancia = distancias[0]
        elif cidade == "Fortaleza":
            distancia = distancias[1]
        elif cidade == "Natal":
            distancia == distancias[2]
        else:
            distancia == distancias[3]
    total_gasolina = distancia * 2 * (preco_gasolina / consumo_gasolina)
    return total_gasolina

def gasto_passeio(cidade, dias, gastos_extras):
    for i in range(len(gastos_extras)):
        if cidade == "Salvador":
            gasto = gastos_extras[0] * dias
        elif cidade == "Fortaleza":
            gasto = gastos_extras[1] * dias
        elif cidade == "Natal":
            gasto = gastos_extras[2] * dias
        else:
            gasto = gastos_extras[3] * dias
    total_gastos = gasto 
    return total_gastos

total_hotel = gasto_hotel(dias)
total_gasolina = gasto_gasolina(cidade, distancias)
total_gastos = gasto_passeio(cidade, dias, gastos_extras)
total_viagem = total_hotel + total_gasolina + total_gastos
print(f'Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {round(total_viagem, 2)} reais')
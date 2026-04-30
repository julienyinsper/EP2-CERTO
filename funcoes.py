# Q1
def rolar_dados(numero):
    lista = []
    for i in range(numero):
        lista.append(random.randint(1,6))
    return lista

# Q2
def guardar_dado(dados_rolados, dados_no_estoque, dados_a_guardar):
    dado = dados_rolados[dados_a_guardar]
    dados_no_estoque.append(dado)
    del dados_rolados[dados_a_guardar]
    return [dados_rolados, dados_no_estoque]

# Q3
def remover_dado(dados_rolados, dados_no_estoque, dados_a_remover):
    dado = dados_no_estoque[dados_a_remover]
    dados_rolados.append(dado)
    del dados_no_estoque[dados_a_remover]
    return [dados_rolados, dados_no_estoque]

# Q4
def calcula_pontos_regra_simples(dados):
    pontuacao = {}
    
    for face in range(1, 7):
        soma = 0
        for dado in dados:
            if dado == face:
                soma += dado
        pontuacao[face] = soma
    
    return pontuacao

# Q5
def calcula_pontos_soma(dados):
    soma = 0 
    for dado in dados:
        soma += dado
    return soma
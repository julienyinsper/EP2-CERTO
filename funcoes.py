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

# Q6
def calcula_pontos_sequencia_baixa(dados):
    dados_unicos = set(dados)
    
    if {1, 2, 3, 4}.issubset(dados_unicos):
        return 15
    elif {2, 3, 4, 5}.issubset(dados_unicos):
        return 15
    elif {3, 4, 5, 6}.issubset(dados_unicos):
        return 15
    else:
        return 0
    
# Q7
def calcula_pontos_sequencia_alta(dados):
    dados_unicos = set(dados)

    if {1, 2, 3, 4, 5}.issubset(dados_unicos):
        return 30
    elif {2, 3, 4, 5, 6}.issubset(dados_unicos):
        return 30
    else:
        return 0
    
# Q8
def calcula_pontos_full_house(dados):
    soma = 0
    for dado in dados:
        soma += dado

    contagens = {}
    for dado in dados:
        if dado in contagens:
            contagens[dado] += 1
        else:
            contagens[dado] = 1

    tem_3 = False
    tem_2 = False

    for quantidade in contagens.values():
        if quantidade == 3:
            tem_3 = True
        elif quantidade == 2:
            tem_2 = True

    if tem_3 and tem_2:
        return soma
    else:
        return 0
    
# Q9
def calcula_pontos_quadra(dados):
    soma = 0
    for dado in dados:
        soma += dado

    contagens = {}
    for dado in dados:
        if dado in contagens:
            contagens[dado] += 1
        else:
            contagens[dado] = 1

    for quantidade in contagens.values():
        if quantidade >= 4:
            return soma

    return 0

# Q10
def calcula_pontos_quina(dados):
    for valor in dados:
        if dados.count(valor) >= 5:
            return 50
    return 0

# Q11
def calcula_pontos_regra_avancada(dados):
    return {
        "cinco_iguais": calcula_pontos_quina(dados),
        "full_house": calcula_pontos_full_house(dados),
        "quadra": calcula_pontos_quadra(dados),
        "sequencia_alta": calcula_pontos_sequencia_alta(dados),
        "sequencia_baixa": calcula_pontos_sequencia_baixa(dados),
        "sem_combinacao": calcula_pontos_soma(dados)
    }
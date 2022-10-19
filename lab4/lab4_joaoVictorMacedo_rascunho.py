# Joao Victor Macedo Fernandes Ramos



#ex. 1

def SIGA (registro):
    '''retorna o resultado da média do aluno e se ele foi ou nao aprovado
       dado o nome dele e as 3 notas dado uma (str, float, float, flat)
       tuple -> tuple '''

    nome = registro[0]
    nota1 = registro[1]
    nota2 = registro[2]
    nota3 = registro[3]

    media = round((nota1+nota2+nota3)/3,1)
    mensagem = (nome, media)

    if media>=7:
        mensagem = (mensagem, 'aprovado', 'parabens!')
    elif media>=5:
        mensagem = (mensagem, 'aprovado',)
    else:
        mensagem = (mensagem, 'reprovado')
    return mensagem

# teste 1
# SIGA(('joao', 5.4, 3.4, 5.5)) 
# saída esperada: 'oi, tudo bem?'
# teste 2 
# SIGA(('maria', 7.4, 3.6, 0))
# saída esperada: 'um dois'
# teste 3
# SIGA(('jose', 2.45, 9.32, 10))
# saída esperada: 'o numeral de um é igual: 1'


#ex. 2

def signo (ano):
    '''retorna o signo do zodiaco chines dado o ano de nascimento de uma pessoa
       int -> float '''
    
    

    if ano>100:
        ano = str(ano)[2,4]
        ano = int(ano)
    else:
        ano = ano

    

    return ano/12

        
    

# teste 1
# SIGA(('joao', 5.4, 3.4, 5.5)) 
# saída esperada: 'oi, tudo bem?'
# teste 2 
# SIGA(('maria', 7.4, 3.6, 0))
# saída esperada: 'um dois'
# teste 3
# SIGA(('jose', 2.45, 9.32, 10))
# saída esperada: 'o numeral de um é igual: 1'



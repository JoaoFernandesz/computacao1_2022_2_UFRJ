# Joao Victor Macedo Fernandes Ramos

#ex. 1 a

def criaContatinhosApp (nome,listaTelefone=[],email='',instagram=''):
    '''resgitra todos os dados informados na função em uma lista, incluindo nome, 
       telefonem, email e instagram e retorna a lista
       string, list, string, string -> list'''

    listaTelefone = [''.join(listaTelefone)]
    contato1 = [nome,listaTelefone,email,instagram]
    return contato1

# teste 1
# contatinhosApp ('JOAO',['210897901'],'JOAOFER1999@gmail.com')
# saída esperada: ['JOAO', ['210897901'], 'JOAOFER1999@gmail.com', '']
# teste 2 
# contatinhosApp('victor')
# saída esperada: ['victor', [], '', '']
# teste 3
# contatinhosApp('macedo',['190238709'],'joaofernandes@ufrj','@joaovictorfernandes')
# saída esperada: ['macedo', ['190238709'], 'joaofernandes@ufrj', '@joaovictorfernandes']
# teste 4
# contatinhosApp('macedo','190238709','joaofernandes@ufrj','@joaovictorfernandes')
# saída esperada: ['macedo', ['190238709'], 'joaofernandes@ufrj', '@joaovictorfernandes']


#ex. 1 b

def atualizaContatinhosApp (contato1,indice,atualizacao):
    '''atualiza os dados da lista informada na função, podendo atualizar o nome(contato1[0]), 
       adicionar um telefone(contato1[0]), atualizar ou adicionar o email (contato1[0])
       ou atualizar ou adicionar o instagram(contato1[0]) e retorna o valor boleano se foi alterado ou nao
       list, int, string -> list'''
    
    
    if indice == 1 and atualizacao not in contato1[1]:
        atualizacao = [''.join(atualizacao)]
        contato1[1] = contato1[1] + atualizacao
        return indice == 1 and atualizacao != contato1
        
    elif indice == 0 or indice == 2 or indice == 3:
        contato1[indice] = atualizacao
        return indice == 0 or indice == 2 or indice == 3
        
    else:
        return atualizacao not in contato1[1]

# teste 1
# atualizaContatinhosApp(['JOAO', ['210897901'], 'JOAOFER1999@gmail.com', ''],0,'victor')
# saída esperada: True
# teste 2 
# atualizaContatinhosApp(['JOAO', ['210897901'], 'JOAOFER1999@gmail.com', ''],1,'21999008495')
# saída esperada: True
# teste 3
# atualizaContatinhosApp(['JOAO', ['210897901'], 'JOAOFER1999@gmail.com', ''],2,'joaofernandes@eufrj')
# saída esperada: True
# teste 4
# atualizaContatinhosApp(['JOAO', ['210897901'], 'JOAOFER1999@gmail.com', ''],3,'@joaovictorfernandes')
# saída esperada: True
# teste 5
# atualizaContatinhosApp(['JOAO', ['210897901'], 'JOAOFER1999@gmail.com', ''],1,['@21999008495'])
# saída esperada: True
# teste 6
# atualizaContatinhosApp(['JOAO', ['210897901'], 'JOAOFER1999@gmail.com', ''],1,'210897901')
# saída esperada: False
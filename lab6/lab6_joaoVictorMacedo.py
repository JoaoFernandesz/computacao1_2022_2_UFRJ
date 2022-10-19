# Joao Victor Macedo Fernandes Ramos

#ex. 1 a
def excluiContato (lista,telefone):
    '''exclui a informação de telefone de uma lista de contatos caso esse telefone esteja salvo 
       na lista, dado a lista(lista) e o telefone a ser excluido
       list -> list'''



    lista[1] = [''.join(lista[1])]
    telefone = [''.join(str(telefone))]
    
    
    
    if telefone in lista:
        lista_com_exclusao = lista[:]
        del lista_com_exclusao[1]
        return telefone in lista
        
    else:
        lista = lista
        return telefone in lista
   

# teste 1
# excluiContato (['JOAO','210897901','JOAOFER1999@gmail.com'],210897901)
# saída esperada: True
# teste 2
# excluiContato (['JOAO',['210897901'],'JOAOFER1999@gmail.com'],210897901)
# saída esperada: True
# teste 3
# excluiContato (['JOAO','210897901','JOAOFER1999@gmail.com'],'210897901')
# saída esperada: True
# teste 4
# excluiContato (['JOAO','210897901','JOAOFER1999@gmail.com','joaofernandes'],21999008495)
# saída esperada: False
# teste 4
# excluiContato (['JOAO',[],'JOAOFER1999@gmail.com'],210897901)
# saída esperada: False


#ex. 2

def campeonato (tabela):
    '''função que recebe os dados em dict de uma tabela do campeonato, com o nome dos time
       e a pontuação de cada time e retorna uma lista com o nome dos times, a pontuação do time campeão
       e a média de pontos
       dict{str:int}  -> list[list[str], int, float]'''
    
    times = list(dict.keys(tabela)) 
    resultados = list(dict.values(tabela))
    
    
    return times, max(resultados), sum(resultados) / len(times)
    

# teste 1
# campeonato({'vasco':3,'flamengo':6,'corinthias':9,'cruzeiro':12,'santos':10,'nova iguacu':7,'fluminense':8,'bangu':4,'botafogo':13})
# saída esperada: (['vasco', 'flamengo', 'corinthias', 'cruzeiro', 'santos', 'nova iguacu', 'fluminense', 'bangu', 'botafogo'], 13, 8.0)
# teste 2 
# campeonato({'vasco':0,'flamengo':1,'corinthias':2,'cruzeiro':100,'santos':1,'nova iguacu':2})
# saída esperada: (['vasco', 'flamengo', 'corinthias', 'cruzeiro', 'santos', 'nova iguacu'], 100, 17.666666666666668)
# teste 3
# campeonato({'vasco':3,'flamengo':6})
# saída esperada: (['vasco', 'flamengo'], 6, 4.5)
# teste 4
# campeonato({'vasco':3})
# saída esperada: (['vasco'], 3, 3.0)
# teste 5
# campeonato({'vasco':0})
# saída esperada: (['vasco'], 0, 0.0)



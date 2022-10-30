# Joao Victor Macedo Fernandes Ramos

#ex. 1 

import random

def dado ():
    '''retorna o número de vezes que o dado precisou ser rodado para 
       tirar dois números repetidos
       null -> int'''

    resultados = []
    vezesRodado = 0
    x=0

    while x == 0:
        resultado = random.randint(1, 6)
        if resultado not in resultados:
            resultados.append(resultado)
        else: 
            x=1
        vezesRodado = vezesRodado + 1
    return vezesRodado
   

# teste 1
# dado ()
# saída esperada: 2
# teste 2
# dado ()
# saída esperada: 5
# teste 3
# dado ()
# saída esperada: 3
# teste 4
# dado ()
# saída esperada: 3
# teste 4
# dado ()
# saída esperada: 4


#ex. 2

def contatinhosApp(contatos,busca):
    '''busca as informações do contato dado uma string referente ao nome do contato
        list[list[list,string]]  -> list[list,string]'''
        
    i=0
    contatosIndex = []
        
    while i < len(contatos):
        if busca in contatos[i][0]:
            contatosIndex.append(contatos[i])
        i=i+1
        
    return contatosIndex
           

# teste 1
# contatinhosApp([['Bruno Campos', ['2199112233', '2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields', ['2198145233'], '', '@juju.fields'] ],'u')
# saída esperada: [['Bruno Campos', ['2199112233', '2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields', ['2198145233'], '', '@juju.fields'] ]
# teste 2 
# contatinhosApp([['Bruno Campos', ['2199112233', '2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields', ['2198145233'], '', '@juju.fields'] ],'Bruno') 
# saída esperada: [['Bruno Campos', ['2199112233', '2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91']]
# teste 3
# contatinhosApp([['Bruno Campos', ['2199112233', '2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91'],['Julia Fields', ['2198145233'], '', '@juju.fields'],['joao Fernandes',['21999008495'],'joaofer1999@gmail.com','@joaofer'] ],'joao')
# saída esperada: [['joao Fernandes',['21999008495'],'joaofer1999@gmail.com','@joaofer'] ]
# teste 4
# contatinhosApp([['Bruno Campos', ['2199112233', '2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91'],['Julia Fields', ['2198145233'], '', '@juju.fields'],['joao fernandes',['21999008495'],'joaofer1999@gmail.com','@joaofer'],['fabio fernandes',['9999999'],'','']],'fernandes')
# saída esperada: [['joao fernandes',['21999008495'],'joaofer1999@gmail.com','@joaofer'],['fabio fernandes',['9999999'],'','']]
# teste 4
# contatinhosApp([['Bruno Campos', ['2199112233', '2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91'],['Julia Fields', ['2198145233'], '', '@juju.fields'],['joao fernandes',['21999008495'],'joaofer1999@gmail.com','@joaofer'],['fabio fernandes',['9999999'],'','']],'ramos')
# saída esperada: []



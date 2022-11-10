# Joao Victor Macedo Fernandes Ramos

# ex. 1


def multiplicaMatriz(matriz, num):
    """calcula a matriz resultante da multiplicação de uma matriz por um número
       dado a matriz e o número
       list[list[float]], float -> list[list[float]]"""

    matrizResultante = []

    for l in matriz:
        linhas = []
        for c in l:
            c = num*c
            linhas.append(c)
        matrizResultante.append(linhas)
    return matrizResultante



# teste 1
# multiplicaMatriz([ [1, 2, -1], [0, 3, 2] ],2)
# saída esperada: [ [2, 4, -2], [0, 6, 4] ]
# teste 2
# multiplicaMatriz([ [1, -1], [2, 0], [3, 2] ],2)
# saída esperada: [[2, -2], [4, 0], [6, 4]]
# teste 3
# multiplicaMatriz([[1,2,3],[2,1,4],[3,4,1]],2)
# saída esperada: [[2, 4, 6], [4, 2, 8], [6, 8, 2]]
# teste 4
# multiplicaMatriz([[1,2,3],[2,1,4],[3,4,1]],0)
# saída esperada: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# teste 5
# multiplicaMatriz([[1,2,3],[2,1,4],[3,4,1]],-1)
# saída esperada: [[-1, -2, -3], [-2, -1, -4], [-3, -4, -1]]
# teste 6
# multiplicaMatriz([[2,3],[2,1],[3,1]],2)
# saída esperada: [[4, 6], [4, 2], [6, 2]]
# teste 7
# multiplicaMatriz([[2],[4],[1]],10)
# saída esperada: [[20], [40], [10]]


# ex. 2

def deu_match(afinidades):
    """função que recebe um dicionario com as afinidades de cada pessoas
       e retorna tuplas de duas pessoas que correspondem essa afinidade
       list,tuple,str -> int"""

    participantes = afinidades.keys()
    matchs = []

    for participante in participantes:
        for curtiu in afinidades[participante]:
            if participante in afinidades[curtiu]:
                if match[::-1] not in matchs:
                    list.append(matchs, match)

    return match

# ex. 3

def quem_ligou(listaContatos, numero):
    """dado um número de telefone retorna quais contatos fazem uso desse
       telefone na agenda
       list[list,str],str -> list[list,str]"""

    contatosNum = []

    for contato in listaContatos:
        infos = []
        for informacao in contato:
            infos.append(informacao)
            if numero in infos:
                contatosNum.append(contato)
    return contatosNum


# teste 1
# quem_ligou([['Bruno Campos', ['2199112233', '2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields', ['2198145233'], '', '@juju.fields'] ],'2199112233')
# saída esperada: [['Bruno Campos', ['2199112233', '2133992211'], 'brunoc91@emailquente.com.br', '@brunocampos91']]
# teste 2 
# quem_ligou([['Bruno Campos', ['2199112233', '2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields', ['2199112233'], '', '@juju.fields'] ],'2199112233') 
# saída esperada: [['Bruno Campos', ['2199112233', '2133992211'], 'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields', ['2199112233'], '', '@juju.fields']]
# teste 3
# quem_ligou([['Bruno Campos', ['2199112233', '2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91'],['Julia Fields', ['2198145233'], '', '@juju.fields'],['joao Fernandes',['21999008495'],'joaofer1999@gmail.com','@joaofer'] ],'2199112230')
# saída esperada: []
# teste 4
# quem_ligou([['Bruno Campos', ['2199112233', '2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91'],['Julia Fields', ['2199112233'], '', '@juju.fields'],['joao fernandes',['2199112233'],'joaofer1999@gmail.com','@joaofer'],['fabio fernandes',['849495233'],'','']],'2199112233')
# saída esperada: [['Bruno Campos', ['2199112233', '2133992211'], 'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields', ['2199112233'], '', '@juju.fields'], ['joao fernandes', ['2199112233'], 'joaofer1999@gmail.com', '@joaofer']]
# teste 5
# quem_ligou([['Bruno Campos', ['2199112233', '2133992211'],'brunoc91@emailquente.com.br', '@brunocampos91'],['Julia Fields', ['2198145233', '2133992211'], '', '@juju.fields'],['joao fernandes',['21999008495'],'joaofer1999@gmail.com','@joaofer'],['fabio fernandes',['9999999'],'','']],'2133992211')
# saída esperada: [['Bruno Campos', ['2199112233', '2133992211'], 'brunoc91@emailquente.com.br', '@brunocampos91'], ['Julia Fields', ['2198145233', '2133992211'], '', '@juju.fields']]

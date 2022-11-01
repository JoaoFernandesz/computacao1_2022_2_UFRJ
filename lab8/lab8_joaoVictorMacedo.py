# Joao Victor Macedo Fernandes Ramos

# ex. 1


def repeticoes(iteravel, elem):
    """retorna a quantidade de vezes que elem aparece no valor iterável dado às duas variáveis
       list,tuple,str -> int"""

    contador = 0

    for valores in iteravel:
        if valores == elem:
            contador += 1
    return contador

# teste 1
# repeticoes((1,2,3,4,5,6,7,1,3,2,4,1,2,465,1), 1)
# saída esperada: 4
# teste 2
# repeticoes('joao victor macedo fernandes ramos', 'a')
# saída esperada: 4
# teste 3
# repeticoes(['joao',1.5,5123,1.5,'joao','janela',123],1.5)
# saída esperada: 2
# teste 4
# repeticoes(['joao',1.5,5123,1.5,'joao','janela',123],'joao')
# saída esperada: 2
# teste 5
# repeticoes('joao victor macedo fernandes ramos', 's')
# saída esperada: 2


# ex. 2

def repeticoes_inicio_fim(iteravel, elem, ini, fim):
    """retorna a quantidade de vezes que elem aparece no valor iterável dado essas duas variáveis
       mais às duas variáveis de início e fim dos índices
       list,tuple,str -> int"""

    contador = 0

    if fim > len(iteravel):
        fim = len(iteravel) + 1

    for indices in range(ini, fim+1):
        if elem == iteravel[indices]:
            contador += 1

    return contador

# teste 1
# repeticoes((1,2,3,4,5,6,7,1,3,2,4,1,2,465,1), 1,0,10)
# saída esperada: 2
# teste 2
# repeticoes('joao victor macedo fernandes ramos', 'a',1,14)
# saída esperada: 2
# teste 3
# repeticoes(['joao',1.5,5123,1.5,'joao','janela',123],1.5,0,2)
# saída esperada: 1
# teste 4
# repeticoes(['joao',1.5,5123,1.5,'joao','janela',123],'joao',2,5)
# saída esperada: 1
# teste 5
# repeticoes('joao victor macedo fernandes ramos', 's',0,3)
# saída esperada: 0
# teste 5
# repeticoes('joao victor macedo fernandes ramos', 's',0,40)
# saída esperada: 2


# ex. 3

def forca(palavra, mascara, letra):
    """retorna a atualização da forca dado a palavra a situação da máscara e a letra a ser
       adivinhada ou não
       string,list,str -> int"""

    indice = 0
    indices = []

    if letra not in mascara:
        return mascara
    else:
        for letras in palavra:
            if letra == letras:
                indices.append(indice)
        indice += 1

        for indice in indices:
            del mascara[indice]
            mascara.insert(indice, letra)

        return mascara


# teste 1
# atualiza_mascara('janela', ['j','-','-','e','l','-'],'a')
# saída esperada: ['j','a','-','e','l','a']
# teste 2
# atualiza_mascara('janela', ['j','-','-','e','l','-'],'n')
# saída esperada: ['j','-','n','e','l','-']
# teste 4
# atualiza_mascara('computador', ['c','-','m','p','u','t','a','d','-','r'],'o')
# saída esperada: ['c','o','m','p','u','t','a','d','o','r']
# teste 5
# atualiza_mascara('banana', ['b','-','-','-','-','-'],'a')
# saída esperada: ['b','a','-','a','-','a']
# teste 6
# atualiza_mascara('banana', ['b','a','-','a','-','a'],'n')
# saída esperada: ['b','a','n','a','n','a']
# teste 7
# atualiza_mascara('computador', ['c','-','m','p','u','t','a','d','-','r'],'w')
# saída esperada: ['c','-','m','p','u','t','a','d','-','r']

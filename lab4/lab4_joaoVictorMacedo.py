# Joao Victor Macedo Fernandes Ramos

#ex. 3

def telefone (numero):
    '''retorna uma tupla com o ddd(caso informado) e o número de telefone fixo ou telefone celular informado
       dado a informação do telefone em string(numero)
       string -> tuple '''
       
    numero = str(numero)   
       
    if len(numero) == 8:
        ddd_numero = ('', numero)
        
    elif len(numero) == 9:       
        ddd_numero = ('', numero)
        
    elif len(numero) == 10:
        ddd_numero = (numero[0:2], numero[2:10])
        
    elif len(numero) == 11:
        ddd_numero = (numero[0:2], numero[2:11])
    
    else:
        ddd_numero = ('', '')

    return ddd_numero

# teste 1
# telefone (2199900845)
# saída esperada: ('21', '99900845')
# teste 2 
# telefone (999008495)
# saída esperada: ('', '999008495')
# teste 3
# telefone (2126933713)
# saída esperada: ('21', '26933713')
# teste 4
# telefone (269233713)
# saída esperada: ('', '269233713')
# teste 5
# telefone ('2199900845')
# saída esperada: ('21', '99900845')
# teste 6
# telefone ('21999008423534265')
# saída esperada: ('', '')
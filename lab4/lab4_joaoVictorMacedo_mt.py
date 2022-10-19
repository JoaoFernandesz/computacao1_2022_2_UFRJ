def filtra_pares (t):
 '''retorna uma tupla com o ddd(caso informado) e o número de telefone fixo ou telefone celular informado
        dado a informação do telefone em string(numero)
        string -> tuple '''
    
    lista = []
     
         
    for i in t:
             
             if type(i) != int:
                 lista = []
                 return ('Todos os itens da tuplas devem ser inteiros.')
                 break
             elif i%2 == 0:
                  lista.append(i)
                  
             return tuple(lista)

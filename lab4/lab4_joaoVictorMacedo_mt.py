Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def filtra_pares (t):
...     '''retorna uma tupla com o ddd(caso informado) e o número de telefone fixo ou telefone celular informado
...        dado a informação do telefone em string(numero)
...        string -> tuple '''
...     lista = [] 
...     
...         
...     for i in t:
...             
...             if type(i) != int:
...                 lista = []
...                 return ('Todos os itens da tuplas devem ser inteiros.')
...                 break
...             elif i%2 == 0:
...                  lista.append(i)
...                  
...             return tuple(lista)

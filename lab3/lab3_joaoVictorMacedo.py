# Joao Victor Macedo Fernandes Ramos

from lab2_joaoVictorMacedo import discriminante

#ex. 1 

def numAbsoluto (a):
    '''defina o valor absoluto de números inteiros e fracionários dado o número
       int, float -> int, float'''
    if (a<0):
        return a*-1
    elif (a==0):
        return 0
    else:
        return a
# teste 1
# abs(2)
# numAbsoluto(2) 
# saída esperada: 2
# saída esperada: 2
# teste 2 
# abs(-2)
# numAbsoluto(-2)
# saída esperada: 2
# saída esperada: 2
# teste 3
# abs(5+0j)
# numAbsoluto(5+0j)
# saída esperada: ERRO
# saída esperada: 5


#ex. 2

def qntdRaizes (a,b,c):
    '''defina a quantidade de raizes dado os coeficientes da equacao de segundo grau(a,b,c)
       int, float -> str'''

    mensagem = 'o numero de raizes e '
    if (discriminante(a,b,c) > 0):
        mensagem = mensagem + '2'
    elif (discriminante(a,b,c)==0):
        mensagem = mensagem + str(1)
    else:
        mensagem = 'essa esquacao nao tem raizes'
    return mensagem

# teste 1
# qntdRaizes(3,4,2)
# saída esperada: 'essa esquacao nao tem raizes'
# teste 2 
# qntdRaizes(12,-3,4)
# saída esperada: 'o numero de raizes e 2'  
# teste 3
# qntdRaizes(-3,2,-7)
# saída esperada: 'essa esquacao nao tem raizes'


#ex. 3

def replicaString (n,t):
    '''retorna um texto(t) repetidas vezes por (n)
       int -> str'''
    return n*t

# teste 1
# replicaString(5,'Feliz Aniversario! ')
# saída esperada: 'Feliz Aniversario! Feliz Aniversario! Feliz Aniversario! Feliz Aniversario! Feliz Aniversario! '
# teste 2 
# replicaString(12,'cinco ')
# saída esperada: 'cinco cinco cinco cinco cinco cinco cinco cinco cinco cinco cinco cinco '
# teste 3
# replicaString(5,'5')
# saída esperada: '55555'


#ex. 4

def data (d,m,a):
    '''retorna uma string no padrao de data dado o dia(d), mes(m) e  ano(a)
       int -> str'''
    return str(a)+'/'+str(m)+'/'+str(a)

# teste 1
# data(28,9,1999)
# saída esperada: '28/9/1999'
# teste 2 
# data(27,10,1945)
# saída esperada: '27/10/1945'
# teste 3
# data(1,10,2022)
# saída esperada: '1/10/2022'


#ex. 5

def funcaoVariavel (x):
    '''retorna o y de uma funcao dado o x
       int, float -> int, float'''
    if (x<0):
        return 0
    elif (x<=2):
        return x
    elif (2<x<=3.5):
        return 2
    elif (3.5<x<=5):
        return 3
    else:
        return x*x-10*x+28     
    
# teste 1
# funcaoVariavel(0)
# saída esperada: 0
# teste 2 
# funcaoVariavel(1)
# saída esperada: 1
# teste 3
# funcaoVariavel(2.5)
# saída esperada: 2
# teste 4
# funcaoVariavel(4)
# saída esperada: 3
# teste 5
# funcaoVariavel(6)
# saída esperada: 4
# teste 6
# funcaoVariavel(-6)
# saída esperada: 0
# teste 7
# funcaoVariavel(3.5)
# saída esperada: 2
# teste 8
# funcaoVariavel(5)
# saída esperada: 3


#ex. 6 letra a

def salarioLiquidoInss (salarioBruto):
    '''retorna o valor do salario da uma pessoa com os descontos do INSS 
       dado o salario bruto dela
       int, float -> float, str'''
    if (salarioBruto<=0):
        return 'numero invalido'
    elif (salarioBruto<=2000):
        descontoInss=salarioBruto*0.06
    elif (salarioBruto<=3000):
        descontoInss=salarioBruto*0.08
    else:
        descontoInss=salarioBruto*0.1
        
    return salarioBruto-descontoInss
        
# teste 1
# salarioLiquidoInss(-200)
# saída esperada: 'numero invalido'
# teste 2 
# salarioLiquidoInss(1800)
# saída esperada: 1656.0
# teste 3
# salarioLiquidoInss(2200)
# saída esperada: 2024.0
# teste 4
# salarioLiquidoInss(8300)
# saída esperada: 7470.0


#ex. 6 letra b

def salarioLiquidoIr (salarioBruto):
    '''retorna o valor do salario da uma pessoa com os descontos do IR 
       dado o salario bruto dela
       int, float -> float, str'''
    if (salarioBruto<=0):
        return 'numero invalido'
    elif (salarioBruto<=2500):
        descontoIr=salarioBruto*0.11
    elif (salarioBruto<=5000):
        descontoIr=salarioBruto*0.15
    else:
        descontoIr=salarioBruto*0.22
        
    return salarioBruto-descontoIr
        
# teste 1
# salarioLiquidoIr(-200)
# saída esperada: 'numero invalido'
# teste 2 
# salarioLiquidoIr(2200)
# saída esperada: 1958.0
# teste 3
# salarioLiquidoIr(3500)
# saída esperada: 2975.0
# teste 4
# salarioLiquidoIr(5100)
# saída esperada: 3978.0


#ex. 6 letra c

def salarioLiquido (salarioBruto):
    '''retorna o valor do salario liquido de uma pessoa dado o salario bruto dela
       int, float -> float, str'''
    descontoInss=salarioBruto-salarioLiquidoInss(salarioBruto)
    descontoIr=salarioBruto-salarioLiquidoIr(salarioBruto)
  
    return salarioBruto-descontoInss-descontoIr

# teste 1
# salarioLiquido(1800)
# saída esperada: 1494.0
# teste 2 
# salarioLiquido(2200)
# saída esperada: 1782.0
# teste 3
# salarioLiquido(2600)
# saída esperada: 2002.0
# teste 4
# salarioLiquido(3100)
# saída esperada: 2325.0
# teste 5
# salarioLiquido(5400)
# saída esperada: 3672.0
# Joao Victor Macedo Fernandes Ramos

import math

#ex. 1 letra b

def media (a,b,c):
    '''defina a média de 3 números 
       float, float -> float float'''
    return (a+b+c)/3

# teste 1
# media(5,7,3) 
# saída esperada: 5
# teste 2 
# media(15,2,7)
# saída esperada: 8
# teste 3
# media(500,700,250)
# saída esperada: 483.3333333333333
# teste 4
# media(5,0,7)
# saída esperada: 4


#ex. 1 letra c

def diferanca_MaiorMedia (a,b,c):
    '''defina a diferença do maior número da média pela a média 
       float, float -> float float'''
    return (max(a,b,c))-(media(a, b, c))

# teste 1
# diferanca_MaiorMedia(5,7,3) 
# saída esperada: 2
# teste 2 
# diferanca_MaiorMedia(15,2,7)
# saída esperada: 7
# teste 3
# diferanca_MaiorMedia(500,700,250)
# saída esperada: 216.66666666666669
# teste 4
# diferanca_MaiorMedia(5,0,7)
# saída esperada: 3


#ex. 1 letra d

def soma_MenorMedia (a,b,c):
    '''defina a média de 3 números 
       float, float -> float'''
    return (min(a,b,c))+(media(a, b, c))

# teste 1
# soma_MenorMedia(5,7,3) 
# saída esperada: 8
# teste 2 
# soma_MenorMedia(15,2,7)
# saída esperada: 10
# teste 3
# soma_MenorMedia(500,700,250)
# saída esperada: 733.3333333333333
# teste 4
# soma_MenorMedia(5,0,7)
# saída esperada: 4


#ex. 2 letra a

def discriminante (a,b,c):
    '''define o delta da uma equação dados os coeficientes a, b, c
       float, float -> float'''
    return b^2-4*a*c

# teste 1
# discriminante(-5,7,3) 
# saída esperada: 57
# teste 2 
# discriminante (-15,2,7)
# saída esperada: 420
# teste 3
# discriminante(-500,700,250)
# saída esperada: 500638
# teste 4
# discriminante(-5,0,7)
# saída esperada: 142


#ex. 2 letra b

def primeiraRaiz (a,b,c):
    '''defina a primeira raizes de um polinomio dados os coeficientes a, b, c
       float, float -> float'''
    return -b+math.sqrt(discriminante(a,b,c))/2*a
    

# teste 1
# primeiraRaiz(-5,7,3) 
# saída esperada: -25.874586088176876
# teste 2 
# primeiraRaiz(15,2,-7)
# saída esperada: 151.70426148939396
# teste 3
# primeiraRaiz(-500,700,250)
# saída esperada: -177589.4428732252
# teste 4
# primeiraRaiz(5,0,-7)
# saída esperada: 29.79093821953246


#ex. 2 letra c

def segundaRaiz (a,b,c):
    '''defina a segunda raizes de um polinomio dados os coeficientes a, b, c
       float, float -> float'''
    return -b-math.sqrt(discriminante(a,b,c))/2*a
    

# teste 1
# segundaRaiz(-5,7,3) 
# saída esperada: 11.874586088176876
# teste 2 
# segundaRaiz(15,2,-7)
# saída esperada: -155.70426148939396
# teste 3
# segundaRaiz(-500,700,250)
# saída esperada: 176189.4428732252
# teste 4
# segundaRaiz(5,0,-7)
# saída esperada: -29.79093821953246


#ex. 3 letra b 

def numeroTermos (a1,an,r):
    '''define o número de termos de uma PA dados o valor final(an), valor inicial(a1) e a razao(r)
       float, float -> float'''
    return ((an-a1)/r)+1
    

# teste 1
# numeroTermos(5,7,3) 
# saída esperada: 1.6666666666666665
# teste 2 
# numeroTermos(15,2,7)
# saída esperada: -0.8571428571428572
# teste 3
# numeroTermos(500,700,250)
# saída esperada: 1.8
# teste 4
# numeroTermos(5,0,7)
# saída esperada: 0.2857142857142857


#ex. 3 letra c

def somaPa (a1,an,r):
    '''define o soma de uma PA dados o valor final(an), valor inicial(a1) e a razao(r)
       float, float -> float'''
    return (a1+an)*numeroTermos(a1,an,r)/2
    

# teste 1
# somaPa(5,7,3) 
# saída esperada: 10
# teste 2 
# somaPa(15,2,7)
# saída esperada: -7.2857142857142865
# teste 3
# somaPa(500,700,250)
# saída esperada: 1080.0
# teste 4
# somaPa(5,0,7)
# saída esperada: 0.7142857142857142


#ex. 4 letra a

def distanciaCoordenadas (x1,y1,x2,y2):
    '''define a distância entre duas coordenadas dados as coordenadas(x1,y1,x2,y2)
       float, float -> float'''
    return math.sqrt((x2-x1)^2*(y2-y1)^2)
    

# teste 1
# distanciaCoordenadas(5,7,-5,-7) 
# saída esperada: 4.0
# teste 2 
# distanciaCoordenadas(15,2,-55,-23)
# saída esperada: 10.862780491200215
# teste 3
# distanciaCoordenadas(500,700,250,-400)
# saída esperada: 46.4327470649756
# teste 4
# distanciaCoordenadas(5,0,6,2)
# saída esperada: 2.6457513110645907


#ex. 4 letra b

def perimetroTrianguloRetangulo (c1,c2):
    '''define o perimêtro de um triângulo retângulo dados os catetos(c1,c2)
       float, float -> float'''
    return c1+c2+math.sqrt(c1^2+c2^2)
    

# teste 1
# perimetroTrianguloRetangulo(5,7) 
# saída esperada: 15.74165738677394
# teste 2 
# perimetroTrianguloRetangulo(15,2)
# saída esperada: 20.0
# teste 3
# perimetroTrianguloRetangulo(500,700)
# saída esperada: 1228.9827534923788
# teste 4
# perimetroTrianguloRetangulo(5,1)
# saída esperada: 8.0


#ex. 4 letra c

def somaTrigonometrica (a):
    '''define o perimêtro de um triângulo retângulo dados os catetos(c1,c2)
       float, float -> float'''
    return math.sin(a)**2+math.cos(a)**2
    

# teste 1
# somaTrigonometrica(180)
# saída esperada: 0.9999999999999998
# teste 2 
# somaTrigonometrica(45)
# saída esperada: 1
# teste 3
# somaTrigonometrica(60)
# saída esperada: 1
# teste 4
# somaTrigonometrica(90)
# saída esperada: 1


#ex. 5

def areaSetorCircula (r,a=360):
    '''define a ́area de um setor circular dados o raio(r) e o ângulo(a).
       float, float -> float'''
    return r**2*math.radians(a)
    

# teste 1
# areaSetorCircula(5) 
# saída esperada: 157.07963267948966
# teste 2 
# areaSetorCircula (15,90)
# saída esperada: 353.4291735288517
# teste 3
# areaSetorCircula(700)
# saída esperada: 3078760.8005179972
# teste 4
# areaSetorCircula(5,45)
# saída esperada: 19.634954084936208

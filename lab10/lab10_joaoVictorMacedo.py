# Joao Victor Macedo Fernandes Ramos

# ex. 2

"""programa que le um código número em um intervalo de 1 a 4 e três valores inteiros e positivos.
   e calcula um resultado dependente do i informado"""

i = int(input("informe um número de um a quatro: "))
a = int(input("informe um número inteiro e positivo: "))
b = int(input("informe um número inteiro, positivo e maior que o anterior: "))
c = int(input("informe um número inteiro e positivo: "))


def um():
    resultado = ((a + b)*c)/2
    print(f'a={a}',f'b={b}',f'c={c}',f'i={i}')
    print(resultado)


def dois():
    resultado1 = a*a
    resultado2 = b*b
    resultado3 = c*c
    print(f'a={a}',f'b={b}',f'c={c}',f'i={i}')
    print(resultado1, resultado2, resultado3)
    

def tres():
    resultado = (a + b + c)/3
    print(f'a={a}',f'b={b}',f'c={c}',f'i={i}')
    print(resultado)


def quatro():
    x = a
    lista = [a,]
    while x <= b:
        x += c
        if x <= b:
            lista.append(x)
    resultado = sum(lista)4
    print(f'a={a}',f'b={b}',f'c={c}',f'i={i}')
    print(resultado)

if i == 1:
    um()
elif i == 2:
    dois()
elif i == 3:
    tres()
elif i == 4:
    quatro()

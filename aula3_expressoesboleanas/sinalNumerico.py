def sinalNumerico(x):  

    mensagem = 'o numero é '
    if (x>0):
        mensagem = mensagem + 'positivo'
    elif (x<0):
        mensagem = mensagem + 'negativo'
    else:
        mensagem = mensagem + 'zero'
    return mensagem
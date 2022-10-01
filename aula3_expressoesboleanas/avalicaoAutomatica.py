def msg_avaliacao(media):

    mensagem = 'o aluno foi '
    if (0<=media<5<10):
        mensagem = mensagem + 'reprovado'
    elif (0<5<=media<=10):
        mensagem = mensagem + 'aprovado'
    else:
        mensagem = 'numero invalido'
    return mensagem

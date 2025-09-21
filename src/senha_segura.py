# TODO: Trocar o módulo random por secrets, que é o módulo especilizado para 
# geração de números aleátorios seguros.


from random import randrange
import caracteres_senha as caractere


def gerar_senha_segura(tam_senha=16):
    """A função tem um objetivo claro, gerar senhas seguras. Para essa função, 
    senhas seguras são as que atendem algums requisitos, são eles:
    - Deve ter letras maiúsculas e minúsculas
    - Deve ter números
    - Deve ter caracteres especiais
    - Deve ter no mínimo 8 (oito) caracteres e no maxímo 16
    - Não pode ter sequências, como '123' e nem repetição de sequências, como 
    'xn#nxn#n'

    Return:
    Retorna uma string (texto)
    """

    senha_segura = ""
    
    TAM_MINIMO = 8
    TAM_MAXIMO = 16

    if tam_senha == TAM_MINIMO or tam_senha == TAM_MAXIMO:
        intervalo = len(caractere.caracteres)
        while len(senha_segura) <= tam_senha:
            num_aleatorio = randrange(intervalo)
            senha_segura += caractere.caracteres[num_aleatorio]
        return senha_segura 
    else:
        return

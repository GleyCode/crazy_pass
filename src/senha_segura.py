#!/usr/bin/env python3

from sys import argv
import string
import secrets


conj_caracteres = string.ascii_letters + string.digits + string.punctuation


def gerar_senha_segura(tam_senha=16):
    """Gera senhas seguras de 8 e 16 caracteres. Usando o módulo secrets para
    gerar senhas com um nível de segurança superior se comparado com a geração de números pseudoaletorios com o módulo Random."""

    TAM_MINIMO = 8
    TAM_MAXIMO = 16

    senha = ""

    if tam_senha == TAM_MINIMO or tam_senha == TAM_MAXIMO:
        while len(senha) <= tam_senha:
            senha += secrets.choice(conj_caracteres)    
    return senha


if __name__ == "__main__":
    try:
        senha_segura = gerar_senha_segura(int(argv[1]))
    except IndexError:
        print("""O programa necessita do tamanho da senha para funcionar!\nPor favor, execute novamente.""")
        exit()
    print(senha_segura)
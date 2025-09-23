#!/usr/bin/env python3

from sys import argv
from string import ascii_letters, digits, punctuation
import secrets

CARACTERES = ascii_letters + digits + punctuation

def gerar_senha_segura(tam_senha=16):
    """Gera senhas seguras de 8 e 16 caracteres utilizando o módulo secrets e 
    string.
    """

    TAM_MINIMO = 8
    TAM_MAXIMO = 16

    senha = ""

    if tam_senha == TAM_MINIMO or tam_senha == TAM_MAXIMO:
        while len(senha) <= tam_senha:
            senha += secrets.choice(CARACTERES)    
    return senha


if __name__ == "__main__":
    try:
        senha_segura = gerar_senha_segura(int(argv[1]))
    except IndexError:
        print("O programa necessita do tamanho da senha para funcionar!")
        print("Por favor, execute novamente.")
        exit()
    print(senha_segura)
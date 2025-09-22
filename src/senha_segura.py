#!/usr/bin/env python3

# TODO: Trocar o módulo random por secrets, que é o módulo especilizado para 
# geração de números aleátorios seguros.
from random import randrange
from sys import argv

TAM_MINIMO = 8
TAM_MAXIMO = 16

caracteres = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z', 
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z', 
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '%', '#', 
              '&', '$', '!')

def gerar_senha_segura(tam_senha=16):
    """Gera senhas seguras de 8 e 16 caracteres."""

    senha = ""

    if tam_senha == TAM_MINIMO or tam_senha == TAM_MAXIMO:
        intervalo_index = len(caracteres)

        while len(senha) <= tam_senha:
            index = randrange(intervalo_index)
            senha += caracteres[index]    

    return senha

senha_segura = gerar_senha_segura(int(argv[1]))
print(senha_segura)

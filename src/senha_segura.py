#!/usr/bin/env python3

"""
Este módulo contem uma classe capaz de gerar senhas seguras seguindo os 
pilares da geração de senhas seguras, como a entropia, um conjunto de 
caracteres extenso e diverso e um módulo para seleção segura dos caracteres de 
forma aleatória.
"""

from sys import argv
from string import ascii_letters, digits, punctuation
import secrets


class GeradorSenha():
    """A classe implementa um gerador de senhas seguras."""
    
    @staticmethod
    def gerar_senha_segura(tam_senha=16):
        """Gere senhas seguras.
        
        As senhas tem tamanho de 8 e 16 caracteres e são geradas utilizando os  
        caracteres e dígitos do módulo string e escolhidas de forma aleatória 
        por secrets.
        
        Contantes:
            CARACTERES: O conjunto de caracteres, tendo letras, dígitos e 
                        sinais de pontuação.
            TAM_MINIMO: Tamanho minímo da senha (8 caracteres).
            TAM_MAXIMO: Tamanho maxímo da senha (16 caracteres).
            
        Variáveis:
            senha: A senha gerada; inicialmente uma string vazia.
        """
        CARACTERES = ascii_letters + digits + punctuation
    
        TAM_MINIMO = 8
        TAM_MAXIMO = 16
        
        senha = ""

        if tam_senha == TAM_MINIMO or tam_senha == TAM_MAXIMO:
            while len(senha) <= tam_senha:
                senha += secrets.choice(CARACTERES)    
        return senha


if __name__ == "__main__":
    try:
        senha_segura = GeradorSenha.gerar_senha_segura(int(argv[1]))
    except IndexError:
        print("O programa necessita do tamanho da senha para funcionar!")
        print("Por favor, execute novamente.")
        exit()
    print(senha_segura)
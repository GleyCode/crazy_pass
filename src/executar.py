from sys import argv
import senha_segura

# TODO: A função ARGV não está coletando o valor digitando no terminal, 
# refazer. 
def executar_senha_segura1M(tam_senha=argv[1]):
    """Executa a função geradora de senhas seguras."""
    for i in range(100000000):
        print(senha_segura.gerar_senha_segura(int(tam_senha)))


executar_senha_segura1M()

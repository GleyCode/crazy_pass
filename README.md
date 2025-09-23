# crazy_pass
Veja como uma função simples escrita em Python pode gerar senhas seguras.

# Entendendo a lógica do **crazy_pass**
O **crazy_pass** observa três pilares para geração de senhas seguras.

* Duração da senha
* Entropia
* Conjunto de caracteres

## Duração da senha
As senhas atualmente seguem um padrão de duração longa. Duração é o tamanho da senha definido pelo utilizador de
um determinado sistema. Quanto maior for a duração, menor é a probabilidade de um cybercriminoso conseguir
comprometer a senhar por meio de técnicas como, força bruta, preenchimento de credenciais e adivinhação de senhas.

O módulo **crazy_pass** define dois tipos de duração:
8 caracteres e 16 caracteres.

Se na execução do programa for informado um valor diferente para a duração, a função responsável por gerar a senha
retornará uma string vazia.

## Conjunto de caracteres
O conjunto de caracteres é a base de dados que será usado para compor a senha. No caso do **crazy_pass** o 
tamanho é de 68 caracteres. Além disso é importante que o conjunto de caracteres seja bem diversificado, 
contendo letras maiúsculas, minúsculas, números e caracteres especiais.

## Entropia
A entropia é o cálculo que determina o quão dificil é para um cibercriminoso quebrar a senha utilizando
várias técnicas para isso.

A formúla é a seguinte:
```
H = LOG2 (N**L)
```
* _**H**_:---É o resultado da entropia
* _**N**_:---É o tamanho do conjunto de caracteres que será usado
* _**L**_:---É o tamanho da senha (duração)

# Exemplo de saída
Abaixo é possível ver dois exemplos de saída para o **crazy_pass**.

Tamanho | Resultado
:--------:|-----------
8       | b7daiLinZ
16      | RX!@!?#93,pJH9Ybj


# Como executar

1. Clone o repositório do projeto
~~~shell
git clone https://github.com/GleyCode/crazy_pass.git
~~~
2. Execute o módulo principal
~~~shell
# Gera uma senha de 8 caracteres
python senha_segura.py 8
~~~
~~~shell
# Gera uma senha de 16 caracteres
python senha_segura.py 16
~~~

# ATENÇÃO!
**crazy_pass** é um gerador de senha segura SIMPLES, portanto não conta com verificação de _unicidade_, ou seja,
é plenamente possível que duas senhas iguais sejam geradas em momentos diferentes.

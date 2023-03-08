# Para a resolução desse exercício, definiremos um algorítmo para dizer o que é um fibonacci e outro para verificar se o número valor inserido faz parte da sequência.

# De forma recursiva, o algoritmo do fibonacci receberá um valor. Caso ele seja menor ou igual a 1, será retornado ele mesmo. Caso não, esse mesmo algorítmo retornará a soma do (valor - 1) com o (valor - 2)
def fibonacci(valor):
    if valor <= 1:
        return valor
    else:
        return fibonacci(valor - 1) + fibonacci(valor - 2)

# Para a verificação, precisaremos do número recebido e a posição dele no fibonacci para assim criarmos as condições.
# Se o valor do item de fibonacci na posição estabelecida no parâmetro for maior do que o valor do  número, isso quer dizer que ultrapassou a chance desse número ser um fibonacci, então será retornado Falso.
# Se o valor do item de fibonacci na posição estabelecida no parâmetro for igual ao valor do número, quer dizer que encontramos o número. Retornará Verdadeiro.
# Caso o valor do número seja menor do que o valor na posição estabelecida, então quer dizer que ainda há mais número para percorrer. Sabendo disso, será retornado novamente o programa de verificação, agora com uma posição a mais.
def verificarFibonacci(numero, posicao = 0):
    if fibonacci(posicao) > numero:
        return False
    elif fibonacci(posicao) == numero:
        return True
    else:
        return verificarFibonacci(numero, (posicao + 1))

# Com os algorítmos craidos, agora receberemos o valor e faremos a verificação.
valor = int(input("Digite um valor numérico: "))
if verificarFibonacci(valor) == True:
    print("O número informado pertence a sequência.")
else:
    print("O número informado não pertence a sequência.")
# Em python, a manipulação de strings é bem simplificada, inclusive na forma com que ela vai ser printada. Como a string é tratada como um conjunto de caractéres, python permite que um texto seja tratado como uma lista, podendo abrir colchetes e definir por onde começar a ler, por onde terminar a ler e a razão para definir de quantas em quantas casas deve ser pulado para ser feita a leitura.
# No algorítmo de inversão, precisamos apenas dizer que não vamos pular casas, mas voltar -1.
def inverteTexto(texto):
    return print(texto[::-1])

texto = str(input("Insira um texto a ser invertido: ")).strip()
inverteTexto(texto)
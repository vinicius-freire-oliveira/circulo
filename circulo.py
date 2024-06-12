# Definindo a constante Pi
Pi = 3.14159

# Função para calcular a área de um círculo
def area(raio):
    # Calcula e retorna a área do círculo usando a fórmula A = πr²
    return Pi * (raio ** 2)

# Função para calcular o comprimento da circunferência
def comprimento_circunferencia(raio):
    # Calcula e retorna o comprimento da circunferência usando a fórmula C = 2πr
    return 2 * Pi * raio

# Imprime o valor de Pi
print("Pi =", Pi)

# Exemplos de uso das funções
raio = 5
print("Área do círculo com raio", raio, ":", area(raio))
print("Comprimento da circunferência com raio", raio, ":", comprimento_circunferencia(raio))


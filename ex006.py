import math

# Função para verificar se um número é inteiro
def verificar_inteiro(numero):
    try:
        int_num = int(numero)
        return int_num
    except ValueError:
        return None

# Função principal que solicita 5 números inteiros e realiza os cálculos
def realizar_calculos():
    variaveis = []
    
    while len(variaveis) < 5:
        numero_digitado = input(f"Digite o número {len(variaveis) + 1}: ")
        numero = verificar_inteiro(numero_digitado)
        
        if numero is not None:
            variaveis.append(numero)
        else:
            print("Número inválido. Por favor, digite um número inteiro.")
    
    # Atribuir valores às variáveis
    A, B, C, D, E = variaveis
    
    # 1) Calcular e imprimir a área do triângulo
    area_triangulo = 0.5 * B * C
    print(f"A área do triângulo com base {B} e altura {C} é: {area_triangulo}")
    
    # 2) Calcular e imprimir o perímetro do retângulo
    perimetro_retangulo = 2 * (A + B)
    print(f"O perímetro do retângulo com largura {A} e altura {B} é: {perimetro_retangulo}")
    
    # 3) Calcular e imprimir a área do círculo
    area_circulo = math.pi * E**2
    print(f"A área do círculo com raio {E} é: {area_circulo:.2f}")

# Chamar a função principal
realizar_calculos()
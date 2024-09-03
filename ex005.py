# Função para verificar se um número é inteiro
def verificar_inteiro(numero):
    try:
        int_num = int(numero)
        return int_num
    except ValueError:
        return None

# Função principal que solicita 5 números inteiros, calcula a soma e o produto
def solicitar_numeros_e_calcular():
    numeros_inteiros = []
    
    while len(numeros_inteiros) < 5:
        numero_digitado = input(f"Digite o número {len(numeros_inteiros) + 1}: ")
        numero = verificar_inteiro(numero_digitado)
        
        if numero is not None:
            numeros_inteiros.append(numero)
        else:
            print("Número inválido. Por favor, digite um número inteiro.")
    
    soma_total = sum(numeros_inteiros)
    produto_total = 1
    for numero in numeros_inteiros:
        produto_total *= numero

    print(f"A soma dos 5 números inteiros digitados é: {soma_total}")
    print(f"O produto dos 5 números inteiros digitados é: {produto_total}")

# Chamar a função principal
solicitar_numeros_e_calcular()
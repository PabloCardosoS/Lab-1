# Função para verificar se um número é um valor numérico válido
def verificar_numero(valor):
    try:
        num = float(valor)
        return num
    except ValueError:
        return None

# Função principal que solicita as notas e calcula a nota final
def calcular_nota_final():
    notas = {'trabalho': 0.1, 'prova': 0.6, 'teste': 0.3}
    notas_obtidas = {}
    
    for avaliacao, peso in notas.items():
        while True:
            nota_digitada = input(f"Digite a nota para {avaliacao} (0 a 10): ")
            nota = verificar_numero(nota_digitada)
            
            if nota is not None and 0 <= nota <= 10:
                notas_obtidas[avaliacao] = nota
                break
            else:
                print("Nota inválida. Por favor, digite um valor numérico entre 0 e 10.")
    
    # Calcular a nota final com base nos pesos
    nota_final = (notas_obtidas['trabalho'] * notas['trabalho'] +
                  notas_obtidas['prova'] * notas['prova'] +
                  notas_obtidas['teste'] * notas['teste'])
    
    print(f"A nota final do aluno é: {nota_final:.2f}")

# Chamar a função principal
calcular_nota_final()
# Função para solicitar e validar a nota
def solicitar_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Função para calcular o grau A
def calcular_grau_a(atividade_pratica, atividade_teorica):
    grau_a = (atividade_pratica * 0.45) + (atividade_teorica * 0.55)
    return grau_a

# Função para calcular o grau B
def calcular_grau_b(prova, teste_teorico, trabalho_extraclasse):
    grau_b = (prova * 0.60) + (teste_teorico * 0.20) + (trabalho_extraclasse * 0.20)
    return grau_b

# Função para calcular a nota final
def calcular_nota_final(grau_a, grau_b):
    nota_final = (grau_a * 0.33) + (grau_b * 0.67)
    return nota_final

# Solicitando as notas do usuário com validação
atividade_pratica = solicitar_nota("Digite a nota da atividade prática (Grau A): ")
atividade_teorica = solicitar_nota("Digite a nota da atividade teórica (Grau A): ")
prova = solicitar_nota("Digite a nota da prova (Grau B): ")
teste_teorico = solicitar_nota("Digite a nota do teste teórico (Grau B): ")
trabalho_extraclasse = solicitar_nota("Digite a nota do trabalho extraclasse (Grau B): ")

# Calculando o grau A e o grau B
grau_a = calcular_grau_a(atividade_pratica, atividade_teorica)
grau_b = calcular_grau_b(prova, teste_teorico, trabalho_extraclasse)

# Calculando a nota final
nota_final = calcular_nota_final(grau_a, grau_b)

# Determinando se o aluno foi aprovado ou não
status = "Aprovado" if nota_final >= 6.0 else "Reprovado"

# Imprimindo a nota final e o status de aprovação
print(f"A nota final obtida na disciplina é: {nota_final:.2f}")
print(f"Status: {status}")


# Exercício 1

import random

resultados = []

for i in range(1 , 101):
    resultado = random.randint(1 , 6)
    resultados.append(resultado)

contadores = [0, 0, 0, 0, 0, 0 ]

for resultado in resultados:
    contadores[resultado - 1] += 1

for i, contagem in enumerate(contadores):
    print(f"Número {i + 1} foi obtido {contagem} vezes!")




# Exercício 2

import json

def ler_dados_aluno():
    matricula = input("Digite a matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    return matricula, nome, email

dados_alunos = {}

while True:
    matricula, nome, email = ler_dados_aluno()
    dados_aluno = {
        "nome": nome,
        "e-mail": email
    }
    dados_alunos[matricula] = dados_aluno

    continuar = input("Deseja adicionar outro aluno? (S/N): ").strip().lower()
    if continuar != 's':
        break

with open('alunos.json', 'w') as arquivo_json:
    json.dump(dados_alunos, arquivo_json, indent=4)




# Exercício 3

from datetime import datetime


def main(data):
    try:
        data = datetime.strptime(data, "%d/%m/%Y")
        data_ajust = data.strftime("%d de %B de %Y")
        return data_ajust
    except ValueError:
        return None


print(main("13/1/2003"))



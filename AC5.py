
# Exercício 1

def imprime_sequencia_numeros(num):
    for i in range(1, num + 1):
        print(" ".join(str(j) for j in range(1, i + 1)))
        
num = int(input("Digite um número inteiro: "))
imprime_sequencia_numeros(num)


# Exercício 2

def quantidade_digitos(num):
    num = str(num)
    print(len(num))

quantidade_digitos()


# Exercício 3

def divisao():
    while True:
        try:
            num1 = int(input("Digite o primeiro número inteiro: "))
            num2 = int(input("Digite o segundo número inteiro: "))
            resultado = num1 / num2
            print(resultado)  
            break 

        except ZeroDivisionError:
            print("Divisão inválida! Tente novamente... ")


divisao()


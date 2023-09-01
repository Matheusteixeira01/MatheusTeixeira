
# Exercício 1

sal = float(input("Informe o valor da sua hora de trabalho: "))
horas = int(input("Informe quantas horas você trabalha em um mês: "))

def main1(sal, horas):
    sal_total = sal * horas
    return sal_total

print(f"O salário total que você deve receber é: {main1(sal, horas)}")


# Exercício 2

num1 = int(input("Informe o primeiro número inteiro: "))
num2 = int(input("Informe o segundo número inteiro: "))
num3 = int(input("Informe o terceiro número inteiro: "))

def main2(num1, num2, num3):
    cont1 = (num1 * 2) * (num2 / 2)
    cont2 = (num1 * 3) + num3
    cont3 = num3 ** 3
    print(f"(1): {cont1}")
    print(f"(2): {cont2}")
    print(f"(2): {cont3}")

main2(num1, num2, num3)


# Exercício 3

n1 = int(input("Informe o primeiro número inteiro: "))
n2 = int(input("Informe o segundo número inteiro: "))
n3 = int(input("Informe o terceiro número inteiro: "))

def main3(n1, n2, n3):
    cal1 = (n1 * 2) * (n2 / 2)
    cal2 = (n1 * 3) + n3
    cal3 = n3 ** 3
    return (cal1, cal2, cal3)

print(main3(n1, n2, n3))


# Exercício 4

ano = int(input("Insira um ano: "))

def main4(ano):
    bi = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
    return bi

print(main4(ano))














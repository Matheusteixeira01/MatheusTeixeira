
# Exercício 1

def reajuste(salario):
    if salario <= 280:
        aumento = 0.2
    elif salario <= 700:
        aumento = 0.15
    elif salario <= 1500:
        aumento = 0.1
    else:
        aumento = 0.05

    valor_aumento = salario * aumento
    salario_ajustado = salario + valor_aumento
    porcentagem = aumento * 100

    print(f"Salário inicial: R${salario}\nPorcentagem de aumento: {porcentagem}%\nAumento: R${valor_aumento}\nSalário ajustado: {salario_ajustado}\n\n")

reajuste(200)
reajuste(500)
reajuste(1000)
reajuste(2000)



# Exercício 2
def dia(num):
    if num == 1:
        print("Domingo\n")
    elif num == 2:
        print("Segunda\n")
    elif num == 3:
        print("Terça\n")
    elif num == 4:
        print("Quarta\n")
    elif num == 5:
        print("Quinta\n")
    elif num == 6:
        print("Sexta\n")
    elif num == 7:
        print("Sábado\n")
    else:
        print("Valor inválido\n")

dia(1)
dia(5)
dia(3)
dia(10)


# Exercício 3
def eq(a, b ,c):
    if a == 0:
        return "Esta não é uma equação do 2° grau"
    delta = (b**2) - (4*a*c)
    raiz1 = (-b + delta ** (1/2)) / (2 * a) 
    raiz2 = (-b - delta ** (1/2)) / (2 * a) 

    if delta < 0:
        return "Não há raízes reais"
    elif delta == 0:
        return raiz1
    elif delta > 0:
        return raiz1, raiz2

print(eq(0, 2, 3))
print(eq(1, 0, 4))
print(eq(1, -3, 0))
print(eq(1, -14, 49))










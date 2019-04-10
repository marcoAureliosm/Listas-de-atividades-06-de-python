def soma_intervalo(a,b):
    soma = 0
    for i in range(a,b+1):
        soma += i
    return soma

n1 = int(input("\nDigite o primeiro número: "))
n2 = int(input("\nDigite o segundo  número: "))
print("A soma do intervalo informado é ", soma_intervalo(n1,n2))
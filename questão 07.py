def fatorial(f):
    fat = 1
    for i in range (1,f+1):
        fat = fat * i
    return fat

num = int(input("Digite um número: "))
print("O fatorial de {} é: {}" .format(num, fatorial(num)))

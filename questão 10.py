def max(a, b):
    if a > b:
        return a
    else:
        return b


for i in range(4):
    num1 = int(input("\nDigite o primeiro número: "))
    num2 = int(input("\nDigite o segundo  número: "))
    print("O maior número é ", max(num1, num2))





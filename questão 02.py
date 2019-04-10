def area(num):
    pi=3.14
    area2=pi*num**2
    return area2
def perimetro(num):
    pi=3.14
    perimetro2=pi*2*num
    return perimetro2
valor=int(input("Digite o Raio do circulo"))
print("A area calculada é de:",area(valor))
print("O perimetro calculado é: ",perimetro(valor))

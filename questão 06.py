def lados(n,base,altura):
    if n == 3:
        a=base*altura/2
        print("TRIANGULO e o valor do seu perimetro: ",a)
    elif n == 4:
        a=base*altura
        print("QUADRADO e o valor do seu perimetro: ",a)
    elif n == 5:
        print("PENTAGONO")

numero=int(input("informe o nº de lados do poligono"))
while numero != 3 and numero != 4 and numero != 5:
    print("POLIGONO INVALIDO")
    numero = int(input("informe o nº de lados do poligono"))
lado1 = int(input("informe o tamanho dos lados"))
lado2 = int(input("informe o tamanho dos lados"))
lados(numero, lado1, lado2)



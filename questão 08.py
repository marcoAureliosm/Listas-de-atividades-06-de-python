def cubo (numero):
    valorcubo = numero * 2
    return valorcubo
while True:
    numero=int(input("DIGITE UM VALOR"))
    cubo(numero)
    n=str(input("DESEJA CONTINUAR [S]-SIM [N]-N"))
    if n=="S":
        numero = int(input("DIGITE UM VALOR"))
        print("VALOR AO CUBO DO NUMERO DIGITADO",cubo(numero))
    elif n=="N":
        print("PROGRAMA ENCERRADO...")
        break
    else:
        print("CARACTERE INVALIDO")
        n = str(input("DESEJA CONTINUAR [S]-SIM [N]-N"))



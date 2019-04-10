def trueandfalso(num):
    if num %2 ==0:
        return True

    else:
        return False
valor =int(input("DIGITE O NUMERO"))
trueandfalso(valor)
if trueandfalso(valor)==True:
    print("NUMERO  PAR: ",valor)
else:print("NUMERO IMPAR: ",valor)


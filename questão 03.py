def celsius(f):
    celsius  = 5 * (f - 32) / 9
    print("Celsius",celsius )
    return celsius
valor=int(input("DIGITE A TEMPERATURA EM FAHRENHEIT: "))
print("Celsius",celsius(valor) )

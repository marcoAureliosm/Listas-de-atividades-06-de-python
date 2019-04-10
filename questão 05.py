def peso_ideal(sexo,altura):
    if sexo=="f":
        peso=72.7*altura
        print("SEU PESO IDEAL É: ", peso)

    elif sexo =="m":
        peso = 62.1 * altura
        print("SEU PESO IDEAL É: ",peso)


s=str(input("DIGITE O SEU SEXO [F]-FRMININO [M]-MASCULINO"))
a=float(input("DIGITE A SUA ALTURA"))
peso_ideal(s,a)

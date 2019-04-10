def media(nota1,nota2):
    media=(nota+nota2)/2
    if media>=6:
        return media
    else:
       return media
nota=int(input("DIGITE A SUA 1ª NOTA"))
notas=int(input("DIGITE SUA 2ª NOTA"))
if media(nota,notas)>=6:
    print("PARABENS VC ESTÁ APROVADO :")
else:
    print("VC ESTÁ REPROVADO: ")

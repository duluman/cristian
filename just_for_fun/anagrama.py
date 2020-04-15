# acest program verifica daca doua texte indeplinesc conditia de anagrama
def tastatura():
    global text
    text = input("Tasteaza textul: ")
    text = text.replace(' ', '')
    text.upper()


def verificare():
    tastatura()
    t1 = text
    tastatura()
    t2 = text
    print("Primul text este {}".format(t1))
    print("Al doilea text este {}".format(t2))

    if len(t1) == len(t2):
        print("Cele doua cuvinte au acelasi numar de caractere")
        if sorted(t1) == sorted(t2):
            print(" Avem anagrama !")
        else:
            print("Nu avem anagrama !")
    else:
        print("Nici macar nu au aceeasi lungime de caractere")

    amazon = input("Mai vrei sa verifici alte texte?")
    if amazon == "Da" or amazon == "da":
        verificare()
    else:
        return


verificare()

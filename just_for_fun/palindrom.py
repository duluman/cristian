#aceste program verifica daca textul este palindrom
def tastatura():
    global text
    text = input("Tasteaza textul: ")
    text = text.replace(' ', '')
    text.upper()


def verificare():
    tastatura()

    if text == text[::-1]:
        print("Este un palindrom")

    else:
        print("Nu este un palindrom")

    amazon = input("Vrei sa mai verific un alt text?")
    if amazon == "Da" or amazon == "da":
        verificare()
    else:
        return


verificare()

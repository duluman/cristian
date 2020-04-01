

def verificare(x, y, semn):
    global r_partial, z
    r_partial = 0
    if semn == "*":
        r_partial = x * y
        print("Rezultat partial: ", r_partial)
    elif semn == "/":
        try:
            r_partial = x / y
            print("Rezultat partial: ", r_partial)
        except ZeroDivisionError:
            print("Nu se poate face impartirea la 0")

    elif semn == "+":
        r_partial = x + y
        print("Rezultat partial: ", r_partial)
    elif semn == "-":
        r_partial = x - y
        print("Rezultat partial: ", r_partial)
    else:
        print("Semnul tastat nu se regaseste in variantele date, \nte rog sa tastezi: +. -, *, /, ")

    z = input()

    if z == "=":
        r_final = r_partial
        print("Rezultat final: ", r_final)
        exit()

    else:
        try:
            semn = z
            x = r_partial
            y = int(input())
        except ValueError:
            print("Nu ai respectat regulile")

        verificare(x, y, semn)


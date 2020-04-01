print("\n\n\t\t*******************")
print("\t\t      X si O")
print("\t\t*******************")
print("\t\t*** Sa incepem! ***")
print("\t\t******************* \n ")


semn = " "

tabla = [[11, 12, 13],
         [21, 22, 23],
         [31, 32, 33]]

# generam tabla ca design

def afisare_tabla(tabla):
    print("+--------" * 3, "+", sep="")
    for ran in range(3):
        print("|        " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(tabla[ran][col]) + "   ", end="")
        print("|")
        print("|        " * 3, "|", sep="")
        print("+--------" * 3, "+", sep="")

# adaugam numerele din lista tabla in design

def functie_adaugare(pozitie_j, semn):
    for ran in range(3):
        for col in range(3):
            if pozitie_j in str(tabla[ran][col]):
                tabla[ran][col] = " {}".format(semn)
                afisare_tabla(tabla)


# realizam  functiile care sa verifice daca este indeplinit criteriu de joc castiga
# adica  X X X sau O O O

victorie_x = 0
victorie_o = 0


def rand():
    global victorie_x, victorie_o, victorie_p
    victorie_p = []

    if tabla[0][0] == tabla[0][1] == tabla[0][2]:
        victorie_p.append(tabla[0][0])
        print("\nSarbatorim jocul castigat de {}".format(tabla[0][0]))
        if tabla[0][0] == " X":
            victorie_x += 1
            print(victorie_x)
        elif tabla[0][0] == " O":
            victorie_o += 1
        resetare_tabla()
    if tabla[1][0] == tabla[1][1] == tabla[1][2]:
        victorie_p.append(tabla[1][0])
        print("\nSarbatorim jocul castigat de {}".format(tabla[1][0]))
        if tabla[1][0] == " X":
            victorie_x += 1
        elif tabla[1][0] == " O":
            victorie_o += 1
        resetare_tabla()
    if tabla[2][0] == tabla[2][1] == tabla[2][2]:
        victorie_p.append(tabla[2][0])
        print("\nSarbatorim jocul castigat de {}".format(tabla[2][0]))
        if tabla[2][0] == " X":
            victorie_x += 1
        elif tabla[2][0] == " O":
            victorie_o += 1
        resetare_tabla()


def coloana():
    global victorie_x, victorie_o
    if tabla[0][0] == tabla[1][0] == tabla[2][0]:
        victorie_p.append(tabla[0][0])
        print("\nSarbatorim jocul castigat de {}".format(tabla[0][0]))
        if tabla[0][0] == " X":
            victorie_x += 1
        elif tabla[0][0] == " O":
            victorie_o += 1
        resetare_tabla()
    if tabla[0][1] == tabla[1][1] == tabla[2][1]:
        victorie_p.append(tabla[0][1])
        print("\nSarbatorim jocul castigat de {}".format(tabla[0][1]))
        if tabla[0][1] == " X":
            victorie_x += 1
        elif tabla[0][1] == " O":
            victorie_o += 1
        resetare_tabla()
    if tabla[0][2] == tabla[1][2] == tabla[2][2]:
        victorie_p.append(tabla[0][2])
        print("\nSarbatorim jocul castigat de {}".format(tabla[0][2]))
        if tabla[0][2] == " X":
            victorie_x += 1
        elif tabla[0][2] == " O":
            victorie_o += 1
        resetare_tabla()



def egalitate():
    eg = 0 #setam o variabila care sa numere cate semne de X si O sunt pe tabla
    for element in list(tabla):
        if element == [" X"] or element == [ "O"]:
            eg += 1
    if eg == 9:
        print("Avem egalitate! \nVom reinitializa tabla de joc!")
        resetare_tabla()





def diagonala():
    global victorie_x, victorie_o
    if tabla[0][0] == tabla[1][1] == tabla[2][2]:
        victorie_p.append(tabla[0][0])
        print("\nSarbatorim jocul castigat de {}".format(tabla[0][0]))
        if tabla[0][0] == " X":
            victorie_x += 1
        elif tabla[0][0] == " O":
            victorie_o += 1
        resetare_tabla()
    if tabla[0][2] == tabla[1][1] == tabla[2][0]:
        victorie_p.append(tabla[1][1])
        print("\nSarbatorim jocul castigat de {}".format(tabla[0][2]))
        if tabla[0][2] == " X":
            victorie_x += 1
        elif tabla[0][2] == " O":
            victorie_o += 1
        resetare_tabla()

# pentru a determima castigatorul 2 din 3


def castigator_xo():

    egalitate()
    rand()
    coloana()
    diagonala()

    global victorie_x, victorie_o, i, jucam

    if victorie_x == tip_joc:
        print("A castigat campionatul X")
        if tip_joc == 2:
            print("Jucam 2 din 3")
        else:
            print("Jucam 3 din 4")

        i=0
        jucam = False
        return

    elif victorie_o == tip_joc:
        print("A castigat campionatul O")
        if tip_joc == 2:
            print("Jucam 2 din 3")
        else:
            print("Jucam 3 din 4")

        i = 0
        jucam = False
        return


# setam din nou cifrele pe tabla de joc
def resetare_tabla():

    global tabla

    tabla = [[11, 12, 13],
             [21, 22, 23],
             [31, 32, 33]]
    print("\n  ")
    joc()

# functia joc ne permite sa introducem de la tastatura numarul dorit de pe tabla de joc
# cheama functia castigator_xo pentru a verifica daca sunt cele 3 caracatere la rand


def joc():

    afisare_tabla(tabla)
    global j
    global i
    i = 10
    j = 1
    while i:

        try:

            pozitie_j = input("\n Jucator, tasteaza in cifre pozitia \npe care vrei sa o ocupi:\t")
            egalitate()
            if pozitie_j in str(tabla):
                if j % 2:
                    functie_adaugare(pozitie_j, "X")
                    j += 1
                    castigator_xo()

                else:
                    functie_adaugare(pozitie_j, "O")
                    j += 1
                    castigator_xo()

            else:

                print(" !!! Nu ai tastat cifre de pe tabla !!!")
                j += 2

        except():

            print("Nu ai tastat cifre de pe tabla ")


# IVR
def tema3():
    jucam = True
    while jucam == True:
        global optiuni1
        print("""
        Joc nou -- tasteaza: joc --
        Iesire din aplicatie -- tasteaza: iesire --- \n""")
        optiuni1 = input("\t\tAstept raspunsul tau:")

        global amazon
        amazon = True

        global optiune_finala, tip_joc

        if optiuni1 == "joc" and amazon == True:

            while amazon:
                print("\n rapid (joc 2 din 3)\n \t\t sau \n agale (joc 3 din 5)\n \t\tsau \n\t   inapoi")
                optiune_finala = input("\nAlege rapid, agale sau inapoi: \n")
                if optiune_finala == "rapid":
                    tip_joc = 2
                    joc()  # joc 2 din 3

                elif optiune_finala == "agale":
                    tip_joc = 3
                    joc()  # joc 3 din 5

                elif optiune_finala == "inapoi":
                    amazon = False



                else:
                    print("Nu ai ales o optiune valabila")
                    optiune_finala = input(" ??? rapid sau agale ??? \n")


        elif optiuni1 == "iesire":
            print( 7 *"\n\t \tLa revedere! \n ")
            print("\t  Te mai asteptam!")
            break
        else:
            print("Nu ai tastat 'joc' sau 'iesire'")
            #optiuni1 = input("joc sau iesire?:")
            continue



tema3()
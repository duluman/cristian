print("*******************")
print(""""Salut,
E sunt un simpu calculator.
Te pot ajuta cu sa calculezi:
suma daca folosesti +
diferenta daca folosesti -
inmultirea daca folosesti *
inpartirea daca folosesti /
Cand vrei sa te opresti tasteaza =""")
print("*******************")
print("*** Sa incepem! ***")
print("******************* \n \n")


def verificare(x, y, semn):
    global r_partial
    global z
    if semn == "*":
        r_partial = x * y
        print("Rezultat partial: ", r_partial)
    elif semn == "/":
        try:
            r_partial = x / y
            print("Rezultat partial: ", r_partial)
        except ZeroDivisionError:
            print("Nu se poate face impartirea la 0")
        #  verificare(x, y, semn)

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
        semn = z
        x = r_partial
        y = int(input())
        verificare(x, y, semn)


r_final = 0

# try:
#     while r_final == 0:
#
#         # try:
#         x = int(input())
#         semn=input()
#         y = int(input())
#         #r_partial=0
#         verificare(x, y, semn)
# except():
#     print("Nu ai respectat sugestiile date")


def test_verificare():
    assert verificare(7, 8, '-')
    r_partial == 1


test_verificare()
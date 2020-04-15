# calculam cifra vietii
def ziua():
    global text
    text = input("Tasteaza ziua ta de nastere ( din 8 cifre in formatul ZZLLAAAA):")

    if len(text) != 8:
        print("Nu ai respectat regula")
    else:
        calcul()


def calcul():

    suma = suma_noua = 0

    for element in text:
        suma += int(element)

    while suma > 9:
        for element in str(suma):
            suma_noua += int(element)
            suma = suma_noua
        suma_noua = 0

    print(suma)
    amazon= input("Daca vrei sa verifici o alta zi de nastere tasteaza da: ")
    if amazon == "da":
        ziua()
    else:
        return

ziua()




    # if suma > 9:
    #     for element in str(suma):
    #         suma_noua += int(element)
    #     print(suma_noua)
    #
    # suma = suma_noua
    # suma_noua = 0
    # if suma > 9:
    #     for element in str(suma):
    #         suma_noua += int(element)
    #     print(suma_noua)
    #
    # suma = suma_noua
    #
    # print("Digit of your life is: ", suma)



# text = input("Tasteaza ziua ta de nastere ( din 8 cifre in formatul ZZLLAAAA):")
#
# if len(text) != 8:
#     print("Nu ai respectat regula")
# else:
#     suma = suma_noua = 0
#
#     for element in text:
#         suma += int(element)
#
#     if suma > 9:
#         for element in str(suma):
#             suma_noua += int(element)
#         suma = suma_noua
#
#     print("Digit of your life is: ", suma)





src = open('n_catalog.txt', 'rt')
dst = open('m_catalog.txt', 'wt')

dst.write("Prima data afisam elevii cu nume si prenume si nota")
caracter1 = src.read(1)
dst.write(caracter1)
cnt = 0
while caracter1 != '':
    print(caracter1, end='')
    cnt += 1
    caracter1 = src.read(1)
    dst.write(caracter1)
print(cnt)
dst.write("\n \n Avem {} caractere in text".format(str(cnt)))
# src.close()
# dst.close()

dst.write(" \n A doua oara ii facem anonimi si calculam media notelor \n")

suma = nr = 0

for line in open("n_catalog.txt", "rt"):
    boring = line
    notare = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # nota = boring[-1]
    print(boring)

    for alfa in boring:
        if alfa in notare:
            print("Elevul are nota: {} ".format(alfa))
            print("------------------=")
            dst.write("              \n")
            dst.write("Elevul are nota {} ".format(alfa))
            suma += int(alfa)
            nr += 1

media = int(suma)/int(nr)
print(media)
dst.write("\n Media este:  ")
dst.write(str(media))



src.close()
dst.close()

patrat = [1, 4, 9]

print(patrat[::2]) # afiseaza toate elementele din lista care respecta masura 2

print(patrat[::-1]) # afiseaza lista in ordine inversa

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(sqs[7:5:-1]) # incepe cu pozita 7 si afiseaza catre pozitia 5 din 1 in 1 [fara sa fie inclusa pozitia 5]

cubes = [i**3 for i in range(5)]

print(cubes)

evens = [i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)

print("{0} {1} {0}".format("abra", "cad"))
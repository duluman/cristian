from calculator2 import verificare

print("*******************")
print(""""
Te pot ajuta cu sa calculezi:
suma daca folosesti +
diferenta daca folosesti -
inmultirea daca folosesti *
inpartirea daca folosesti /
Cand vrei sa te opresti tasteaza =""")
print("*******************")
print("*** Sa incepem! ***")
print("******************* \n \n")


r_final = 0


while r_final == 0:
    try:
        x = int(input())
        semn=input()
        y = int(input())
    except ValueError:
        print("Nu ai tastat cifre")

    verificare(x, y, semn)

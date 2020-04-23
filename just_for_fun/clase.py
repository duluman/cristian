# class Stack:
#     def __init__(self):
#         self.__stackList = []
#
#     def push(self, val):
#         self.__stackList.append(val)
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
#
#
# stackObject1 = Stack()
# stackObject2 = Stack()
#
# stackObject1.push(7)
# # stackObject2.push(stackObject1.pop())
#
# print(stackObject1.pop())
# # print(stackObject2.pop())

#========================

# class Stack:
#     def __init__(self):
#         self.__stackList = []
#
#     def push(self, val):
#         self.__stackList.append(val)
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
#
# littleStack = Stack()
# anotherStack = Stack()
# funnyStack = Stack()
#
# littleStack.push(1)
# anotherStack.push(littleStack.pop() + 1)
# funnyStack.push(anotherStack.pop() - 2)
#
# print(funnyStack.pop())

#========================


# class ExampleClass:
#     counter = 0
#
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.counter += 1
#
#
# exampleObject1 = ExampleClass()
# exampleObject2 = ExampleClass(2)
# exampleObject3 = ExampleClass(4)
#
# print(exampleObject1.__dict__, exampleObject1.counter)
# print(exampleObject2.__dict__, exampleObject2.counter)
# print(exampleObject3.__dict__, exampleObject3.counter)

#========================

#
# class Classy:
#     def other(self):
#         print("other")
#
#     def method(self):
#         print("method")
#         self.other()
#
#     def matematica(self):
#         print("Matematica")
#         self.method()
#
#
# obj = Classy()
# # obj.method()
# obj.matematica()
#========================


# def fun(n):
#     for i in range(n):
#         yield i
#
# for v in fun(5):
#     print(v)
#========================


# def powersOf2(n):
#     pow = 1
#     for i in range(n):
#         yield pow
#         pow *= 2
#
# t = [x for x in powersOf2(5)]
#
# print(t)


#========================

# x = int(input("Tasteaza valoare lui X:"))
# y = int(input("Tasteaza valoarea lui y:"))
#
# pwr = lambda x, y: x**y
#
# print("X la puterea lui Y este:", pwr(x, y))

#========================

# def makeclosure(par):
#     loc = par
#
#     def power(p):
#         return p ** loc
#
#     return power
#
#
# fsqr = makeclosure(2)
# fcub = makeclosure(3)
#
# print(fsqr, fcub)
#
# for i in range(5):
#     print(i, fsqr(i), fcub(i))

#========================

# cnt = 0
# s = open('text.txt', "rt")
# ch = s.read(1)
# print(ch)
# ch = s.read(1)
# print(ch)
# ch = s.read(1)
# print(ch)
# ch = s.read(1)
# print(ch)
# while ch != '':
#     print(ch, end='')
#     cnt += 1
#     ch = s.read(1)
# s.close()
# print("\n\nCharacters in file:", cnt)

#========================

# fo = open('newtext.txt', 'wt') # a new file (newtext.txt) is created
# for i in range(21):
#     s = "line #" + str(i+1) + "\n"
#     for ch in s:
#         fo.write(ch)
# fo.close()

# daca schimb parametrul din rage, imi rescrie fisierul, nu adauga
# in cazul in care fisierul nu exista el in creeaza/ daca exista il suprascrie

#========================

src = open('text.txt', 'rt')
dst = open('newtext.txt', 'wt')
caracter1 = src.read(1)
dst.write(caracter1)
cnt = 0
while caracter1 != '':
    print(caracter1, end='')
    cnt += 1
    caracter1 = src.read(1)
    dst.write(caracter1)

print(cnt)
dst.write("   spatiu   lasam    spatiu   ")
dst.write("Avem {} caractere in text".format(str(cnt)))

src.close()
dst.close()
#========================





#========================

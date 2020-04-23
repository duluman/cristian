class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")

print(fido.name, fido.color)
fido.bark()

maya = Cat("Maya", "white")
print(maya.name, maya.color)
maya.purr()

#=============================
print("""


""")
class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
print(first)
second = Vector2D(3, 9)
print(second)
result = first + second
print(result.x)
print(result.y)
#=============================
print("""


""")

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def calculate_area(self):
    return self.width * self.height

  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)
    ##Technically, the parameters self and cls are just conventions; they could be changed to anything else.
    ##However, they are universally followed, so it is wise to stick to using them.
square = Rectangle.new_square(5)
print(square.calculate_area())

#=============================
print("""


""")

class Person:
    def __init__(self, age):
        self.age = int(age)


    @property
    def isAdult(Person):
        if self.age > 18:
            return True
        else:
            return False

marin = Person(17)
print(marin.age)
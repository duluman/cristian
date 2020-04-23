
def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))

def my_func(f, arg):
  return f(arg)

print(my_func(lambda x: 2*x*x, 5))


hahahap = (lambda x: x**2 + 5*x + 4)(4)
print(hahahap)

a2 = (lambda x: x*2)(7)
print(a2)



nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x < 5, nums))
print(res)

def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()


@decor
def print_t():
    print("Hello wolrd")

print_t()

#==========================
def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
print(fib(4)) # why 5 ?
#==========================

from itertools import product
a = {1, 2}
print(len(list(product(range(3), a))))


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


print(power(2, 3))
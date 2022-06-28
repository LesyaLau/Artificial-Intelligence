from functools import reduce

list3 = (l for l in range(100, 1001) if l%2 == 0)
def my_func(prev_el, el):
  return prev_el*el
print(f"произведение четных чисел от 100 до 1000 равно: {reduce(my_func, list3)}")

from functools import reduce

list4 = (l for l in range(100, 1001) if l%2 == 0)
a = reduce(lambda x,y: x+y, list4)
print(f"сумма четных чисел от 100 до 1000 равна: {a}")
from math import factorial

def fact_n(n):
    for i in range(n):
      print(i, end='! = ')
      yield factorial(i)

print("вычисление факториала")
for el in fact_n(15):
      print(el)
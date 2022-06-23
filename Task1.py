a = int(input("введите первое число: "))
b = int(input("введите второе число: "))
if b == 0:
    print('на 0 делить нельзя')
def division(a,b):
  return round(a/b,2)
print(division(a,b))


c = int(input("введите первое число: "))
d = int(input("введите второе число: "))
if d == 0:
    print('на 0 делить нельзя')
division1 = lambda c,d: round(c/d,3)
print(division1(c,d))
x = int(input("введите действительное положительное число: "))
y = int(input("целое отрицательное число: "))

def degree(x,y):
  return x ** y
print(degree(x,y))


u = int(input("введите действительное положительное число: "))
w = int(input("целое отрицательное число: "))

degree1 = lambda u,w: u**w
print(degree1(u,w))

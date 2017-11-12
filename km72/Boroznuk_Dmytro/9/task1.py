# Функция считает расстаяние между 2 точками.
def distance(x1, y1, x2, y2):
  return ((x2-x1)**2+(y2-y1)**2)**(1/2)
x1=float(input("Введите x первой точки:"))
y1=float(input("Введите y первой точки:"))
x2=float(input("Введите x второй точки:"))
y2=float(input("Введите y второй точки:"))
print(distance(x1, y1, x2, y2))

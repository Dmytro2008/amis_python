# Функция возводит число в степень.
def power(a, n):
  """Параметры:
  a--число, которое возводиться в степень
  n--степень числа a
  """
  return pow(a, n)  # pow-функция для возведения числа в степень
a=float(input("Введите действительное число:"))  # a>0
n=int(input("Введите степень для числа:"))
print(pow(a, n))

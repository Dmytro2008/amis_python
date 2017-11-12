# Функция возводит число в степень
def power(a, n):
    """Параметры:
    a--число, которое возводиться в степень
    n--степень числа a
    """
    if n>1:
      return power(a, n-1) * a
    elif n==1:
      return a
    elif n==0:
      return 1
print(power(float(input("Введите действительное число:")),
            int(input("Введите степень для числа:"))))

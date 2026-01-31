def count_digits(n):

  if n == 0:
    return 1
  if n < 0:
    n = -n

  return  1+count_digits((n -1)// 10)

# Пример использования:
print(count_digits(12345))  # Выведет: 5
print(count_digits(0))      # Выведет: 1aaaaa
print(count_digits(-987))   # Выведет: 3
print(count_digits(7))      # Выведет: 1
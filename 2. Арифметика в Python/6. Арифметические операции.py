print(3 + 4)
print(3 ** 2)   # => 9 (power)
print(81 / 9)   # => 9.0 (division)
print(25 // 8)  # => 3 (mod)
print(25 % 8)   # => 1 (div)

#9 композиция операций (просто последовательность операторов согласно их приоритетам)
print(8 / 2 + 5 - -3 / 2)  # => 10.5

#10 приоритет, скобки
print(3 ** (4 - 2))  # => 9
print(70 * (3 + 4) / (8 + 2))  # => 49

#11 Числа с плавающей точкой
print(0.2 + 0.1) # 0.30000000000000004)
print(0.39 * 0.22) #0.0858

# 12 Linter
# проверка стандарта pep8 с помощью запуска flake8
# python -m pip install flake8
#flake8 "2. Арифметика в Python/6. Арифметические операции.py"  - напишет где у тебя косяки, но исправлять надо самому

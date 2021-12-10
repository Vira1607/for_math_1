print('Выражение\n')

# Дано число x.
# Программа вычисляет выражение:
#
# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))

number = int(input('Введите число x: '))

dividend = 1
divider = 1

for i in range(1, 65, 2):
  dividend *= number - i
  divider *= number - (i + 1)

answer = dividend/divider

print('Ответ:', answer)

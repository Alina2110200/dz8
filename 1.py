numbers = input("Введите числа через пробел: ")
numbers_list = numbers.split()

N = int(input("Введите N: "))

length = len(numbers_list)

N = N % length

for i in range(N):
    last_element = numbers_list[-1]
    numbers_list.pop()
    numbers_list.insert(0, last_element)

print("Результат:", numbers_list)
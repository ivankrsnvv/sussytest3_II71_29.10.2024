# Задача 1.
# Напишите функцию для поиска суммы элементов списка больше х. Замените х на найденное значение. Используйте х как глобальную переменную.

x = 10

def find_sum_and_replace(lst):
    global x
    sum_of_elements_greater_than_x = sum(element for element in lst if element > x)
    if sum_of_elements_greater_than_x != 0:
        x = sum_of_elements_greater_than_x
    return sum_of_elements_greater_than_x

lst = [12, 8, 15, 7]
result = find_sum_and_replace(lst)
print(f"Сумма элементов списка, больших 10, равна: {result}")
print(f"Теперь x равно: {x}")


# Задача 2.
# 2. Напишите программу вычисления выражения: s = х3 + х5 + хn, где х и n вводятся с клавиатуры и  передаются в качестве параметров. Используйте подпрограмму вычисления степени.
def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

def calculate_expression(x, n):
    s = power(x, 3) + power(x, 5) + power(x, n)
    return s

if __name__ == "__main__":
    x = float(input("Введите значение x: "))
    n = int(input("Введите степень n: "))
    result = calculate_expression(x, n)
    print(f"Результат вычисления выражения: {result}")

# задача 3
# Напишите программу для вычисления чисел Фибоначчи, исходя из рекуррентного выражения F(n) = F(n-1) + F(n-2). Используйте рекурсию
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Введите номер члена последовательности Фибоначчи: "))

print(f"{n}-й член последовательности Фибоначчи равен {fibonacci(n)}")

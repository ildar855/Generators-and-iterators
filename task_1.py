def prime_generator(n: int):
    # если значение n меньше или равно 1, функция сразу завершает работу без генерации чисел
    if n <= 1:
        return
    
    # число 2 - единственное четное простое число, поэтому оно выводится отдельно
    yield 2 

    # цикл от 3 до n с шагом 2 - проверяем только нечётные числа (все остальные чётные числа больше 2 уже не могут быть простыми - т.к. делятся на 2).
    for number in range(3, n, 2):
        is_prime = True
        
        # для каждого числа проверяется, делится ли оно нацело на любое другое число в диапазоне от 3 до квадратного корня этого числа. Если такое деление возможно, значит, число составное, и проверка прекращается
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                is_prime = False
                break
                
        if is_prime:
            yield number

# пример работы
for prime in prime_generator(15): 
    print(prime)  # 2, 3, 5, 7, 11, 13 


# Почему проверяем делимость только до квадратного корня числа.
# Если число n делится на некоторое число k, то обязательно найдется другой делитель m = n / k, который тоже будет делителем n.
# При этом хотя бы один из этих делителей (k или m) будет меньше или равен корню из n.
# Значит, если мы проверим все числа до корня из n и не найдем делителей, то число n точно будет простым.
# Пример: допустим, нам нужно проверить, является ли число 97 простым. Его квадратный корень примерно равен 9.8.
# Нам нужно проверить делимость числа 97 на все числа от 3 до 9. Если ни одно из этих чисел не будет делителем, то 97 – простое число.
# Прибавляем 1, т.к. в последовательность включает все числа до этого значения, но не само это значение.
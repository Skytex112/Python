import time
# Exercise 1
def odd_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

for x in odd_numbers(1, 10):
    print(x, end=" ")

#Exercise 2
def outside_range(lst, start, end):
    for item in lst:
        if item < start or item > end:
            yield item

numbers = [1, 5, 10, 15, 20]
for x in outside_range(numbers, 5, 15):
    print(x, end=" ")

# Exercise 3
def horizontal_line(symbol):
    print(symbol * 10)


def vertical_line(symbol):
    for i in range(10):
        print(symbol)


def show_line(symbol, function_to_call):
    function_to_call(symbol)

symbol = input("Введіть символ: ")
line_type = input("Введіть тип лінії (h - горизонтальна, v - вертикальна): ")

if line_type.lower() == 'h':
    show_line(symbol, horizontal_line)
elif line_type.lower() == 'v':
    show_line(symbol, vertical_line)
else:
    print("Невірний тип лінії")

# Exercise 4
def timer(func):
    def wrapper():
        start_time = time.time()
        
        result = func()
        
        end_time = time.time()
        print(f"\nЧас виконання: {end_time - start_time:.5f} секунд")
        
        return result
    return wrapper

@timer
def get_even_numbers():
    return [x for x in range(0, 100001) if x % 2 == 0]

evens = get_even_numbers()
print(evens)

# Exercise 5
def timer(func):
    def wrapper(start, end):
        start_time = time.time()
        
        result = func(start, end)
        
        end_time = time.time()
        print(f"\nЧас виконання: {end_time - start_time:.5f} секунд")
        
        return result
    return wrapper

@timer
def get_even_numbers_range(start, end):
    return [x for x in range(start, end + 1) if x % 2 == 0]

evens = get_even_numbers_range(0, 100000)
print(evens)
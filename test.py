print(some_var := 8)
print(some_var)

# debug using f'string:
some_var = "Artem Sushchikh"
print(f'{some_var =}')  # позволяет выводить переменную и ее значение через f'strings


def add_one(number):
    return number + 1
print(add_one(2))


print('='*80)
print()

def parent(num):
    def first_child():
        return "My name is Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

first = parent(1)
second = parent(2)
print(f'{first = }')
print(f'{second = }')

print(first())


print('='*80)
print()


def my_decorator(func):
    def wrapper():
        print('что-то происходит до функции')
        func()
        print('что-то происходит после функции')
    return wrapper


@my_decorator
def say_whee():
    print('Whee!')

say_whee()


import time
import math
answer = math.log(int(time.time()))
print(answer)
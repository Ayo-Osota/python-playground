# print([1, 2, 3])


# # OOP

# class BigObject:  # Class
#     pass


# obj1 = BigObject()  # instanciate an object
# print(type(BigObject))


# class PlayerCharacter:
#     membership = True  # Class Object Attribute

#     def __init__(self, name, age):
#         if self.membership:  # Can use PlayerCharacter.membership
#             self.name = name  # attributes
#             self.age = age
#             self.nationality = 'Nigeria'

#     def run(self):  # method
#         print('run')

#     @classmethod  # method available to entire class, can also be used to create a new object
#     def adding_teddy(cls, num1, num2):
#         return cls('Teddy', num1 + num2)

#     @staticmethod  # Same as class method but without the cls, used when we don't care about the class attributes
#     def adding_things(num1, num2):
#         return num1 + num2


# player1 = PlayerCharacter('James', 23)
# player2 = PlayerCharacter('Cinderella', 16)

# print(player1.adding_things(3, 4))
# print(PlayerCharacter.adding_things(4, 7))

# print(player1.name)
# print(player1.age)
# print(player1.nationality)


# player1.run()
# player2.attack = 2  # New attribute to player2 that other players will not have

# print(player2.attack)


# # Functional programming

# # Pure functions
# # # 1. always returns the same thing
# # # 2. has no side effects


from functools import reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30, 40]


def multiply_by2(item):
    return item*2


def check_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))
print(list(zip(my_list, your_list)))
print(list(map(multiply_by2, my_list)))
print(list(filter(check_odd, my_list)))

# lambda expressions are one time anonymous functions you don't need to run more than once

print(list(map(lambda item: item*2, my_list)))

my_list = [param for param in 'iterable']  # lst comprehension


# Decorators : super charges our function
# 1. they are higher order functions
# 2. they take another function as an argument
# 3. they return a function as a result
# 4. they can modify the behavior of the function they decorate without permanently changing the function

def my_decorator(func):
    def wrap_func():
        print('ayo')
        func()
        print('bolu')
    return wrap_func


@my_decorator
def hello(greeting):
    print(greeting)


hello('there')

# Error handling

while True:
    try:
        age = int(input('age?'))
        print(age)
        raise ZeroDivisionError('hey cut it out bro')
    except ValueError as err:
        print(f'please enter a number {err}')
    else:
        print('thsnkd')
        break
    finally:
        print("I am done")


# Generators

# all generators are iterables but not all iterables are generators

def generator_function(num):
    for i in range(num):
        yield i


for item in generator_function(1000):
    print(item)

g = generator_function(1)

next(g)
print(next(g))

# debugging
# linting
# ide / editors
# read errors
# pdb


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


add(4, 'dfs')

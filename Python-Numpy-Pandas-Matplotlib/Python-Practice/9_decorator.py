def my_decorator(func):
    def wrapper():
        print("Before the function runs...")
        func()
        print("After the function runs...")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# The above code defines a decorator `my_decorator` that adds behavior before and after the execution of the function `say_hello`.
# The `@my_decorator` syntax is a shorthand for applying the decorator to the function.
# When `say_hello()` is called, it will first print "Before the function runs...", then execute the original `say_hello()` function, and finally print "After the function runs...".
# The output will be:
# Before the function runs...
# Hello!
# After the function runs...
# The decorator pattern is a design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class.
# It is a structural pattern that is used to extend the functionalities of classes in a flexible and reusable way.
# The decorator pattern is often used in Python to modify the behavior of functions or methods.
# The decorator pattern is often used in Python to modify the behavior of functions or methods.
# It is a powerful tool for code reuse and separation of concerns.          





import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
# The above code defines a decorator `time_it` that measures the time taken by the decorated function to execute.
# The `@time_it` syntax is a shorthand for applying the decorator to the functions `calc_square` and `calc_cube`.
# When `calc_square(array)` and `calc_cube(array)` are called, the decorator will print the time taken for each function to execute.
# The output will show the time taken for each function in milliseconds.
# The decorator pattern is a design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class.
# It is a structural pattern that is used to extend the functionalities of classes in a flexible and reusable way.
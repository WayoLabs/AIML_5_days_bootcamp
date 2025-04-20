def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

for value in gen:
    print(value)


# The above code defines a generator function `my_generator` that yields three values: 1, 2, and 3.
# The generator is then instantiated and iterated over, printing each value.
# The output will be:
# 1                             
# 2
# 3
# The `yield` statement allows the function to return a value and pause its execution, so it can be resumed later.
# This is different from a regular function that would return a value and terminate its execution.
#
# Generators are a convenient way to create iterators in Python, allowing for lazy evaluation and memory efficiency.
#
# The `for` loop automatically handles the iteration over the generator, calling `next()` on it until it is exhausted.
#
# The `next()` function can also be used directly to get the next value from the generator.
#
# The `StopIteration` exception is raised when there are no more values to yield, which is handled by the `for` loop.                           
#
# The `yield` statement can also be used to send values back into the generator using the `send()` method.
# This allows for more complex interactions with the generator.
#Why use generators?
#Memory-efficient (doesn’t load all items into memory)

#Great for large datasets, files, streams, etc.

def count_up_to(max):
    count = 10
    while count <= max:
        yield count
        count += 1

for num in count_up_to(15):
    print(num)





def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for f in fib():
    if f > 100:
        break
    print(f)

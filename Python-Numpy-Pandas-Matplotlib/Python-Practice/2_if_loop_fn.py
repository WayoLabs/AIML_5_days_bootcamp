# Example of an if statement
budget = int(input("\nEnter your budget: "))

if budget >= 70:
    print("You can afford a cherry!")
elif budget >= 50:
    print("You can afford an apple!")
elif budget >= 30:
    print("You can afford a banana!")
else:
    print("Sorry, not enough budget for any fruit.")


for i in range(1,6):
        s = ''
        for j in range(i):
            s += '*'
        print(s)


for i in range(1,11):
    print(i)


count = 0
while count < 5:
    print("Count is:", count)
    count += 1


def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)  # Output: Sum is: 8


def calculate(a, b):
    return a + b, a * b

sum_val, product = calculate(4, 5)
print("Sum:", sum_val)
print("Product:", product)


def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"

print(calculator(10, 5, "multiply"))  # Output: 50




# lambda function   # A lambda function is a small anonymous function that can take any number of arguments but can only have one expression.
# It is often used for short, throwaway functions that are not reused elsewhere in the code.
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
# lambda function with filter
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
# lambda function with map
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36]
# lambda function with reduce
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 720
# lambda function with sorted
names = ["Alice", "Bob", "Charlie"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)  # Output: ['Bob', 'Alice', 'Charlie']
# lambda function with sorted           
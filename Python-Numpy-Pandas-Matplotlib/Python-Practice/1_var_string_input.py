# Variable and number


base=4.43
height=10.421
area=(1/2)*base*height
print("area is:",area) 
# names are case sensitive
Ai="AI"
ai="ai"
print(Ai)
print(ai)

age = 25
pi = 3.14

print(type(pi))

# String
name = "Virat Kohli"

# Print variables
print("Name:", name)
print("Age:", age)
print("Pi value:", pi)

#string operation
print(name[0])
print(name[-1])
print(name[0:2])
print(name[:2])
print(name[-3:-1])
print(name[-3:])
print(len(name))

print(name.replace('Virat','Rohit'))

print(name.upper())
print(name.lower())



str='145'
print(str.isdigit())

# User input (string)
user_name = input("Enter your name: ")

# User input (number)
user_age = int(input("Enter your age: "))

# Output with formatted string
print(f"\nHello {user_name}, you are {user_age} years old!")
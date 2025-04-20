# A list
my_list = [10, 20, 30, 40]

# Get iterator object
my_iter = iter(my_list)

# Use next() to iterate manually
print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30
print(next(my_iter))  # 40
# If you call next() again, it will raise StopIteration

#using for loop
# Iterate through the list using a for loop
print("Using for loop:")        
for value in my_list:
    print(value)
# Using a while loop





class CountUpTo:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

# Use the iterator
for num in CountUpTo(5):
    print(num)

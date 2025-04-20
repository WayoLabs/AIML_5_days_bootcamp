fruits = ["apple", "banana", "cherry"]

print(type(fruits))  # Output: <class 'list'>

# Accessing elements
print(fruits[1])  # Output: banana
print(fruits[-1]) 
print(fruits[1:3]) 
print(fruits[:2]) 
print(fruits[2:]) 
print(len(fruits)) 

print(fruits.count("banana"))
print("cherry" in fruits)  # Count occurrences of "banana"
# Adding an item
fruits.append("orange")

# Removing an item
fruits.remove("banana")
fruits.insert(0,'mango')
# Loop through list
for fruit in fruits:
    print(fruit)



veges=['potato','carrot','broccoli']
# Concatenate lists
fruits_veges=fruits+veges
print(fruits_veges)  # Output: ['mango', 'apple', 'cherry', 'orange', 'potato', 'carrot', 'broccoli']
# List comprehension
fruits_veges=[fruit for fruit in fruits if fruit[0]=='a']
print(fruits_veges)  # Output: ['apple', 'orange']
fruits[0]='kiwi'
print(fruits)  # Output: ['kiwi', 'apple', 'cherry', 'orange']

fruits[3:]=[2 ,3,4]
print(fruits)  # Output: ['kiwi', 'apple', 'cherry', 2, 3, 4]

# Adding multiple items
fruits.extend(["grape", "mango"])
print(fruits)  # Output: ['kiwi', 'apple', 'cherry', 2, 3, 4, 'grape', 'mango']
# Removing an item by index
del fruits[1]
print(fruits)  # Output: ['kiwi', 'cherry', 2, 3, 4, 'grape', 'mango']
# Removing an item by value
fruits.remove("kiwi")
print(fruits)  # Output: ['cherry', 2, 3, 4, 'grape', 'mango']

# Reversing list
fruits.reverse()
print(fruits)  # Output: ['orange', 'kiwi', 'cherry', 'apple']
# Copying list
fruits_copy=fruits.copy()
print(fruits_copy)  # Output: ['orange', 'kiwi', 'cherry', 'apple']
# Clearing list
fruits.clear()
print(fruits)  # Output: []










captains = {
    'Mi': 'rohit',
    'rcb': 'virat',
    'csk': 'dhoni',
    'delhi': 'rishabh',
    'kolkata': 'dinesh'
}
type(captains)
# Accessing dictionary values
print(captains['Mi'])  # Output: rohit
print(captains.get('rcb'))  # Output: virat
# Adding a new key-value pair
captains['sunrisers'] = 'warner'            
print(captains.keys())
print(captains.values())
print(captains.items())
# Removing a key-value pair
del captains['kolkata']
print(captains)  # Output: {'Mi': 'rohit', 'rcb': 'virat', 'csk': 'dhoni', 'delhi': 'rishabh', 'sunrisers': 'warner'}
# Copying dictionary
captains_copy = captains.copy()
print(captains_copy)  # Output: {'Mi': 'rohit', 'rcb': 'virat', 'csk': 'dhoni', 'delhi': 'rishabh', 'sunrisers': 'warner'}

for team in captains:
    print(team)  # Output: Mi rcb csk delhi sunrisers
for captain in captains.values():
    print(captain)  # Output: rohit virat dhoni rishabh warner
# Looping through keys and values   

for team, captain in captains.items():
    print(f"The captain of {team} is {captain}")
# Output: The captain of Mi is rohit

captains.clear()
print(captains)  # Output: {}

emp={}
emp['age']=35
emp['name']='Alice'
emp['salary']=50000
emp['id']=123
print(emp)  # Output: {'age': 35, 'name': 'Alice', 'salary': 50000, 'id': 123}


#tupple
# Tuple (immutable collection)
# Define a tuple
dimensions = (1920, 1080)
# Access elements
print("Width:", dimensions[0])  # Output: Width: 1920
print("Height:", dimensions[1])  # Output: Height: 1080
# Loop through tuple
for dimension in dimensions:
    print(dimension)  # Output: 1920 1080
# Tuple unpacking
width, height = dimensions
print("Width:", width)    # Output: Width: 1920
print("Height:", height)  # Output: Height: 1080
# Tuple concatenation
dimensions2 = (1280, 720)
# Concatenate tuples
dimensions_combined = dimensions + dimensions2
print(dimensions_combined)  # Output: (1920, 1080, 1280, 720)





# List of dictionaries
students = [
    {"name": "John", "age": 22},
    {"name": "Jane", "age": 20},
    {"name": "Mike", "age": 21}
]
# Accessing dictionary values
print(students[0]["name"])  # Output: John
print(students[1]["age"])   # Output: 20
# Adding a new student
students.append({"name": "Alice", "age": 23})
print(students)  # Output: [{'name': 'John', 'age': 22}, {'name': 'Jane', 'age': 20}, {'name': 'Mike', 'age': 21}, {'name': 'Alice', 'age': 23}]
# List of tuples
fruits_tuple = ("apple", "banana", "cherry")
# Accessing tuple values
print(fruits_tuple[0])  # Output: apple
print(fruits_tuple[1:3])  # Output: ('banana', 'cherry')
# Tuple unpacking
fruit1, fruit2, fruit3 = fruits_tuple
print(fruit1)  # Output: apple
print(fruit2)  # Output: banana
print(fruit3)  # Output: cherry
# Tuple concatenation
fruits_tuple2 = ("orange", "grape")                     









#######
# Each student is a dictionary
student1 = {
    "name": "Amit",
    "age": 21,
    "dob": (2003, 5, 17),  # Tuple: (Year, Month, Day)
    "courses": ["Math", "CS"]
}

student2 = {
    "name": "Sara",
    "age": 22,
    "dob": (2002, 8, 25),
    "courses": ["Biology", "Chemistry"]
}

# List of all students
students = [student1, student2]

# Print all student details
for s in students:
    print(f"\nName: {s['name']}")
    print(f"Age: {s['age']}")
    print(f"DOB: {s['dob'][2]}/{s['dob'][1]}/{s['dob'][0]}")
    print("Courses:", ", ".join(s["courses"]))



# list comprehension creates an entire list 
# generator does not creates list instead creates generator objects 
# Create list comprehension: squares
# list comprehension
squares = [i **2 for i in range(0,10)]
print(squares)

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]
print(matrix)

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = [member for member in fellowship if len(member) >= 7]

print(new_fellowship)    
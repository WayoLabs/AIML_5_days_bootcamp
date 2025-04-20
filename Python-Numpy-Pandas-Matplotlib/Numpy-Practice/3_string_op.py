import numpy as np 



# Array String Operations
arr = np.array(['apple', 'banana', 'cherry'])
arr1 = np.char.upper(arr)
print("Uppercase Array 1:", arr1)
# Array String Concatenation
arr2 = np.char.add(arr, ' fruit')
print("Concatenated Array 2:", arr2)
# Array String Splitting
arr3 = np.char.split(arr2, ' ')
print("Split Array 3:", arr3)
# Array String Joining
arr4 = np.char.join('-', arr)
print("Joined Array 4:", arr4)
# Array String Replacement
arr5 = np.char.replace(arr, 'a', 'A')
print("Replaced Array 5:", arr5)
# Array String Searching
arr6 = np.char.find(arr, 'a')
print("Searched Array 6:", arr6)
# Array String Counting
arr7 = np.char.count(arr, 'a')
print("Counted Array 7:", arr7)
# Array String Comparison
arr8 = np.char.equal(arr, 'banana')
print("Compared Array 8:", arr8)
# Array String Length
arr9 = np.char.str_len(arr)
print("Length of Array 9:", arr9)
# Array String Formatting
arr10 = np.char.add('Hello ', arr)
print("Formatted Array 10:", arr10)
# Array String Capitalization
arr11 = np.char.capitalize(arr)
print("Capitalized Array 38:", arr11)
# Array String Title Case
arr12 = np.char.title(arr)
print("Title Case Array 12:", arr12)
# Array String Centering
arr13 = np.char.center(arr, 10)
print("Centered Array 13:", arr13)
# Array String Justification
arr14 = np.char.ljust(arr, 10)
print("Left Justified Array 14:", arr14)
arr15 = np.char.rjust(arr, 10)
print("Right Justified Array 15:", arr15)
# Array String Stripping
arr16 = np.char.strip(arr)
print("Stripped Array 16:", arr16)
# Array String Encoding
arr44 = np.char.encode(arr, 'utf-8')
print("Encoded Array 44:", arr44)
# Array String Decoding
arr45 = np.char.decode(arr44, 'utf-8')
print("Decoded Array 45:", arr45)
# Array String Startswith
arr46 = np.char.startswith(arr, 'a')
print("Startswith Array 46:", arr46)
# Array String Endswith
arr47 = np.char.endswith(arr, 'a')
print("Endswith Array 47:", arr47)
# Array String Partitioning
arr48 = np.char.partition(arr, 'a')
print("Partitioned Array 48:", arr48)
# Array String Rpartitioning
arr49 = np.char.rpartition(arr, 'a')
print("Rpartitioned Array 49:", arr49)
# Array String Zfill
arr50 = np.char.zfill(arr, 10)
print("Zfilled Array 50:", arr50)
# Array String Expand Tabs
arr51 = np.char.expandtabs(arr, 4)
print("Expanded Tabs Array 51:", arr51)
# Array String Splitlines
arr52 = np.char.splitlines(arr)
print("Splitlines Array 52:", arr52)
# Array String Translate
arr53 = np.char.translate(arr, str.maketrans('aeiou', 'AEIOU'))
print("Translated Array 53:", arr53)
# Array String Isdigit
arr54 = np.char.isdigit(arr)
print("Isdigit Array 54:", arr54)
# Array String Isalpha
arr55 = np.char.isalpha(arr)
print("Isalpha Array 55:", arr55)
# Array String Isalnum
arr56 = np.char.isalnum(arr)
print("Isalnum Array 56:", arr56)
# Array String Islower
arr57 = np.char.islower(arr)
print("Islower Array 57:", arr57)
# Array String Isupper
arr58 = np.char.isupper(arr)
print("Isupper Array 58:", arr58)
# Array String Isnumeric
arr60 = np.char.isnumeric(arr)
print("Isnumeric Array 60:", arr60)
# Array String Isdecimal
arr61 = np.char.isdecimal(arr)
print("Isdecimal Array 61:", arr61)
# Array String Isspace
arr62 = np.char.isspace(arr)
print("Isspace Array 62:", arr62)
# Array String Isnumeric



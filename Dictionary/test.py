sample_str = 'Mango'
str_count = {}

for char in sample_str:
    if char not in str_count:
        str_count[char]= 1
        print(str_count)
    else:
        str_count[char]= str_count.get(char,0)+1

print(str_count)


#1 Add a New Key-Value Pair

car = {'brand': 'TATA', 'Model': 'Curve'}
car['year'] = '2025'
print(car)

#2 Update a Value

employee = {'name': "Mayur", "Position": "Test Engineer"}
employee['Position'] = 'Sr. test engineer'
print(employee)


#1 Add a New Key-Value Pair

car = {'brand': 'TATA', 'Model': 'Curve'}
car['year'] = '2025'
print(car)


#2 Update a Value

employee = {'name': "Mayur", "Position": "Test Engineer"}
employee['Position'] = 'Sr. test engineer'
print(employee)


#3 Loop Through Dictionary Keys

fruits = {"apple": 2, "banana": 5, "mango": 3}
for fruit in fruits:
    print(fruit)




#4 Loop Through Dictionary Values
prices = {"pen": 10, "pencil": 5, "eraser": 7}
for price in prices.values():
    print(price)




#5 Loop Through Keys and Values
marks = {"math": 90, "science": 85}
for key, values in marks.items():
    print(key, ":", values)

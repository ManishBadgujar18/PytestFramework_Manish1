#Print numbers from 1 to 10
#1
num1= []
for num in range(1,11):
    num1.append(num)
print(num1)

#2
fruits = ['apple', 'grapes', 'jam']
for i in fruits:
    print(i)


#3 Sum of first 10 natural numbers

count = 0

for num in range(1,11):
    count = num + count
print('sum:', count)


#4 Print even numbers from 1 to 10

evennum = []
for num in range(1,11):
    if num%2 == 0:
        evennum.append(num)
print(evennum)



#5 Generate a pattern
for i in range(1, 6):
    print("*" * i)



#6 Repeat name 3 times
for i in range(3):
    print("Manish")



#7 print square of no.
for num in range(1,6):
    print(num * num)



#7 print cube of no.
for num in range(1,6):
    print(num * num * num)



#8 Print only even numbers from list

evennum = [1, 3, 4, 6, 5, 7, 8]
for i in evennum:
    if i%2 == 0:
        print('even:', i)

#9 Print only odd numbers from list

oddnum = [1, 3, 4, 6, 5, 7, 8, 9, 11]
for i in oddnum:
    if i%2 != 0:
        print('odd:', i)


#10 Print "Yes" if number is greater than 5

num = [1, 3, 4, 6, 5, 7, 8]
for i in num:
    if i>5:
        print("yes:", i)
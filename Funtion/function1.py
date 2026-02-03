# calculator

def add(x, y):
    num1 = x
    num2 = y
    addValue = num1 + num2
    return addValue


def mul(x, y):
    num1 = x
    num2 = y
    mulValue = num1 * num2
    return mulValue


## main program
res1 = add(3, 4)
print(res1)
res = mul(4, 5)
print(res)

print('------------------------------------------')
# something goes in, somethong comes out

def add(x, y):
    z = x + y
    return z


return_value = add(4, 4)
print(return_value)

print('------------------------------------------')
# nothing goes in, nothing comes out
# function declaration
def add():
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    c = a + b
    print(f'addition of 2 numbers: {c}')

# main program
print('I am executing add function....')
add()

print('------------------------------------------')
# something goes in, nothing comes out

def add(x, y):
    c = x + y
    print(c)


add(2, 3)
add(4, 5)
add(45, 76)


print('------------------------------------------')
# nothing goes in, something comes out

def add():
    x = 6
    y = 8
    z = x + y
    print('This is from print ', z)
    return z


output = add()
print(output)
avg = output / 2
print(avg)


print('------------------------------------------')
# something goes in, somethong comes out

def add(x, y):
    z = x + y
    return z


return_value = add(4, 4)
print(return_value)
print('------------------------------------------')

# something goes in, somethong comes out

def add(x, y):
    z = x + y
    return 'addition of 2 numbes: ', z
print('------------------------------------------')

# mp
for i in range(2):
    n1 = int(input('Enter a 1st number: '))
    n2 = int(input('Enter 2nd number: '))
    return_value = add(n1, n2)
    print(return_value)
    print('------------------------------------------')


# something goes in, somethong comes out

def add(x, y):
    z = x + y
    return 'addition of 2 numbes: ', z


def mul(x, y):
    z = x * y
    return 'Multiplication of 2 numbers : ', z


def div(a, b):
    c = a / b
    return c


# mp
n1 = int(input('Enter a 1st number: '))
n2 = int(input('Enter 2nd number: '))
return_value = add(n1, n2)
print(return_value)
print('------------------------------------------')
returnvalue_mul = mul(n1, n2)
print(returnvalue_mul)
print('------------------------------------------')
return_div = div(n1, n2)
print(return_div)



def print_1to_10(*args):
    for i in args:
        print(i)


num = (1, 2, 3)
print_1to_10(num)


from math import sqrt

num = 36
res = sqrt(num)
print(res)
def adder(*num):
    sum=0
    for n in num:
        sum = sum + n

    print("sum:", sum)

adder(3,5)
adder(4,5,6,7)
adder(4,5,9,7,9)

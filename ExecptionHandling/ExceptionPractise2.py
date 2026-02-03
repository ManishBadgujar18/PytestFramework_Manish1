

try:
    num=int("50")
except Exception as e:
    print(e)
    print(e.__class__)
    print("Invalid input")
else:
    print("Correct Output", num)
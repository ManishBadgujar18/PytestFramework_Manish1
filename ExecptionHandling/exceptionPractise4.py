

def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print(e)
        print(e.__class__)
        return "Division by zero not allowed"

print(divide(10, 2))
print(divide(5, 0))


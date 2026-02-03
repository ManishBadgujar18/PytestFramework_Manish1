

try:
    num = int("abc")   # invalid conversion
except ValueError:
    #print(e.__class__)
    print("Error:")

except NameError:
    print("Mention Name Error:")




try:
    x = 3 / 0

except Exception as e:
    print("Can't divide the number with Zero- ", e)
    print(e.__class__)



try:
    file = open("sample.txt", "r")
    data = file.read()
except Exception as e:
    print(e)
    print(e.__class__)
    print("File not found")
finally:
    print("Closing file (if opened)")

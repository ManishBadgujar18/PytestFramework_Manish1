

try:
    with open("file.log", 'w') as file:
        read_data = file.write('hi ,ijiji')
except:
    print("Couldn't open file.log")
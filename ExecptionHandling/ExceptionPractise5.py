
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age is: {age}")

# try:
#     check_age(5)
# except ValueError as e:
#     print(f"Error: {e}")

check_age(-5)
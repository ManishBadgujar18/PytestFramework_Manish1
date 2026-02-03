country_codes = {'India': 'IN', 'Australia': 'AU', 'Singapore': 'SG', 'Sweden': 'SW'}

for i in country_codes.values():
    print(i)

d = {1: 'Geeks', 2: 'For', 'age': 22}

# Iterate over keys
for key in d:
    print(key)
print('--------------------------\n')
# Iterate over values
for value in d.values():
    print(value)
print('--------------------------\n')
# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")
    print('{} : {}'.format(key, value))

sample_str = 'banana'
str_count = {}

for character in sample_str:
    if character not in str_count:
        str_count[character] = 1  # {A=1, p:1}
        print(str_count)
    else:
        str_count[character] = str_count.get(character, 0) + 1

print(str_count)

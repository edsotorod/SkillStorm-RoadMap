'''
Topic - Conditions

# weather project
uv_index = 100
precipitation = 75
temperature = 40
is_cloudy = True

if uv_index > 10:
  print("Bring sunscreen")

if precipitation > 50 and temperature <= 32:
  print("It's likely to snow")
elif precipitation > 50 and temperature >= 33:
  print("It's likely to rain")
else:
  print("It's not likely to snow")

print("Finished")
'''

'''
Topic - Loops

# while loop : number of iterations NOT known
number = 2000

# exit condition
while number > 1000:
  number = number * 2
  if number > 100000:
    break
  print(number)

print("Finished")
'''

'''
Topics - List

# List : storing multiple related values in same variable
weekly_temp = [45, 67, 90, 45, 75, 80]
# index:        0   1   2   3   4   5

# slicing the list
print(weekly_temp[2:])
print(weekly_temp)

weekly_temp[2] = 60
print(weekly_temp)

for temp in weekly_temp:
  temp = (temp - 32) * (5/9)
  print(int(temp))
'''

'''
Topic - Tuple

# tuple is an immutable list
lotto_numbers = (32, 35, 76, 2, 20)

lotto_numbers[2] = 90
'''

# Dictionary stores key-value pair (entries / entry)
user_dictionary = {
  "danp": "Dan Pickles",
  "howie": "Howard Johnson"
}

username = input("Add a Username: ")
name = input("What is the user's full name? ")

user_dictionary[username] = name
print(user_dictionary[username])

search = input("Search by username: ")
print(user_dictionary.get(search, "Value not found"))
from helper import validate_and_execute, days_to_units
# import helper
# from helper import *
# import helper as h

print(days_to_units(22))
print(days_to_units(30))
print(days_to_units(40))

while True:
    user_input = input("hey user, enter a number of days and I will convert it to hours!\n")
    validate_and_execute(user_input)

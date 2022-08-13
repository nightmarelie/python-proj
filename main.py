calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_units(days):
    if days > 0:
        return f"{days} days are {(days * calculation_to_seconds)} {name_of_unit}"
    elif days == 0:
        return "you entered a 0, please enter a valid positive number"


print(days_to_units(22))
print(days_to_units(30))
print(days_to_units(40))

user_input = input("hey user, enter a number of days and I will convert it to hours!\n")
if user_input.isdigit():
    days = int(user_input)
    print(days_to_units(days))
else:
    print('sorry it is not working')


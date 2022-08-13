calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_units(days):
    if days > 0:
        return f"{days} days are {(days * calculation_to_seconds)} {name_of_unit}"
    else:
        return "you entered a negative value, so no conversion for you!"


print(days_to_units(22))
print(days_to_units(30))
print(days_to_units(40))

days = int(input("hey user, enter a number of days and I will convert it to hours!\n"))

days_to_units(days)
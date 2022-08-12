calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_units(days):
    print(f"{days} days are {(days * calculation_to_seconds)} {name_of_unit}")


days_to_units(20)
days_to_units(30)
days_to_units(40)

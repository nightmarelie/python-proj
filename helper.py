calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_units(days):
    return f"{days} days are {(days * calculation_to_seconds)} {name_of_unit}"


def validate_and_execute(user_input):
    try:
        days = int(user_input)
        if user_input.isdigit():
            # we want to do conversion only for positive integers
            """if days > 0:
                print(days_to_units(days))"""
            if days > 0:
                print(days_to_units(days))
            else:
                return "you entered a 0, please enter a valid positive number"
        else:
            print('sorry it is not working')
    except ValueError:
        print("you get value error! Don't ruin my program!")
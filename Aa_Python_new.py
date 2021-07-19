# How many seconds there are in 20 days


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 *60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:

        user_input_number = int(days_and_units_dictionary["days"])

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_units_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered zero , please enter valid positive number")
        else:
            print("You entered a negative number, no conversion for you")
    except ValueError:
        print("your input is not a valid number ")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days and conversion unit! \n")
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_units_dictionary = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(days_and_units_dictionary)
    validate_and_execute()
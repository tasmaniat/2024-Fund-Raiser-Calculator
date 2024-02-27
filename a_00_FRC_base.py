# import libraries

# Fuctions go here

# checks that input is either a float or an
# integer that is more than zero. Takes in custom error message
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <=0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Checks that user has entered yes / no to question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")

# main rountine goes here



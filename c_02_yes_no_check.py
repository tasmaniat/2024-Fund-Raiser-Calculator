# Function go here...
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


# Main Routine goes here...
show_instructions = yes_no("Have you played the "
                           "game before?  ")
print("you chose {}".format(show_instructions))
print()
having_fun = yes_no("Are you having fun? ")
print("you said {} to having fun".format(having_fun))

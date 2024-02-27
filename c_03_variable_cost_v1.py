import pandas

# checks users enter an integer to a given question
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")

# checks that user response is not blank
def not_blank(question, error):

    valis = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again \n".format(error))
            continue

            return response

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# main rountine goes here

#  set up dictionaries and lists

item_list = []
quantiy_list = []
price_list =[]


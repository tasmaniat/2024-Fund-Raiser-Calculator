# Function go here...
# check user answers yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


# Display instructions
def show_instructions():

    print('''\n
    * * * * * Instructions * * * * *
    
    This program will ask you for...
    - The name of hte product you are selling
    - How many items you plan on selling
    - The costs for each component of the product
    - How much money you want to make
    
    It will then output an itemised list of the costs
    with subtotals for the variable and fixed costs.
    Finally it will tell you how mush you should sell
    each item for to reach you profit gaol.
    
    The data will also be written to a text file which 
    has the same name as the product.
    
    * * * * * Program Launched! * * * * *''')


# Main Routine goes here...
played_before = yes_no("Have you played the "
                       "game before?  ")

if played_before == "no":
    show_instructions()
print()


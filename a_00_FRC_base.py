# import libraries
import pandas
import math
from datetime import date


# Functions go here

# checks that input is either a float or an
# integer that is more than zero. Takes in custom error message
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
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
            print("Please answer either yes or no...")
            print()


# checks that user response is not blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again \n".format(error))
            continue

        return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Gets expenses, returns list which has
# the data frame and sub_total
def get_expenses(var_fixed):
    #  set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity adn price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ",
                              "The component name can't be "
                              "blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity:",
                                 "The amount must be a whole number"
                                 "more than zero",
                                 int)
        else:
            quantity = 1

        price = num_check("How much for a single item? $",
                          "The price must be a number <more "
                          "than 0>", float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub_total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


def expense_string(heading, frame, subtotal):
    expense_heading = "**** {} Costs ****".format(heading)
    expense_frame_txt = pandas.DataFrame.to_string(frame)
    expense_sub_txt = "\n{} Costs: ${:.2f}".format(heading, subtotal)

    return expense_heading, expense_frame_txt, expense_sub_txt


# work out profit goal and total sales required
def profit_goal(total_costs):
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal...
        print()
        response = input("What is your profit goal (eg $500 or 50) ")

        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before tha %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}. "
                                 "ie {:.2f} dollars? ,"
                                 "y / n ".format(amount, amount))

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}%? , "
                                  "y / n".format(amount))

            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# Display instructions
def show_instructions():
    print('''
***** Instructions *****

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
''')


# ******* main routine goes here *******

# Main Routine goes here...
played_before = yes_no("Have you used this program before? ")

if played_before == "no":
    show_instructions()
print("***** Program Launched! *****")

# Get user data
print()
product_name = not_blank("Product name: ", "The product name can't be blank.")

how_many = num_check("How many items will you be producing? ",
                     "The number of items must be a whole "
                     "number more than zero", int)

print()
print("Please enter your variable costs below...")
print("Enter 'xxx' for the item name when done.")
# get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y / n)? ")
print("Enter 'xxx' for the item name when done.")

if have_fixed == "yes":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0
    fixed_frame = ""

# works out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)


# calculate total sales needed to reach goal
sales_needed = all_costs + profit_target

# ASk user for rounding
round_to = num_check("Round to nearst...? $",
                     "Can't be 0", int)

# Calculate recommended price
selling_price = sales_needed / how_many
print("Selling price (un-rounded): "
      "${:.2f}".format(selling_price))
print()
recommended_price = round_up(selling_price, round_to)

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

filename = "MMF_{}_{}_{}".format(year, month, day)

# ***** Printing Area *****

print()
product_heading = "***** Fund Raising - {} - ({}/{}/{}) *****\n".format(product_name, year, month, day)

variable_strings = expense_string("Variable", variable_frame, variable_sub)
variable_heading = variable_strings[0]
variable_frame_txt = variable_strings[1]
variable_sub_txt = variable_strings[2]

if have_fixed == "yes":
    fixed_strings = expense_string("Fixed", fixed_frame, fixed_sub)
    fixed_heading = fixed_strings[0]
    fixed_frame_txt = fixed_strings[1]
    fixed_sub_txt = fixed_strings[2]
else:
    fixed_heading = ""
    fixed_frame_txt = "**** no fixed cost ****"
    fixed_sub_txt = ""

total_cost_heading = "**** Total costs: ${:.2f} ****".format(all_costs)

profit_heading = "\n**** Profit & Sales Target ****"
profit_frame_txt = "Profit Target: ${:.2f}".format(profit_target)
profit_sub_txt = "Total Sales: ${:.2f}".format(all_costs + profit_target)

price_heading = "\n**** Pricing ****"
price_frame_txt = "Minimum Price: ${:.2f}".format(selling_price)
price_sub_txt = "Recommended Price: ${:.2f}".format(recommended_price)

# print()
# print("**** Total costs: ${:.2f} ****".format(all_costs))
#
# print()
# print("**** Profit & Sales Target ****")
# print("Profit Target: ${:.2f}".format(profit_target))
# print("Total Sales: ${:.2f}".format(all_costs + profit_target))
#
# print()
# print("**** Pricing ****")
# print("Minimum Price: ${:.2f}".format(selling_price))
# print("Recommended Price: ${:.2f}".format(recommended_price))

# list holding stuff to print / write to file
to_write = [product_heading, variable_heading, variable_frame_txt, variable_sub_txt,
            fixed_heading, fixed_frame_txt, fixed_sub_txt, total_cost_heading,
            profit_heading, profit_frame_txt, profit_sub_txt,
            price_heading, price_frame_txt, price_sub_txt]

# write to file...
# create file to hold data (add .txt extension)
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()

# Print Stuff
for item in to_write:
    print(item)
    print()

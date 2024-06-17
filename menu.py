# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("Enter the item number from the menu that you want to order: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items:
                    # Store the item name as a variable
                    item_name = menu_items[menu_selection]["Item name"]
                    item_price = menu_items[menu_selection]["Price"]

                    # Ask the customer for the quantity of the menu item
                    quant = input(f"How many {item_name}s would you like? ")

                    # Check that the customer input is a number. If it isn't, set the quantity to 1
                    if quant.isdigit():
                        quant = int(quant)
                    else:
                        print("Invalid quantity. Defaulting to 1.")
                        quant = 1

                    # Append the customer's order to the order list
                    order.append({
                        "Item name": item_name,
                        "Price": item_price,
                        "Quantity": quant
                    })

                    print(f"{quant} {item_name}(s) added to your order.")
                else:
                    # Tell the customer their selection was not valid
                    print(f"Item number {menu_selection} was not valid.")
            else:
                # Tell the customer they didn't select a number
                print("You didn't select a number.")
        else:
            # Tell the customer they didn't select a valid menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").upper()

        # # 5. Check the customer's input
        # match keep_ordering:
        #         # Keep ordering
        #     case 'Y':
        #         place_order = True
        #     case 'N':
        #         place_order = False
        #         print("thanks for the order!!")
        #         break
        #     case _:
        #         print("not valid input")
        # if not place_order:
        #     break   
        if keep_ordering == "Y":
            place_order = True
            break
        elif keep_ordering == "N":
            place_order = False
            print("Thank you for your order!")
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
total_price = 0
for item in order:
    # 7. Store the dictionary items as variables
    item_name = item["Item name"]
    item_price = item["Price"]
    item_quant = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    
    # Items 
    num_item_spaces = 26 - len(item_name)

    # Prices
    str_price = f"${item_price:.2f}"
    num_price_spaces = 5 -len(str_price)

    # Quantity 
    str_quant = str(item_quant)
    num_quant_spaces = 8 - len(f"{str_quant}")

    # 9. Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces
    quant_spaces = " " * num_quant_spaces


    # 10. Print the item name, price, and quantity use the :.2f to format to two decimal places for a clean price 
    print(f"{item_name}{item_spaces}| ${item_price:.2f}{price_spaces}  | {item_quant}{quant_spaces}")



# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_price = sum(item["Price"] * item["Quantity"] for item in order) 

print(f"\nThe total price for the oreder is: ${total_price:.2f}")
# Code authors: Jeremiah E. Ochepo
# Code Title: Shopping Management System
# Program Description: Allows users to check the price of multiple items
# Last modified: 7/5/2019

import json

# Declare myDict in the global scope
myDict = {}


def plainText_to_dict():
    # Step 1. Import plainText convert to dict
    myFileName = 'dictionary.txt'

    with open(myFileName) as text_string:
        for line in text_string:
            command, description = line.strip().split(' ', 1)
            myDict[command] = description.strip()

    print(f'{myDict}\n')


def add_item():
    try:
        item_name = input("Please enter item name: ").title()
        x = myDict[item_name]
    except KeyError:
        print(item_name, "cannot be found. Try again!")
        return None

    item_qty = input('Quantity? ')

    try:
        val = float(item_qty)
    except ValueError:
        print(item_qty, "is not a number. Try again!")
        return None

    unit_price = float(myDict[item_name])
    final_price = unit_price * float(item_qty)

    print("Item added successfully!")
    return {
        'item_name': item_name,
        'item_qty': item_qty,
        'unit_price': unit_price,
        'discount': 0,
        'sale_tax': 0.04,
        'final_price': final_price
    }


def remove_item(cart, item_name):
    for item in cart:
        if item['item_name'] == item_name:
            cart.remove(item)
            print(f"{item_name} removed from the cart.")
            return True
    print(f"{item_name} not found in the cart.")
    return False


def update_item(cart, item_name):
    for item in cart:
        if item['item_name'] == item_name:
            item_qty = input(f"Enter new quantity for {item_name}: ")
            try:
                val = float(item_qty)
                item['item_qty'] = item_qty
                item['final_price'] = item['unit_price'] * float(item_qty)
                print(f"{item_name} updated successfully.")
                return True
            except ValueError:
                print(item_qty, "is not a number. Try again!")
                return False
    print(f"{item_name} not found in the cart.")
    return False


def main():
    plainText_to_dict()

    discription = "SHOPPING MANAGEMENT SYSTEM"
    ans_key = "Users Instruction:\n\tType 'Add' to add a new item to the cart\n\tType 'Done' to see item summary\n\tType 'Remove' to remove an item from the cart\n\tType 'Update' to update the quantity of an item in the cart\n\tType 'Quit' to quit the program"
    final_msg = "Dear Customer, here is your results:"
    cart_summary = "CART SUMMARY"

    print(discription)
    print(ans_key)

    user_response = {}
    cart = []
    cart_total = 0
    searched_total = 0
    sale_tax = 0.04
    discount = 0

    while user_response != "quit":
        user_response = input("\nEnter ('Add' or 'Done' or 'Remove' or 'Update' or 'Quit'): ")
        user_response = user_response.lower()

        if user_response == 'add':
            item = add_item()
            if item:
                cart.append(item)

        elif user_response == 'remove':
            item_name = input("Enter the name of the item to remove: ").title()
            remove_item(cart, item_name)

        elif user_response == 'update':
            item_name = input("Enter the name of the item to update: ").title()
            update_item(cart, item_name)

        elif user_response == "done":
            final_price_total = (sale_tax * cart_total) + cart_total + discount
            print(cart_summary)
            print('Item searched was:            ', searched_total)
            print('Discount:                     ', discount, '% off')
            print('Price without sales tax:       $', round(cart_total, 2))
            print('Price with sales tax included: $', round(final_price_total, 2))

            print("\nCART DETAILS:")
            for item in cart:
                print(f"\nItem Name:  {item['item_name']}")
                print(f"Quantity:   {item['item_qty']}")
                print(f"Unit Price:  ${item['unit_price']}")
                print(f"Discount:   {item['discount']}% off")
                print(f"Sale tax:   {item['sale_tax']}%")
                print(f"Final price: ${item['final_price']}")

            break

        elif user_response == "quit":
            print('See you next time.. Bye! Bye!')
            exit()


if __name__ == "__main__":
    main()

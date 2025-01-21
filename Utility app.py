Vending_machine_title = """   
                                        ▄▄                                           ▄▄         
▀████▀   ▀███▀                        ▀███                                     ██    ██         
  ▀██     ▄█                            ██                                     ██               
   ██▄   ▄█    ▄▄█▀██▀████████▄    ▄█▀▀███   ▄██▀██▄▀████████▄█████▄  ▄█▀██▄ ██████▀███  ▄██▀██ 
    ██▄  █▀   ▄█▀   ██ ██    ██  ▄██    ██  ██▀   ▀██ ██    ██    ██ ██   ██   ██    ██ ██▀  ██ 
    ▀██ █▀    ██▀▀▀▀▀▀ ██    ██  ███    ██  ██     ██ ██    ██    ██  ▄█████   ██    ██ ██      
     ▄██▄     ██▄    ▄ ██    ██  ▀██    ██  ██▄   ▄██ ██    ██    ██ ██   ██   ██    ██ ██▄    ▄
      ██       ▀█████▀████  ████▄ ▀████▀███▄ ▀█████▀▄████  ████  ████▄████▀██▄ ▀████████▄█████▀ 
                                                                                                
                                                                                                
                                           """   
   
def display_header():   
  print(Vending_machine_title)   
   
# To display the Vending machine title, call the display_header function.  
display_header()  
  
# Function to present the vending machine header  
def display_header():   
    
  # Output the title of the vending machine   
  print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")   
  print("*       WELCOME TO VENDOMATIC            *")   
  print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")   
  print("*    Enjoy discounts on purchases over £10!    *")   
  print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")   
   
# Method to showcase the vending machine selections   
def display_menu():   
  # Present the vending machine header   
  display_header()   
  # Print the menu of the vending machine   
  print("*  Take a look at the menu...      *")   
  print("*  J4. Juice                 *")   
  print("*  C1. Chips                 *")   
  print("*  C2. Cold Drinks             *")   
  print("*  C0. Cold Coffee             *")   
  print("*  H6. Hot Coffee              *")   
  print("*  W7. Water                 *")   
  print("*  C5. Chocolate              *")   
  print("*  C8. Cookies                *")   
  print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")   
   
# Function to select an item from the menu   
def select_item():   
  # Loop until a valid choice is made   
  while True:   
    # Direct the user to input the code for their item of choice.  
    choice = input("Enter the code of your chosen item: ").upper()   
    # Have to check if the code chosen by user is valid  
    if choice in ["J4", "C1", "C2", "C0", "H6", "W7", "C5", "C8"]:   
      # Return the chosen item   
      return choice   
    else:   
      # Output an error alert when the selection is not valid  
      print("Invalid choice. Please try again.")   
   
# Function to pick a flavor based on the selected item   
def select_flavor(choice):   
  # List of flavors corresponding to each item   
  flavors = {   
    "J4": {   
      "DD": {"name": "Orange", "price": 5.50, "stock": 2},   
      "EE": {"name": "Apple", "price": 4.75, "stock": 4},   
      "FF": {"name": "Mango", "price": 5.00, "stock": 1}   
    },   
    "C1": {   
      "AA": {"name": "Cheetos", "price": 6.00, "stock": 5},   
      "BB": {"name": "Pringles", "price": 5.50, "stock": 3},   
      "CC": {"name": "Takis", "price": 9.25, "stock": 0}   
    },   
    "C2": {   
      "GG": {"name": "Pepsi", "price": 8.25, "stock": 5},   
      "HH": {"name": "Red Bull", "price": 10.50, "stock": 3},   
      "II": {"name": "Sprite", "price": 7.75, "stock": 2}   
    },   
    "C0": {   
      "JJ": {"name": "Iced Latte", "price": 6.00, "stock": 4},   
      "KK": {"name": "Iced Macchiato", "price": 7.25, "stock": 1},   
      "LL": {"name": "Iced Mocha", "price": 10.50, "stock": 0}   
    },   
    "H6": {   
      "MM": {"name": "Espresso", "price": 5.75, "stock": 3},   
      "NN": {"name": "Americano", "price": 9.00, "stock": 2},   
      "OO": {"name": "Cappuccino", "price": 7.25, "stock": 1}   
    },   
    "W7": {   
      "PP": {"name": "Still Water", "price": 3.50, "stock": 5},   
      "QQ": {"name": "Sparkling Water", "price": 5.75, "stock": 4}   
    },   
    "C5": {   
      "RR": {"name": "Lindt", "price": 12.50, "stock": 5},   
      "SS": {"name": "Ferrero Rocher", "price": 5.00, "stock": 3},   
      "TT": {"name": "Toblerone", "price": 4.00, "stock": 2}   
    },   
    "C8": {   
      "UU": {"name": "Chocolate Chip Cookies", "price": 6.00, "stock": 5},   
      "VV": {"name": "Oatmeal Raisin Cookies", "price": 3.25, "stock": 3},   
      "WW": {"name": "Nutella Stuffed Cookies", "price": 4.50, "stock": 2}   
    }   
  }   
  # Display the header of the vending machine   
  display_header()   
  # Print the flavors of the chosen item   
  print("*  Flavors:                  *")   
  for code, flavor in flavors[choice].items():   
    # Check if the flavor is in stock   
    if flavor["stock"] > 0:   
      # Print the flavor and its price   
      print(f"*  {code}. {flavor['name']} - £{flavor['price']:.2f}   *")   
    else:   
      # Print a message if the flavor is out of stock   
      print(f"*  {code}. {flavor['name']} - Out of stock   *")   
  print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")   
  # Loop until a valid flavor is chosen   
  while True:   
    # Ask the user to enter the number of their chosen flavor   
    flavor_choice = input("Enter the letter of your chosen flavor: ")   
    # Check if the flavor choice is valid   
    if flavor_choice in flavors[choice]:   
      # Check if the flavor is in stock   
      if flavors[choice][flavor_choice]["stock"] > 0:   
        # Return the chosen flavor   
        return flavors[choice][flavor_choice]   
      else:   
        # Print an error message if the flavor is out of stock   
        print("Sorry, but this item isn’t available right now. Please choose another.")   
    else:   
      # Print an error message if the flavor choice is invalid   
      print("Invalid choice. Please try again.")   
   
# Function to dispense the chosen item   
def dispense_item(item):   
  # Display the header of the vending machine   
  display_header()   
  # Print a message to dispense the item   
  print(f"*  Dispensing {item['name']}...        *")   
  print("*  Don’t forget to collect your item from the vending machine.  *")   
  print("")   
  # Simulate dispensing the item   
  print("*  Item dispensed successfully.        *")   
  print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")   
   
# Function to calculate the discount   
def calculate_discount(overall_cost):   
  # Calculate the discount based on the total cost   
  if overall_cost > 10:   
    discount = 0.10   
  elif overall_cost >= 5:   
    discount = 0.05   
  else:   
    discount = 0   
  return discount   
   
# Function to pay for the chosen items   
def pay(overall_cost, items):   
  # Display the header of the vending machine   
  display_header()   
  # Calculate the discount   
  discount = calculate_discount(overall_cost)   
  discount_amount = overall_cost * discount   
  final_amt_with_discount = overall_cost - discount_amount   
  # Print the total cost and discount   
  print(f"*  Your total is £{overall_cost:.2f}.             *")   
  print(f"*  Discount: {discount*100}% = £{discount_amount:.2f}  *")   
  print(f"*  Total with discount: £{final_amt_with_discount:.2f}  *")   
  print("")   
  # Loop until a valid payment method is chosen   
  while True:   
    # Ask the user to choose a payment method   
    payment_method = input("Which payment option do you prefer: cash, card, or coins? ")   
    # Confirm the payment method's validity  
    if payment_method.lower() == "cash":   
      # Loop until a valid amount is entered   
      while True:   
        try:   
          # Request the user to specify the amount for payment   
          amount = float(input("Enter the amount you'd like to pay: £"))   
          # Check if the amount is sufficient   
          if amount < final_amt_with_discount:   
           # Output an error alert when the amount is not sufficient   
           print("You don't have enough money. Please try again.")   
          else:   
           # Calculate the change   
           change = amount - final_amt_with_discount   
           # Print the change   
           print(f"*  Your change is £{change:.2f}.     *")   
           print("*  Payment successful.            *")   
           # Dispense the items   
           for item in items:   
             dispense_item(item)   
           return   
        except ValueError:   
          # Print an error message if the amount is invalid   
          print("Please enter a valid amount and try again.")   
    elif payment_method.lower() == "card":   
      # Print a message to indicate payment success   
      print("*  Payment successful.        *")   
      # Dispense the items   
      for item in items:   
        dispense_item(item)   
      return   
    elif payment_method.lower() == "coin":   
      # Print a message to insert coins   
      print("*  Please insert coins.        *")   
      # Initialize the total amount   
      final_amt = 0   
      # Loop until the total amount is sufficient   
      while final_amt < final_amt_with_discount:   
        try:   
          # Ask the user to enter the coin value   
          coin = float(input("Please provide the coin value. (e.g. 0.50, 1.00, etc.): £"))   
          # Add the coin value to the total amount   
          final_amt += coin   
          # Show the overall amount   
          print(f"*  Total amount: £{final_amt:.2f}    *")   
          # Check if the overall amount is sufficient   
          if final_amt >= final_amt_with_discount:   
           # Calculate the change   
           change = final_amt - final_amt_with_discount   
           # Print the change   
           print(f"*  Your remaining amount is £{change:.2f}.     *")   
           print("*  Payment processed successfully.           *")   
           # Dispense the items   
           for item in items:   
             dispense_item(item)   
           return   
        except ValueError:   
          # Print an error message if the coin value is invalid   
          print("Incorrect coin value. Please retry.")   
    else:   
      # Print an error message if the payment method is invalid   
      print("Payment method not recognized. Please try again.")   
   
# Main function   
def main():   
  # Initialize the total cost and items   
  overall_cost = 0   
  items = []   
  # Keep looping until the user indicates they want to stop.
  while True:   
    # Print the menu   
    display_menu()   
    # Ask the user to choose an item   
    choice = select_item()   
    # Ask the user to choose a flavor   
    flavor = select_flavor(choice)   
    # Display a message to confirm the selected item.   
    print(f"*  You have selected {flavor['name']}.     *")   
    # Suggest further options related to the chosen item.  
    if choice == "C0" or choice == "H6":   
      print("*  Would you like to add some cookies to your coffee? (yes/no) *")   
      cont = input().lower()   
      if cont == "yes":   
       cookie_cat = "C8"   
       variety_cookie = select_flavor(cookie_cat)   
       print(f"*  You have selected {variety_cookie['name']}.     *")   
       overall_cost += variety_cookie['price']   
       items.append(variety_cookie)   
    elif choice == "C5":   
      print("*  Would you like to add anything to your chocolate? (yes/no) *")   
      cont = input().lower()   
      if cont == "yes":   
       print("*  Please select an item to add: *")   
       print("*  C1. Chips                 *")   
       print("*  J4. Juice                 *")   
       print("*  C2. Cold Drinks             *")   
       print("*  W7. Water                 *")   
       sugg_offer = input("Enter the code of your chosen item: ").upper()   
       if sugg_offer in ["C1", "J4", "C2", "W7"]:   
        add_flavor = select_flavor(sugg_offer)   
        print(f"*  You have selected {add_flavor['name']}.     *")   
        overall_cost += add_flavor['price']   
        items.append(add_flavor)   
    elif choice == "J4":   
      print("*  Would you like to add some chips to your juice? (yes/no) *")   
      cont = input().lower()   
      if cont == "yes":   
       chip_choice = "C1"   
       chip_option = select_flavor(chip_choice)   
       print(f"*  You have selected {chip_option['name']}.     *")   
       overall_cost += chip_option['price']   
       items.append(chip_option)   
    # Add the item to the overall cost and item count.  
    overall_cost += flavor['price']   
    items.append(flavor)   
    # See if the user wants to add another item to their selection.  
    cont = input("Why stop here? Add another item to your order! (yes/no): ")   
    # check if the user wants to stop   
    if cont.lower() == "no":   
      break   
  # Payment for items   
  pay(overall_cost, items)   
  # Thankyou message for the user to use my vending machine 
  print("*  Thanks for vending with Vendomatic! Come back soon! :)  *")   
  print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")   
   
# Run the main function   
if __name__ == "__main__":   
  main()

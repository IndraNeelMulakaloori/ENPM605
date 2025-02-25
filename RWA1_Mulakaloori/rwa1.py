import datetime  # Import the datetime module (you'll need this for the timestamp)

def validation_product_str(products : dict, prompt_message: str, flag = False):
    '''
    Validates user input to ensure it's a product name that exists in the inventory.

    Args:
        products (dict): A dictionary representing the product inventory, where keys are product names.
        prompt_message (str): The message to display to the user prompting for input.
        flag (bool, optional): A flag indicating whether the product name should be added to the inventory if not found. Defaults to False.

    Returns:
        tuple: A tuple containing:
            - str: The validated product name (case-insensitive and stripped of whitespace).
            - bool: True if the product was found, False otherwise.
    '''

    while True:
        ## Input for the product 
        product = input(prompt_message)
        ## product keys lookup is used to map the key of product with 
        # it's case insensitvity for better lookups
        product_keys_lookup = {key.strip().lower() : key for key in products}
        
        ## if product not in product_keys_lookup
        ## print error 
        if product.strip().lower()  not in product_keys_lookup:
            print("Product Doesn't Exist!!!!")
            ## if the product comes from add_product method it
            ## it needs to addedd in the Inventory
            if flag:
                print("Should Add in the Inventory")
                return product.title(),False
        ## if found return the product and check flag
        else:
            return product_keys_lookup[product.strip().lower()],True
            


def validation_integers(prompt_message: str,type= "Quantity"):
    '''
    Validates user input to ensure it's a non-negative integer.

    Args:
        prompt_message (str): The message to display to the user prompting for input.
        type (str, optional): The type of integer being requested (e.g., "Quantity", "Choice"). 
                             Defaults to "Quantity".  This is used in error messages.

    Returns:
        int: The validated non-negative integer value.
    '''
    while True:
        try:
            integer_value = int(input(prompt_message)) # Get user input
            if integer_value < 0:
                print(f"Error!!! {type} cannot be negative!") # Print error if the integer_value is negative
            else : 
                return integer_value # Else return the integer_value
        
        except ValueError: # Raise an exception if non integer is found
                print(f"Error!!! Enter a valid {type})")
    

def validation_float(prompt_message: str):
    '''
    Validates user input to ensure it's a non-negative float.

    Args:
        prompt_message (str): The message to display to the user prompting for input.

    Returns:
        float: The validated non-negative float value.
    '''
    while True:
        try:
            float_value = float(input(prompt_message)) # Get user input and attempt to convert to float
            if float_value < 0.0:
                print("Error!!! Price cannot be negative!")  # Error if the float is negative
            else : 
                return float_value # Return the validated float if it's non-negative
            
        except ValueError:
                print("Error!!! Enter a valid float value") # Return the validated float if it's non-negative
    
def category_check(categories : set, prompt_message: str):
    '''
    Validates user input to ensure it's an existing category.

    Args:
        categories (set): A set containing the valid category names (all lowercase).
        prompt_message (str): The message to display to the user prompting for input.

    Returns:
        str: The validated category name (capitalized).
    '''
    while True:
        category = input(prompt_message) # Get user input for the category
        if category.lower() not in categories:  # Check if the category exists (case-insensitive)
            print(f"Error!!!! Category doesn't exist. Enter a valid category : {categories}") # Print error message with valid categories
        else: 
            return category.capitalize()  # Return the category name (capitalized)

def add_new_product(products : dict, categories : set):
    '''
    Adds a new product to the inventory.

    Args:
        products (dict): A dictionary representing the product inventory.
        categories (set): A set containing the valid category names.
    '''
    name,check = validation_product_str(products,("Name: "),True) # Get and validate the product name, allowing it to be added if not found
    if check:  # If the product already exists
        print("Product Exists!! Change the parameters...") # Call edit_product to modify the existing product
        edit_product(name,products)
        return  # Exit the add_new_product function since the product already exists and was potentially edited

    price = validation_float("Price: ") # Get and validate the price
    quantity = validation_integers("Quantity: ")  # Get and validate the quantity
    category = category_check(categories,"Category: ") # Get and validate the category
    suppliers = list(input("Suppliers (comma-seperated): ").split(", ")) # Get suppliers and split into a list
        
    products[name] = { # Add the new product to the inventory
        "Price" : price,
        "Quantity" : quantity,
        "Category" : category.capitalize(), # Store the capitalized category
        "Suppliers" : suppliers
    }
    
    print(f"Product added successfully! {datetime.datetime.now()}")  # Print success message with timestamp

def remove_product(product : str ,products : dict, flag = False):
    '''
    Removes a specified quantity of a product or the entire product from the inventory.

    Args:
        product (str): The name of the product to remove.
        products (dict): The dictionary representing the product inventory.
        flag (bool, optional): If True, removes the entire product; if False (default), removes a specified quantity. Defaults to False.
    '''
    if not flag: # Remove a specific quantity
        while True:
                quantity = validation_integers("Enter Quantity: ") # Get quantity to remove
                    
                if products[product]['Quantity'] - quantity < 0: # Check if enough quantity exists
                    print("Error!!!!!\nQuantity of Product is less than required quantity. Couldn't Remove it.\nEnter details again")
                else:
                    break # Exit the loop if enough quantity exists
                    
        products[product]['Quantity'] -= quantity  # Decrease the product quantity
    
    # if flag and product is zero check this
    if products[product]['Quantity'] == 0:  #If quantity becomes zero, remove product
            products.pop(product)
        
    print(f"Product removed successfully! {datetime.datetime.now()}")
     
def edit_product(product_name : str, products:dict):
    '''
    Edits an existing product's details in the inventory.

    Args:
        product_name (str): The name of the product to edit.
        products (dict): The dictionary representing the product inventory.
    '''
    print("Current details from dictionary")
    for field,data in products[product_name].items():  # Display current product details
        print(f"- {field} : {data}")
        
    print("\nWhat would you like to edit?\n1. Price \n2. Quantity \n3. Suppliers \n4. Multiple fields ")
    user_choice = validation_integers("Enter a Choice: ", "Choice")  # Get user's edit choice
    
    match user_choice:
        
        case 1: # Edit Price
            user_price = validation_float("Enter New Price: ")
            products[product_name]['Price'] = user_price
            
        case 2: # Edit Quantity
            user_quantity = validation_integers("Enter New Quantity: ")
            products[product_name]['Quantity'] = user_quantity
            
            if user_quantity == 0: # If quantity is set to 0, remove the product
                remove_product(product_name,products,True) # Call remove_product with flag set to True
                return # Exit the edit function since the product was removed
            
        case 3:
            user_supplier = input("Enter a New Supplier: ")
            # Check to prevent duplicates
            if user_supplier not in products[product_name]['Suppliers']:
                products[product_name]['Suppliers'].append(user_supplier)
            else:
                print(f"{user_supplier} is already listed as a supplier.")
            
        case 4:  # Edit Multiple Fields
            while True: # Loop for multiple field edits
                print("Select the fields to update!")
                print("\nWhat would you like to edit?\n0. Stop\n1. Price \n2.Quantity \n3. Suppliers")
                
                field_choice = validation_integers("Enter a Choice: ", "Choice") # Enter choice within multiple fields
                
                if field_choice == 0: # Enter 0 to break
                    break    
                
                elif field_choice == 1: # Enter 1 to edit price field 
                    user_price = validation_float("Enter New Price: ")
                    products[product_name]['Price'] = user_price
                    
                elif field_choice == 2: # Enter 2  to edit integers field
                    user_quantity = validation_integers("Enter New Quantity: ")
                    products[product_name]['Quantity'] = user_quantity
                    
                elif field_choice == 3: # Enter 3 to edit supplier field
                    user_supplier = input("Enter a New Supplier: ")
                    products[product_name]['Suppliers'].append(user_supplier) 
                    
                else: # if not enter a valid choice (in mulitple fields choice)
                    print("Enter a valid choice(0-3)!!!!")
                    
        case _: # Enter a valid choice
            print("Enter a valid choice(1-4)!!!!!")
    # Timestamp tracking
    print(f"Product Updated successfully! {datetime.datetime.now()}")
    

def search_product(products: dict, categories : set):
    '''
    Searches for products in the inventory based on different criteria.

    Args:
        products (dict): The dictionary representing the product inventory.
        categories (set): The set of valid product categories.
    '''
    print("Search by: ")
    print("1. Price range \n2. Category \n3. Supplier ")
    
    # Validate user_choice to int
    user_choice = validation_integers("Enter choice(1-3): ","Choice")
    
    match user_choice:
        case 1:  # Search by Price Range with min and max Range
            min_range = validation_integers("Enter minimum price: ", "Price") 
            max_range = validation_integers("Enter maximum price: ", "Price") 

            print("Results: ")
            
            ## Search for items in the dictionary within the price range and print them
            for product, product_info in products.items():
                if product_info['Price'] >= min_range and product_info['Price'] <= max_range:
                    print(f"- {product} (${product_info['Price']}) - {product_info['Category']} - {product_info['Quantity']} units")

        case 2:  # Search by Category
            print(f"Select Category: {categories}")
            user_prompted_category = category_check(categories, "Enter Category: ")
            print(f"{user_prompted_category} results: ")

            ## Search for items in the dictionary for the Category
            for product, product_info in products.items():
                if product_info['Category'].replace(" ", "").lower() == user_prompted_category.replace(" ", "").lower(): #Whitespace removed for better comparison
                    print(f"- {product} (${product_info['Price']}) - {product_info['Quantity']} units")

        case 3:  # Search by Supplier
            user_prompted_supplier = input("Enter Supplier : ")
            print(f"{user_prompted_supplier} Results: ")

            ## Search for items in the Supplier for the Category
            for product, product_info in products.items():
                for supplier in product_info['Suppliers']:
                    if supplier.strip().lower() == user_prompted_supplier.strip().lower(): #Whitespace removed for better comparison
                        print(f"- {product} (${product_info['Price']}) - {product_info['Category']} - {product_info['Quantity']} units")
                        break #Break after finding the supplier for a product to avoid duplicate printing if a product has multiple suppliers
                    
        case _:  # IF not redirect for default case
            print("Enter a valid choice(1-3)!!!!!")
    
    

def report(products : dict, categories : set):
    '''
    Generates and prints an inventory report, including total inventory value,
    low stock alerts, and item counts per category.

    Args:
        products (dict): The dictionary representing the product inventory.
        categories (set): The set of valid product categories.
    '''
    
    total_inventory_value = 0 # intialize total_inventory_value
    categories_count = {key.capitalize(): 0 for key in categories}  # Initialize category counts
    low_stock_alert = {}
    low_stock_flag = False # Flag to track if any low stock items exist
    
    ## One Pass Iteration for Efficency  
    for product, product_info in products.items():
        total_inventory_value += product_info['Price'] * product_info['Quantity'] # Calculate total inventory value
        categories_count[product_info['Category']] += 1  # Count items per category
        if product_info['Quantity'] < 5:
            low_stock_flag = True 
            low_stock_alert.update({product : product_info['Quantity']})   # Add low stock item to the dictionary

    print(f"Total Inventory Value : ${total_inventory_value}")
    
    print("Low Stock Alert (< 5 units): ")
    if low_stock_flag:   # Print low stock alerts only if any exist
        for product,value in low_stock_alert.items():
            print(f"- {product}: {value}")
    else : # Else print NOne
        print(None)
    
    ## Print items per category
    print("\nItems per category:")
    for category, quantity in categories_count.items():
        print(f"{category}: {quantity} items")


if __name__ == "__main__":
    # Categories and Products Data Structures
    # Categories are stored in a set for Easier access
    categories={"electronics", "food", "books"}
    
    # Products are stored in a Dictionary 
    products = {
            "Smart Watch":{
                          "Price" : 200.00,
                          "Quantity" : 25,
                          "Category" : "Electronics",
                          "Suppliers" : ["Samsung", "Best World", "Tech world"]},
            "Microwave Oven":{
                          "Price" : 359.00,
                          "Quantity" : 15,
                          "Category" : "Electronics",
                          "Suppliers" : ["Samsung", "Walmart", "Tech World"]},
            "Televison":{
                          "Price" : 420.39,
                          "Quantity" : 20,
                          "Category" : "Electronics",
                          "Suppliers" : ["Sony", "Samsung", "Apple", "Oneplus"]},
            "Iphone 16":{
                          "Price" : 2250.00,
                          "Quantity" : 75,
                          "Category" : "Electronics",
                          "Suppliers" : ["Apple","SM Disturbtion", "Walmart", "Best World"]},
            "Electric Geyser":{
                          "Price" : 200.00,
                          "Quantity" : 5,
                          "Category" : "Electronics",
                          "Suppliers" : ['Samsung', "Best World", "Tech world"]},
            "Python Basics" :{ 
                    "Price": 30.00, 
                    "Quantity": 50, 
                    "Category" : "Books",
                    "Suppliers": ["Amazon", "Barnes & Noble"]},
            "Data Science Handbook" :{ 
                    "Price": 45.00, 
                    "Quantity": 40, 
                    "Category" : "Books",
                    "Suppliers": ["O'Reilly", "Packt", "Amazon"]},
            "Robotics Fundamentals" :{ 
                    "Price": 60.00, 
                    "Quantity": 20,
                    "Category" : "Books", 
                    "Suppliers": ["MIT Press", "Springer"]},
            "Deep Learning with Python" :{ 
                    "Price": 55.00, 
                    "Quantity": 35, 
                    "Category" : "Books",
                    "Suppliers": ["Amazon", "Packt"]},
            "Mathematics for Machine Learning" :{ 
                    "Price": 48.00, 
                    "Quantity": 25, 
                    "Category" : "Books",
                    "Suppliers": ["Springer", "Barnes & Noble"]},
            "Organic Honey" :{ 
                   "Price": 12.00, 
                   "Quantity": 100, 
                    "Category" : "Food",              
                   "Suppliers": ["Whole Foods", "Trader Joe's"]},
            "Almond Butter" :{
                   "Price": 15.00, 
                   "Quantity": 80, 
                   "Category" : "Food",
                   "Suppliers": ["Kirkland", "Costco"]},
            "Dark Chocolate" :{
                   "Price": 8.00, 
                   "Quantity": 150,
                    "Category" : "Food",
                   "Suppliers": ["Lindt", "Ghirardelli", "Hershey's"]},
            "Olive Oil" :{
                   "Price": 20.00, 
                   "Quantity": 60, 
                   "Category" : "Food",
                   "Suppliers": ["Bertolli", "Colavita", "Trader Joe's"]},
            "Green Tea" :{
                   "Price": 10.00, 
                   "Quantity": 90, 
                   "Category" : "Food",
                   "Suppliers": ["Lipton", "Twinings", "Tazo"]}
    }

    print("===== Inventory Management System =====\n",end="\n")
    print("Current Categories: Electronics, Books, Food\n")


    while True:
        """
        Main program loop. Continuously prompts the user for an operation
        until the user chooses to quit.
        """

        
        print("=" * 40) # Prints a seperator line
        operation_input = input("Enter operation (a/r/e/s/t/q): ") # Gets an user input
        
        ## Using switch case methods
        match operation_input:
            case "a":
                ## Adds a new product to the inventory.
                print("Adding new product:")
                add_new_product(products,categories)##  Calls the function 
            case "r":
               ## Removes an existing product from the inventory.
                product,check = validation_product_str(products,"Enter Product Name: ")  ## User input for product_name and check flag
                print("Removing a product: ")
                remove_product(product,products)##  Calls the function by passing product and products as args
            case "e":
                ## Edits an existing product in the inventory.
                print("Editing the product: ")
                product_name,check = validation_product_str(products,"Enter Product Name: ") ## User input for product_name and check flag
                edit_product(product_name,products) ##  Calls the function by passing proudct name and products as args

            case "s":
                ## Searches for a product in the inventory.
                print("Searching the product: ")
                search_product(products,categories) ##  Calls the function by passing products anf categories as args
            case "t":
                ## Print for the inventory report.
                 print("=" * 5 + "Inventory Report" + "=" * 5)
                 report(products,categories) # Calls the function by passing products anf categories as args
            case "q":
                ## Exits the program
                print("Exiting the program. Goodbye!\n\n") 
                break
            case _:
                ## Handles invalid user input
                print("Unknown Operation!!! Try using the operations listed.(a/r/e/s/t/q)")
    



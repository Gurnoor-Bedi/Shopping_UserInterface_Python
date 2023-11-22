
# Import the random module for generating session IDs
import random

# Define a class named ShoppingCart
class ShoppingCart:
    # Constructor method initializes class attributes
    def __init__(self):
        # Product catalog with product IDs, names, and prices
        self.catalog = {
            1: {'name': 'Boots', 'price': 500},
            2: {'name': 'Coats', 'price': 1000},
            3: {'name': 'Jackets', 'price': 800},
            4: {'name': 'Caps', 'price': 200},
            5: {'name': 'Sunglasses', 'price':550},
            6: {'name': 'Belts', 'price':400}
        }
        # Shopping cart to store selected items and quantities
        self.cart = {}
        # User and admin session IDs initialized to None
        self.user_session_id = None
        self.admin_session_id = None

    # Display a welcome message for the shopping application
    def display_welcome_message(self):
        print("Welcome to the Chandigarh Sector-17 Market.")

    # Method to create a user login session based on provided credentials
    def create_user_login(self, username, password):
        # Check if provided username and password match predefined values
        if username == 'user' and password == 'password':
            # Generate a random session ID for the user
            self.user_session_id = random.randint(1, 1000)
            print("User login successful. Session ID:", self.user_session_id)
        else:
            print("Invalid credentials for user login.")

    # Display the product catalog with product IDs, names, and prices
    def display_catalog(self):
        print("\nProduct Catalog:")
        for product_id, product_info in self.catalog.items():
            print(f"{product_id}. {product_info['name']} - Rs. {product_info['price']}")

    # Add a specified quantity of a product to the shopping cart
    def add_to_cart(self, product_id, quantity):
        # Check if the provided product ID and quantity are valid
        if product_id in self.catalog and quantity > 0:
            # Update the shopping cart with the selected product and quantity
            if product_id in self.cart:
                self.cart[product_id] += quantity
            else:
                self.cart[product_id] = quantity
            print(f"{quantity} {self.catalog[product_id]['name']}(s) added to the cart.")
        else:
            print("Invalid product ID or quantity.")

    # Remove a specified quantity of a product from the shopping cart
    def remove_from_cart(self, product_id, quantity):
        # Check if the provided product ID and quantity are valid
        if product_id in self.cart and quantity > 0:
            # Update the shopping cart by reducing the quantity or removing the product
            if quantity >= self.cart[product_id]:
                del self.cart[product_id]
            else:
                self.cart[product_id] -= quantity
            print(f"{quantity} {self.catalog[product_id]['name']}(s) removed from the cart.")
        else:
            print("Invalid product ID or quantity.")

    # Process the checkout, displaying an order summary and initiating payment
    def checkout(self, payment_option):
        # Check if the cart is empty before proceeding with checkout
        if not self.cart:
            print("Your cart is empty. Add items before checkout.")
            return

        # Display the order summary with product names and quantities
        print("\nOrder Summary:")
        for product_id, quantity in self.cart.items():
            print(f"{self.catalog[product_id]['name']} - Quantity: {quantity}")

        # Calculate and display the total amount to be paid
        total_amount = sum([self.catalog[p]['price']*q for p, q in self.cart.items()])
        print(f"\nTotal amount: Rs. {total_amount}")

        # Add payment processing logic based on the selected payment option.
        print(f"\nYour order is successfully placed. You will be shortly redirected to the portal for {payment_option} to make a payment.")

# Sample user-end interaction:
# Create an instance of the ShoppingCart class
shopping_app = ShoppingCart()
# Display the welcome message
shopping_app.display_welcome_message()

# User login
username = input("Enter username: ")
password = input("Enter password: ")
shopping_app.create_user_login(username, password)

# Display the product catalog
shopping_app.display_catalog()

# User actions
while True:
    print("\nUser Actions:")
    print("1. Add to Cart")
    print("2. Remove from Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    # Prompt the user to choose an action
    choice = input("Enter your choice (1-5): ")

    # Perform actions based on user's choice
    if choice == '1':
        product_id = int(input("Enter product ID to add to cart: "))
        quantity = int(input("Enter quantity: "))
        shopping_app.add_to_cart(product_id, quantity)
    elif choice == '2':
        product_id = int(input("Enter product ID to remove from cart: "))
        quantity = int(input("Enter quantity: "))
        shopping_app.remove_from_cart(product_id, quantity)
    elif choice == '3':
        # Display the current contents of the shopping cart
        print("\nCurrent Cart:")
        for product_id, quantity in shopping_app.cart.items():
            print(f"{shopping_app.catalog[product_id]['name']} - Quantity: {quantity}")
    elif choice == '4':
        # Prompt the user to select a payment option and initiate checkout
        payment_option = input("Select payment option (e.g., UPI, PayPal): ")
        shopping_app.checkout(payment_option)
        break
    elif choice == '5':
        # Exit the program
        break
    else:
        # Handle invalid user input
        print("Invalid choice. Please enter a number between 1 and 5.")

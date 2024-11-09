class Product:
    
    # Class variables to store inventory and keep track of product count
    INVENTORY = {}
    COUNTER = 0
    
    def __init__(self, product_id, name, category, quantity, price, supplier):
        # Initialize instance attributes
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
        
        # Add product information to the INVENTORY dictionary
        Product.INVENTORY[self.product_id] = {
            "name": name,
            "category": category,
            "quantity": quantity,
            "price": price,
            "supplier": supplier
        }
        
        # Print the updated inventory for verification
        print(Product.INVENTORY)
        
    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        # Increment the counter to generate a unique product ID
        Product.COUNTER += 1
        product_id = Product.COUNTER
        
        # Create a new product instance
        new_product = cls(product_id, name, category, quantity, price, supplier)
        
        # Confirm successful addition of the product
        print("Product Added Successfully")
        
        return new_product
        
    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        # Check if the product exists in the inventory
        if product_id in Product.INVENTORY.keys():
            # Update product attributes if provided
            Product.INVENTORY[product_id]["quantity"] = quantity
            Product.INVENTORY[product_id]["price"] = price
            Product.INVENTORY[product_id]["supplier"] = supplier
            
            # Confirm successful update of product information
            print("Product information updated successfully")
        else:
            # Inform the user if the product is not found
            print("Product not found")
            
    @classmethod
    def delete_product(cls, product_id):
        # Check if the product exists in the inventory
        if product_id in Product.INVENTORY.keys():
            # Delete the product from the inventory
            del Product.INVENTORY[product_id]
            
            # Confirm successful deletion
            print("Product deleted successfully")
        else:
            # Inform the user if the product is not found
            print("Product not found")

class Order:
    
    def __init__(self, order_id, products, customer_info=None):
        # Initialize order attributes
        self.order_id = order_id
        self.products = products  # List of products in the order
        self.customer_info = customer_info  # Optional customer information
    
    def place_order(self, product_id, quantity, customer_info=None):
        # Add product and quantity to the order
        self.products.append((product_id, quantity))
        
        # Print confirmation of order placement
        print(f"Order placed successfully. Order ID: {self.order_id}")

# Retail Inventory and Order Management System

This project is a Python-based inventory and order management system for managing products and processing orders. The system allows users to add, update, and delete products in inventory and create and manage customer orders.

## Features

- **Inventory Management**: Add, update, and delete products with attributes such as name, category, quantity, price, and supplier.
- **Order Management**: Create orders with customer information and ordered products.
- **Adaptive Inventory Tracking**: Automatically track and update the inventory after product updates.

## Class Descriptions

### `Product` Class

This class provides the functionalities to manage products in the inventory.

#### Attributes:
- **INVENTORY**: A class-level dictionary storing all products with details.
- **COUNTER**: A counter used to auto-generate unique product IDs.

#### Methods:
1. **`__init__(self, product_id, name, category, quantity, price, supplier)`**
   - Initializes a new product instance and adds it to the inventory.

2. **`add_product(cls, name, category, quantity, price, supplier)`**
   - A class method to create and add a product to the inventory.
   - **Returns**: The new product instance.

3. **`update_product(cls, product_id, quantity=None, price=None, supplier=None)`**
   - Updates an existing product's details (quantity, price, supplier).
   - If the product ID does not exist, it prints "Product not found."

4. **`delete_product(cls, product_id)`**
   - Removes a product from the inventory by ID.
   - If the product ID does not exist, it prints "Product not found."

#### Example Usage:
```python
# Import needed library
from sales_inventory import Product

# Adding products
p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
p2 = Product.add_product("Smartphone", "Electronics", 100, 800, "Supplier B")

# Updating a product
Product.update_product(1, quantity=45, price=950)

# Deleting a product
Product.delete_product(2)
```

### `Order` Class

This class provides basic functionality to manage customer orders.

#### Attributes:
- **order_id**: Unique identifier for each order.
- **products**: A list of products in the order, with product IDs and their respective quantities.
- **customer_info**: Optional attribute for storing customer information (such as name, address, etc.).

#### Methods:
1. **`__init__(self, order_id, products, customer_info=None)`**
   - Initializes a new order instance with an order ID, a list of products, and optional customer information.

2. **`place_order(self, product_id, quantity, customer_info=None)`**
   - Adds a product to the order with the specified quantity.
   - **Prints**: A confirmation message with the order ID once the product has been added.

#### Example Usage:
```python
# Import needed library
from sales_inventory import Order

# Creating a new order
order1 = Order(order_id=1, products=[])

# Placing an order with a product
order1.place_order(product_id=1, quantity=2, customer_info="Customer A")

# Placing another order with different product
order1.place_order(product_id=2, quantity=3)
```

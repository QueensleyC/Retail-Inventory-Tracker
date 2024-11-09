from sales_inventory import Product

# Add Products
p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
p2 = Product.add_product("Smartphone", "Electronics", 100, 800, "Supplier B")
p3 = Product.add_product("Tablet", "Electronics", 75, 500, "Supplier C")
p4 = Product.add_product("Headphones", "Accessories", 200, 150, "Supplier D")
p5 = Product.add_product("Desk Chair", "Furniture", 30, 300, "Supplier E")
p6 = Product.add_product("Coffee Maker", "Appliances", 40, 120, "Supplier F")
p7 = Product.add_product("Gaming Console", "Electronics", 60, 400, "Supplier G")
p8 = Product.add_product("Smart Watch", "Wearables", 90, 250, "Supplier H")
p9 = Product.add_product("Air Purifier", "Home Appliances", 45, 200, "Supplier I")
p10 = Product.add_product("Bluetooth Speaker", "Accessories", 120, 180, "Supplier J")
p11 = Product.add_product("Electric Kettle", "Kitchen Appliances", 80, 60, "Supplier K")
p12 = Product.add_product("Printer", "Office Supplies", 25, 350, "Supplier L")
p13 = Product.add_product("LED Monitor", "Electronics", 40, 220, "Supplier M")
p14 = Product.add_product("Refrigerator", "Home Appliances", 15, 1500, "Supplier N")
p15 = Product.add_product("Blender", "Kitchen Appliances", 70, 100, "Supplier O")

# Update Product
update_p1 = Product.update_product(1, quantity=45, price=950)

# Delete a Product
Product.delete_product(5)


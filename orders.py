from sales_inventory import Order

order = Order(order_id=1, products=[])

order_placement = order.place_order(1, 2, customer_info="Jane Doe")
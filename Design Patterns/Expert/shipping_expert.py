from expert import OrderProcessingExpert

class ShippingExpert(OrderProcessingExpert):
    def process(self, order):
        print(f"Shipping order {order['order_id']} to {order['customer_name']}")

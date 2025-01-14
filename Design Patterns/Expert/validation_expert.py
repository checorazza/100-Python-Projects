from expert import OrderProcessingExpert

class ValidationExpert(OrderProcessingExpert):
    def process(self, order):
        if not order.get('customer_name') or not order.get('product_id'):
            raise ValueError("Invalid order data")
        print("Order validated")

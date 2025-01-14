from expert import OrderProcessingExpert

class PaymentProcessingExpert(OrderProcessingExpert):
    def process(self, order):
        print(f"Processing payment for order {order['order_id']}")

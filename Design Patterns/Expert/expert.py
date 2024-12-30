from abc import ABC, abstractmethod

class OrderProcessingExpert(ABC):
    @abstractmethod
    def process(self, order):
        pass

#

class ValidationExpert(OrderProcessingExpert):
    def process(self, order):
        if not order.get('customer_name') or not order.get('product_id'):
            raise ValueError("Invalid order data")
        print("Order validated")

class PaymentProcessingExpert(OrderProcessingExpert):
    def process(self, order):
        print(f"Processing payment for order {order['order_id']}")

class ShippingExpert(OrderProcessingExpert):
    def process(self, order):
        print(f"Shipping order {order['order_id']} to {order['customer_name']}")

#

class OrderProcessingContext:
    def __init__(self):
        self.experts = []

    def add_expert(self, expert: OrderProcessingExpert):
        self.experts.append(expert)

    def process_order(self, order):
        for expert in self.experts:
            expert.process(order)

# Use

def main():
    order = {
        'order_id': 12345,
        'customer_name': 'John Doe',
        'product_id': 67890
    }

    validation_expert = ValidationExpert()
    payment_expert = PaymentProcessingExpert()
    shipping_expert = ShippingExpert()

    context = OrderProcessingContext()
    context.add_expert(validation_expert)
    context.add_expert(payment_expert)
    context.add_expert(shipping_expert)

    context.process_order(order)

if __name__ == "__main__":
    main()

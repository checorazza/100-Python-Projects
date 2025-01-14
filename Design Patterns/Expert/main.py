# main.py
from context import OrderProcessingContext
from validation_expert import ValidationExpert
from payment_expert import PaymentProcessingExpert
from shipping_expert import ShippingExpert

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

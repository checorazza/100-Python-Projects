from payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paying {amount} using Credit Card")

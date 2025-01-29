from payment_strategy import PaymentStrategy

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paying {amount} using PayPal")

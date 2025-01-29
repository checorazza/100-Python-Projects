from payment_strategy import PaymentStrategy

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paying {amount} using Bitcoin")

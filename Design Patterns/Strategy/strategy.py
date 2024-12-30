from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

#

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paying {amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paying {amount} using PayPal")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paying {amount} using Bitcoin")

#

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def pay(self, amount: float):
        self._strategy.pay(amount)


# Use

def main():
    amount = 100.0

    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()
    bitcoin_payment = BitcoinPayment()

    context = PaymentContext(credit_card_payment)
    context.pay(amount)  # Output: Paying 100.0 using Credit Card

    context.set_strategy(paypal_payment)
    context.pay(amount)  # Output: Paying 100.0 using PayPal

    context.set_strategy(bitcoin_payment)
    context.pay(amount)  # Output: Paying 100.0 using Bitcoin

if __name__ == "__main__":
    main()

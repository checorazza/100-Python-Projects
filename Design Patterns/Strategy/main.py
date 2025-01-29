from credit_card_payment import CreditCardPayment
from paypal_payment import PayPalPayment
from bitcoin_payment import BitcoinPayment
from payment_context import PaymentContext

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

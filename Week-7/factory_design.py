# Week-7 Activity-3

# Factory + Singleton Example
# Description: To make it a factory patter, we will create multiple payment method classes and a factory to instantiate them based on input. and to make it a singleton pattern, we will ensure that only one instance of the payment gateway exists.

# 1. Payment method classes
class PayPalPayment:
    def process_payment(self, amount):
        return f"Processing {amount} via PayPal."

class CreditCardPayment:
    def process_payment(self, amount):
        return f"Processing {amount} via Credit Card."

class BankTransferPayment:
    def process_payment(self, amount):
        return f"Processing {amount} via Bank Transfer."

class CryptoPayment:
    def process_payment(self, amount):
        return f"Processing {amount} via Crypto."

class GooglePayPayment:
    def process_payment(self, amount):
        return f"Processing {amount} via Google Pay."


# 2. Factory Pattern: creates objects dynamically

class PaymentFactory:
    @staticmethod
    def create_payment(method):
        if method == "paypal":
            return PayPalPayment()
        elif method == "credit_card":
            return CreditCardPayment()
        elif method == "bank_transfer":
            return BankTransferPayment()
        elif method == "crypto":
            return CryptoPayment()
        elif method == "google_pay":
            return GooglePayPayment()
        else:
            raise ValueError("Unsupported payment method")


# 3. Singleton Pattern: only one PaymentGateway instance

class PaymentGateway:
    _instance = None  # store the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PaymentGateway, cls).__new__(cls)
        return cls._instance

    def process(self, method, amount):
        
        payment_processor = PaymentFactory.create_payment(method)
        return payment_processor.process_payment(amount)


# main

gateway1 = PaymentGateway()
gateway2 = PaymentGateway()

# gateway1 and gateway2 are the SAME instance (Singleton)
print(gateway1 is gateway2)  # True

# Process some payments
print(gateway1.process("paypal", 50))
print(gateway1.process("credit_card", 100))
print(gateway1.process("crypto", 200))
print(gateway1.process("google_pay", 75))

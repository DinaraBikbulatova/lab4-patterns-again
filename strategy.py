class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        return f"Оплата картой: {amount} руб."

class PayPal(PaymentStrategy):
    def pay(self, amount):
        return f"Оплата PayPal: {amount} руб."

class ShoppingCart:
    def __init__(self):
        self.strategy = None
    
    def set_payment(self, strategy):
        self.strategy = strategy
    
    def checkout(self, amount):
        return self.strategy.pay(amount)

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.set_payment(CreditCard())
    print(cart.checkout(1000))

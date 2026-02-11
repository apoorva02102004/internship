# Parent class
class Payment:
    def pay(self):
        print("Processing payment...")

# Child class 1
class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay.")

# Child class 2
class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe.")

# Child class 3
class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card.")

# Creating objects
payment = Payment()
google_pay = GooglePay()
phone_pe = PhonePe()
credit_card = CreditCard()

# Calling pay() method
payment.pay()
google_pay.pay()
phone_pe.pay()
credit_card.pay()



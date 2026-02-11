# Parent Class
class Payment:
    def pay(self, amount):
        print("Processing payment...")


# Child Class 1
class GooglePay(Payment):
    def pay(self, amount):
        if amount <= 0:
            print("Invalid payment amount!")
        else:
            print(f"₹{amount} paid successfully using Google Pay.")


# Child Class 2
class PhonePe(Payment):
    def pay(self, amount):
        if amount <= 0:
            print("Invalid payment amount!")
        else:
            print(f"₹{amount} paid successfully using PhonePe.")


# Child Class 3
class Paytm(Payment):
    def pay(self, amount):
        if amount <= 0:
            print("Invalid payment amount!")
        else:
            print(f"₹{amount} paid successfully using Paytm.")


# Creating Objects
gpay = GooglePay()
phonepe = PhonePe()
paytm = Paytm()

# Calling Methods
gpay.pay(1000)
phonepe.pay(500)
paytm.pay(-200)   # Example validation

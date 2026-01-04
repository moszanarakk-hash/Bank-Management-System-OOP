class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"ฝากเงิน {amount} บาท สำเร็จ")

    def withdraw(self, amount):
        if amount > self.balance:
            print("ยอดเงินไม่พอ")
        else:
            self.balance -= amount
            print(f"ถอนเงิน {amount} บาท สำเร็จ")


# ===== โปรแกรมหลัก =====
balance = int(input("กรุณาใส่ยอดเงินเริ่มต้น: "))
account = Account(balance)

while True:
    print("\nเมนู")
    print("1. ฝากเงิน")
    print("2. ถอนเงิน")
    print("3. ดูยอดเงิน")
    print("4. ออก")

    choice = input("เลือกเมนู (1-4): ")

    if choice == "1":
        amount = int(input("จำนวนเงินที่ต้องฝาก: "))
        account.deposit(amount)

    elif choice == "2":
        amount = int(input("จำนวนเงินที่ถอน: "))
        account.withdraw(amount)

    elif choice == "3":
        print("ยอดเงินคงเหลือ:", account.balance)

    elif choice == "4":
        print("ออกจากโปรแกรม")
        break

    else:
        print("เลือกเมนูไม่ถูกต้อง")
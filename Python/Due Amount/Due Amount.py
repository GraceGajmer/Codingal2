def calculate_due_amount(bill_amount, payment):
  due_amount = bill_amount - payment
  return due_amount

bill_amount = float(input("Enter the total bill amount: "))
payment = float(input("Enter the amount paid: "))

due_amount = calculate_due_amount(bill_amount, payment)
print("The remaining due amount is:", due_amount)
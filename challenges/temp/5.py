expense_list = []
while True:
  expense = int(input("Please input an expense to add to the list: "))
  if expense == -1:
    break
  else:
    expense_list.append(expense)

total_expense_over_100 = 0
for expense in expense_list:
  if expense > 100:
    total_expense_over_100 += expense

print(total_expense_over_100)

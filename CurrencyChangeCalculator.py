from math import floor

change_amount = int(input("Enter total cents: "))

dollars = change_amount // 100
quarters = floor((change_amount - (dollars * 100)) / 25)
dimes = floor((change_amount - (dollars * 100) - (quarters * 25)) / 10)
nickles = floor((change_amount - (dollars * 100) - (quarters * 25) - (dimes * 10)) / 5)
pennies = (change_amount - (dollars * 100) - (quarters * 25) - (dimes * 10) - (nickles * 5))

if change_amount <= 0:
    print("No change")

if change_amount >= 100 and dollars >= 1:
    if dollars > 1:
        print(f"{dollars} Dollars")
    else:
        print(f"{dollars} Dollar")
   
if change_amount >= 25 and quarters >= 1:
    if quarters > 1:
        print(f"{quarters} Quarters")
    else:
        print(f"{quarters} Quarter")

if change_amount >= 10 and dimes >= 1:
    if dimes > 1:
        print(f"{dimes} Dimes")
    else:
        print(f"{dimes} Dime")

if change_amount >= 5 and nickles >= 1:
    if nickles > 1:
        print(f"{nickles} Nickels")
    else:
        print(f"{nickles} Nickel")

if change_amount >= 1 and pennies >= 1:
    if pennies > 1:
        print(f"{pennies} Pennies")
    else:
        print(f"{pennies} Penny")

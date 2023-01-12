print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")

total_bill = float(total_bill)
tip_percentage = int(tip_percentage)
tip_percentage = tip_percentage / 100
people = int(people)

total_pay = total_bill * (1 + tip_percentage)
person_pay = total_pay / people
person_pay = round(person_pay, 2)
person_pay = "{:.2f}".format(person_pay)   #使用format來確保強制顯示至少小數點後兩位
print(f"Each person should pay: ${person_pay}")
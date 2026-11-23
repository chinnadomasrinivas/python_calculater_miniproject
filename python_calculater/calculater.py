##inputs we need from the user
#total rent 
#Total food orderedfor snacking
#Electricity units spend 
#Charge per unit
#Persons living in room/flat

##output
# Total amount you've to pay is

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount on food  spend = "))
Electricity_spend = int(input("Enter the total on electricity spend =  "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))
total_bill = Electricity_spend * charge_per_unit
print("Total bill on electricity = " ,total_bill)
output = (food + charge_per_unit + total_bill+rent)/persons
print("total amount"+" = " ,food + charge_per_unit + total_bill+rent)
print("Each person will pay = " ,output)

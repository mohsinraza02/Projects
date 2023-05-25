#Malik Raza
print("Welcome to the tip calculator")
total = (input("What was the total bill?"))
percentage = (input("What percentage tip would you like to give? 10, 12,or 15%"))
people = (input("How many people will the bill be split in?"))

person = (float(total))*(((float(percentage))/100)+1)
amount = person/float(people)

print(round(amount, 2))

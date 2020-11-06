#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
total = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")

# Total after tip:
total_with_tip = float(total) + (float(total) * (int(tip) / 100))
print(f"Total after tip: {total_with_tip}")

# Each person should pay:
person_amount = round(total_with_tip / int(num_people), 2) 

print(f"Each person should pay: ${person_amount}")

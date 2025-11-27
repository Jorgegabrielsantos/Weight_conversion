weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds?(K or P): ")

if unit == "P":
    weight = round(weight * 2.205)
    unit = "Lbs."
    print(f"Your weight is: {weight} {unit}")
elif unit == "K":
    weight = round(weight / 2.205)
    unit = "Kgs."
    print(f"Your weight is: {weight} {unit}")
else: 
    print(f"{unit} was not valid!")
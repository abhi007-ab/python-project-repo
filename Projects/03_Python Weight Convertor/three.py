# Python Weight Convertor

weigth = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds? (K or L): ")

if unit == 'K':
    weigth = weigth * 2.205
    unit = 'Lbs.'
    print(f"Your weight is: {round(weigth, 1)} {unit}")
elif unit == 'L':
    weigth = weigth / 2.205
    unit = 'Kgs.'
    print(f"Your weight is: {round(weigth, 1)} {unit}")
else:
    print(f"{unit} was not valid")
from calculator import Calculator

print("Welcome to the tip calculator.")
total = float(input("What was the total bill? "))
tip = int(input("What percentage top would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

val = Calculator.calculate(total, tip, people)
result = format(val, ".2f")
print("Each person should pay: $" + result)

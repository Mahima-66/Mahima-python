# Ask the user to enter their weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

# Calculate the BMI using the formula
bmi = weight / (height ** 2)

# Print the BMI and the corresponding health condition
print("Your BMI is", bmi)
if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are healthy")
elif bmi < 30:
    print("You are overweight")
else:
    print("You are obese")
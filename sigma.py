height = float(input("enter your height in cm:"))
weight = float(input("enter your weight in kg's:"))

BMI = weight / (height/100)**2
print("Your bmi is", BMI)

if BMI<= 18.4:
    print("Your under weight")
elif BMI<= 24.9:
    print("Your healthy!")

elif BMI<= 29.9:
    print("Your over weight")

elif BMI<= 34.9:
    print("Your severly over weight")

elif BMI<= 39.9:
    print("Your obese")

else:
    print("Your severly obesse")


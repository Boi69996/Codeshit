Name = input("What is your name? ")
print("Hello " + Name)
print("This Program will show you your BMI and how Healthy you are.")
Kg_Weight = input("What is your weight? ")
M_Height = input("What is your height? ")
BMI = float(Kg_Weight)/(float(M_Height) * float(M_Height))
Under_weight = float(BMI) < 18.5
Healthy = (float(BMI) > 18.5) and (float(BMI) < 24.9)
Over_Weight = (float(BMI) > 24.9) and (float(BMI) < 29.9)
Obese = (float(BMI) > 29.9) and (float(BMI) < 39.9 )
print(BMI)
if Under_weight:
    print("You are Underweight.")
if Healthy:
    print("You are healthy!")
if Over_Weight:
    print("You are Overweight.")
if Obese:
    print("You are Obese.")
input('Press enter to exit')

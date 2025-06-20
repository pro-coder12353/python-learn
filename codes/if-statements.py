age = int(input("enter your age: "))

if age >= 21:
    print("You are eligible for applying credit card. ")
elif age < 18:
    print("You are still a minor.")
else:
    print("You must be 21+ to be eligible for applying credit card. ")


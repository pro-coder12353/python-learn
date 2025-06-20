# typecasting = process of converting a variable into another variable.
#                   str(), int(), float(), bool()

name = "manoj k"
age = 21
gpa = 3.5
is_student = True

print(type(is_student)) # to get the type of a variable

gpa = int(gpa) # will be a integer
print(gpa)

age = float(age) # will be a float value
print(age)


name = bool(name) # will become a boolean, it will show true and shows false only for empty
print(name)
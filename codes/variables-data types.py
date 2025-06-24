# variable = strings,integers,float, boolean
"""
numeric: float, integers, complex numbers

sequence: strings, list, tuples

dictionary

boolean

set data type
"""
#complex numbers
a = 10 + 10j

print(a)

# Strings
first_name = "Manoj"
food = "biryani"
email = "man@fake.com"


print(f"Hello {first_name}")
print(f"You like {food}")
print(f"your email is {email}")

#lists: one or more similiar data typesd

example_list = [1,"hello",4.5,"a"]


print(example_list[2])

#tuples: similiar to lists, but cannot me modified or changed
example_tuple = [1,"hello",4.5,"a"]

print(example_tuple[2])


#dictionary: can store any data type

ed = {"a":22, "b":44.3}

print(ed)

#Integers
age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

a,b,c = 1,2,3

print(a)
print(b)
print(c)

del a




# Float
price = 10.99
gpa = 3.5
distance = 5.5


print(f"The price is Rs.{price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")


#Boolean
is_student = True
for_sale = True


print(f"Are you a student? {is_student}")

if for_sale:
    print(" That item is for sale")
else:
    print("That item is not for sale")





"""
Variable Names:
rules:
1. A variable name must start witha a letter or the underscore
2. A variable name caanot start with a number
3. A variable name can only contain alpha-numeric characters and underscored
4. Variable names are case-sensitive
5. A variable name cannot be any of the python keywards.


Multi words variable Names

1. Camel case
each word, except the first, starts with a capital letter

example: myName

2. Pascal Case
Each word starts with a capital letter

example: My Name


3. Snake Case
Each word is seperated by an underscore character.

example:
my_name_hello

"""
# for loop

i = 10

for i in range(0,5):
    print(i)

sum_numbers = 0

for i in range(1,101):
    sum_numbers += i
print(sum_numbers)


""" 
while-loop: 
A while loop is different from the for loop. A for loop 
allows us to iterate over a specific range, whereas a while 
loop allows us to keep iterating as long as a certain condition is met.
"""
#   while conditon:
#   code

number = 27
power_of_two = 1

while power_of_two <= number:
    power_of_two *= 2
    print(f"{power_of_two}")

print(power_of_two)


# break:

for i in range(10): 
    if i == 6:
        break  #stops the loop as soon as the break is encountered
    print(i)
# or =  at least one statement is true
# and = both conditions must be true
# not = inverts the condition


temp = 25
is_raining = True

if temp > 35 or temp < 0 :
    print("The outdoor event is cancelled")
elif temp < 28 and temp > 0 and is_raining:
    print("It is cold and raining 🧊")
else:
    print("The outdoor event is still scheduled")

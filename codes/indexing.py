# accessing elements of a sequence using [] (indexing operator)
# [start : end : step]


credit_number = "1234-5678-9012-3456"

print(credit_number[0])     #answer is 1
print(credit_number[0:4])   #answer is 1234
print(credit_number[5:9])   #answer is 5678
print(credit_number[5:])    #answer is 5678-9012-3456
print(credit_number[-1])    #answer is 6 from back
print(credit_number[::3])   #answer is 146-136


# to show only last 4 digits of the credit card
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
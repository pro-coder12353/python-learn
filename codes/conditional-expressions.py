# print or assign one of two values based on a condition
# x if condition else y


num = 6
a = 6
b = 7


print("Postive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"

max_num = a if a > b else b
min_num = a if a < b else b

print(result)
print(max_num)
print(min_num)
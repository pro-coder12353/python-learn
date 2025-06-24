# format a value absed on what flags inserted
#  {value:flags}


price1 = 747474.145
price2 = -987232.65
price3 = 13232.34



print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:>10}")
a, b, c = 1, 2, 3

print((a > b) and (b > c))  # False
print((a > b) or (b > c))   # False
print((a < b) or (b > c))   # True
print(not (a > b))          # True

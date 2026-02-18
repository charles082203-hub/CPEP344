x = float(input("Enter value for x: "))

inner_most = 1 / x
second = 1 / (x + inner_most)
third = 1 / (x + second)
y = 1 / (x + third)

print("y =", y)

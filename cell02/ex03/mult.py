x = int(input("Enter the first number:\n"))
y = int(input("Enter the second number:\n"))
result = x * y
print(f"{x} x {y} = {result}")
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")

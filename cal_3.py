num1 = input("First Number:\n")
operator = input("Operator (+, -, *, /):\n")
num2 = input("Second Number:\n")

num1 = (num1)
num2 = (num2)

out = None

if operator == "+":
    out =  num1 + num2
elif operator == "-":
    out = num1 - num2
elif operator == "*":
    out = num1 * num2
elif operator == "/":
    out = num1 / num2

print("Answer: " + str(out))


mode = input("Choose an arithmetic operator (+, -, *, /, ^): ")

first = float(input(" Enter the first number: "))
second = float(input("Enter the second number: "))

if mode == "+":
    sum = first + second
    print(sum)
elif mode == "-":
    sum = first - second
    print(sum)
elif mode == "*":
    sum = first * second
    print(sum)
elif mode == "/":
    sum = first / second
    print(sum)
elif mode == "^":
    sum = first ** second
    print(sum)
else:
    print("This is an invalid input!Please try again")
print("****** CALCULATOR ******")
operator = input("Enter the operation(+,-,*,/,%,**): ")
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))

if operator=='+':
    print(f"Sum of {num1} and {num2} = {num1 + num2}")
elif operator=='-':
    print(f"Difference between {num1} and {num2} = {num1 - num2}")
elif operator=='*':
    print(f"Product of {num1} and {num2} = {num1 * num2}")
elif operator=='/':
    print(f"Quotient of {num1} and {num2} = {num1 / num2}")
elif operator=='%':
    print(f"Remainder of {num1} and {num2} = {num1 % num2}")
elif operator=='**':
    print(f"Power of {num1} and {num2} = {num1 ** num2}")
else:
    print(f"{operator} is an invalid choice. please enter a valid one.")
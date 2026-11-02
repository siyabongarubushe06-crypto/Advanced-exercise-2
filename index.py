import math

a=5
b=10
c=7
a += 3
b *= 2
c %= 4
result = math.sqrt(a**2 + b**2 + c**2)
print(round(result, 2))

x =int(input("enter x: "))
y =int(input("enter y: "))
z=int(input("enter z: "))
is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <=50
final_condition = is_even and is_positive and is_in_range 
print(final_condition) 

score = int(input("enter your base score: "))
score += 5
score -= 10
score = max(0, min(100, score))
if score >=90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("final score:", score)
print("your grade is:", grade)

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
operation = input("enter an operation (+, -, *, /, **): ")
try:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    elif operation == "**":
        result = num1 ** num2
 
    else:
         result = "invalid operation"
except ZeroDivisionError:
    result = "Error: cannot divide by zero"

print("Result:", result)        

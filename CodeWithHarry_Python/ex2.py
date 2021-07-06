# Exercise 2 - Faulty Calculator
# Design a calculator which will correctly solve all
# the problems xcept : 45*3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator and two numbers
# as input from the user and return the result.

n1 = float(input("Enter 1st number : "))
op = input("Enter the operator : ")
n2 = float(input("Enter 2nd number : "))
output = 1.1

if (op == "+"):
    if(n1 == 56 and n2 == 9) or (n1 == 9 and n2 == 56):
        output = 77
    else:
        output = n1 + n2;

if (op == "-"):
    output = n1 - n2;

if (op == "*"):
    if(n1 == 45 and n2 == 3) or (n1 == 3 and n2 == 45):
        output = 555
    else:
        output = n1 * n2;

if (op == "/"):
    if(n1 == 56 and n2 == 6) or (n1 == 6 and n2 == 56):
        output = 4
    else:
        output = n1 / n2;

print(n1, op, n2, "=", output)
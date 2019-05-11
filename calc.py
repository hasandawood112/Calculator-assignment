num1 = float(input("Enter First value : "))
op = input("Choose operator : ")
num2 = float(input("Enter Second value : "))

if op == '+' : 
    ans = num1 + num2
    print("Result is : ", ans)
elif op == '-' : 
    ans = num1 - num2
    print("Result is : ", ans)
elif op == '*' : 
    ans = num1 * num2
    print("Result is : ", ans)
elif op == '/' : 
    ans = num1 / num2
    if num2 == 0 :
        print("Denominator should not be 0")
    else:
        print("Result is : ", ans)
else:
    print("invalid inputs!")
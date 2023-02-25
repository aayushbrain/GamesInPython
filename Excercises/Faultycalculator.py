# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# # Design a calculator which will correctly solve all the problems except
# # the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result


print("Enter 1st Number")
num1 = int(input())
print("Enter 2nd Number")
num2 = int(input())
print("So what you want?"+"+,-,/,*")
num3 = input()

if num1 ==45 and num2 ==3 and num3 =="*":
    print("555")
elif num1 ==56 and num2 ==9 and num3 =="+":
    print("77")
elif num1 ==56 and num2 ==6 and num3 =="/":
    print("4")

elif num3 =="*":
    Multi=num1*num2
    print(Multi)
elif num3 =="+":
    Plus=num2+num1
    print(Plus)
elif num3 =="/":
    Dev=num2/num1
    print(Dev)
elif num3 =="-":
    minus=num1-num2
    print(minus)
else:
    print("Out of range")



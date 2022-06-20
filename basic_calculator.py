import math
while True:
    print("===========================================")
    print("                                  ")
    operation = input("select operation \n"
                      "01.To add use '1'\n"
                      "02.To subtract  use '2' ie number 1 - number 2 \n"
                      "03.To multiple '3'\n"
                      "04.To divide '/'ie number1/number2 use '4'\n"
                      "05.To divide '//' want result in integer use '5'\n"
                      "06.To find the power of number ie number1^number2 use '6'\n"
                      "07.To find square root of 1st number use '7'\n"
                      "08.To exit the program type '8'...  \n")
    if operation=="8":
        print("exit the program....")
        print("                                             ")
        print("===========================================")
        break 
    if operation not in ["1","2","3","4","5","6","7"]:
        print("enter the valid option")
        continue
    else:                
     number1 = int(input("enter your first number  "))
     number2=int(input("enter your second number "))
    if operation=="1":
     sum=number1+number2
     print(number1, "+", number2 ,"=" ,sum)
    elif operation=="2":
        subtract=number1-number2
        print(number1, "-", number2 ,"=" ,subtract)
    elif operation=="3":
        mul=number1*number2
        print(number1, "*", number2 ,"=" ,mul)
    elif operation=="4":
        div=number1/number2
        print(number1, "/", number2 ,"=" ,div)
    elif operation=="5":
        div2=number1//number2
        print(number1, "//", number2 ,"=" ,div2)
    elif operation=="6":
        power=pow(number1,number2)
        print(number1, "^", number2 ,"=" ,power)
    elif operation=="7":
        x=math.sqrt(number1)
        print("square root of number1 is = ",x)
    


    


        


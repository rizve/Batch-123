def calculator():
    print("------------------------------------") 
    print("1. Press A or a For Addition")
    print("2. Press B or b For Subtrction")
    print("3. Press C or c For Multiplication")
    print("4. Press D or d For Division")
    # print("5. Press E or e for Exit")
    print("------------------------------------")   

    operation = input("Select One Option In Between : ").lower()
    

    try:
        num1 = float(input("Enter 1st Number : "))
        num2 = float(input("Enter 2nd Number : "))
    except:
        print("Invalid Number")
    
    # if operation == "e":
    #     print("I Am Exit! Good Bye.")
    #     break
    if operation == "a":
        print(num1, "+" ,num2, "=", (num1 + num2)) 
        print("------------------------------------")    
    elif operation == "b":
        print(num1, "-" ,num2, "=", (num1 - num2))
        print("------------------------------------")
    elif operation == "c":
        print(num1, "*" ,num2, "=", (num1 * num2))
        print("------------------------------------")
    elif operation == "d":
        if num1 == 0.0 or num2 == 0.0:
            print("0 Error.. Try Again")
        else:
            print(num1, "/" ,num2, "=", (num1 / num2))
            print("------------------------------------")
    else:
        print("Wrong Option Try Again...")
        print("------------------------------------")

while True:
    calculator()
    option = input("Do You want to quuit (Y/N) :").lower()
    if option == "y":
        break
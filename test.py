def calculator():
   
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. %")
    print("6. sqrt")
    print("7. pow")
    print("8. pow3")

    oper =input("hvjvhg")    
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
     
    if oper == '4':
        print(num1 /num2 )
    elif oper == '5':
        sum = (num1 * num2) /100
        print(sum)
    elif choice =='6':
        #import math
        #print(math.sqrt(num1))
        sqrt =num1 ** (0.5)
        print(sqrt)  
    elif choice =='7':
        result = (num1 ** num2)
        print(result)
    elif choice =='8':
       result = (num1**3)
       print(result)
            
    
calculator()

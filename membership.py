member = int(input("1. Gold, 2. Silver, 3. normal"))
Silver = float (input("amount: "))
# Usual + float (input("Usual")) 

if member  == 1:
    print("Above one hundred,")
    amout = float(input("enter spending: "))
    if amout > 100:
        print(amout * .2)
    else:
        print(amout * 0.1)    

if member  == 2:
    print("and also above one hundred,")
    amout = float(input("enter spending: "))
    if amout > 100:
        print( amout * .15)
    else:
        print(amout * 0.5)

if member  == 3:
    print("but not above one hundred,")
    amout = float(input("enter spending: "))
    if amout > 100:
        print( amout * .05)
    else:
        print(amout * .0)
      
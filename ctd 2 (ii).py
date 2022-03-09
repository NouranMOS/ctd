bag=[5,9,10,77,30,7]
while True :
    print(bag)
    if(len(bag)>4):
        x=str(input("remove or enter or stop: "))
        if(x=='remove'):
            y=int(input("enter number : "))
            if( y in bag):
                 bag.remove(y)
            else:
                print("number not in bag")
        elif(x=='enter'):
            y=int(input("enter number : "))
            bag.append(y)
        elif(x=='stop'):
            break
    else:
        print("cannot remove, bag is at minimum capacity")
        print(bag)
        x=str(input("enter or stop : "))
        if(x=='enter'):
            y=int(input("enter number : "))
            bag.append(y)
        elif(x=='stop'):
            break

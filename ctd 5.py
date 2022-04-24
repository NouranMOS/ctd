import cv2
import random
bag1 = ['*','*','*','*','*','*','*','*','*','*']
bag2 = ['*','*','*','*','*','*','*','*','*','*']
bag3 = ['*','*','*','*','*','*','*','*','*','*']
f = 1
def remove_from_bag(bagx, y):
  f = 1
  if(y>6 or y<1):
    print("\nplease choose from 1 to 5\n")  
  elif(len(bagx)>0): 
    if(len(bagx)>=y):
        for i in range (y):
            bagx.remove('*')
            f =  0
    else:
        print("\nballs in bag length less than\n")
  else:
    print("\nbag empty choose another\n")
  if f == 0:
    return 0
  return 1
while True:
    # Lose
    if len(bag1)==0 and len(bag2)==0 and len(bag3)==0 and f==1:
        img = cv2.imread(r"C:\Users\En\OneDrive\Desktop\ctd\ylose.jpeg", cv2.IMREAD_COLOR)
        cv2.imshow("you lose", img)
        cv2.waitKey(0)
        break
    # your turn
    while f==1 :
        print(len(bag1)," = ", bag1)
        print(len(bag2)," = ", bag2)
        print(len(bag3)," = ", bag3)
        try:
          x = int(input("\nwhich bag? "))
          y = int(input("number of balls "))
          if x==1:
            f = remove_from_bag(bag1, y)
          elif x == 2:
            f = remove_from_bag(bag2, y)
          elif x == 3:
            f = remove_from_bag(bag3, y)
          else:
            print("\nplease choose bag from 1 to 3\n")  
        except ValueError:
          print("\nPlease enter a number\n")
    # win
    if len(bag1)==0 and len(bag2)==0 and len(bag3)==0 and f==0:
        img = cv2.imread(r"C:\Users\En\OneDrive\Desktop\ctd\ywin.jpeg", cv2.IMREAD_COLOR)
        cv2.imshow("you win", img)
        cv2.waitKey(0)
        break
    # Computer turn
    while f==0 :
        print("\n","you removed ", y, "from bag ", x,"\n")
        print(len(bag1)," = ", bag1)
        print(len(bag2)," = ", bag2)
        print(len(bag3)," = ", bag3)
        compbag=random.randint(1,3)
        compballs=random.randint(1,5)
        if compbag==1 and len(bag1)>0 and len(bag1)>=compballs:
          for i in range (compballs):
              bag1.remove('*')
              f=1
        if compbag==2 and len(bag2)>0 and len(bag2)>=compballs:
          for i in range (compballs):
              bag2.remove('*')
              f=1
        if compbag==3 and len(bag3)>0 and len(bag3)>=compballs:
          for i in range (compballs):
              bag3.remove('*')
              f=1
        print("\n","The computer removed ", compballs, "from bag ", compbag)
        print("\n--------------------------------------------------------------\n")
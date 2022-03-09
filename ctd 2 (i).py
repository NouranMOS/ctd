list=[]
while True:
    d = input("insert number: ") 
    if d == 'q':
        break
    else:
        list.append(d)
print("largest number is ", max(list))
print("smallest number is ",min(list))

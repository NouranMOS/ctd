x = input("Enter (1) to convert from celsius to fahrenheit or (2) to convert from fahrenheit to celsius :")
while ( x!='1' and x!='2'):
     x = input("Enter (1) to convert from celsius to fahrenheit or (2) to convert from fahrenheit to celsius :")
if(x=='1'):
    c = float(input("Enter temp in celsius : "))
    f = c * 1.8 + 32
    print('temp in fahrenheit is %0.1f' %f)
elif(x=='2'):
    f = float(input("Enter temp in fahrenheit : "))
    c = (f - 32) / 1.8
    print('temp in celsius is %0.1f' %c)
else:
    print("ERROR")
#reem 
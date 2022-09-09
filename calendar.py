import calendar
a=int(input("Enter year(natural number): "))
b=int(input("Enter month: "))
if(b>12):
    print("provide valid month")
else:
    print("\n")
    print(calendar.month(a,b))
    print("\n")
    if(a%400==0)and(a%100==0):
        print("It is a leap year",a)
    elif(a%4==0)and(a%100!=0):
        print("It is a leap year",a)
    else:
        print("It is not a leap year",a)

    


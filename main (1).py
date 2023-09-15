year=int(input("Please enter the year number/eg:2019:"))
if(year%400==0):
     print("%d is a Leap Year"%year)
elif(year%100==0):
     print("%d is Not the Leap Year"%year)
elif(year%4==0):
     print("%d is a Leap Year"%year)
else:
     print("%d is Not the Leap Year"%year)
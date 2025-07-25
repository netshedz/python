years = int(input("Enter a year: "))

if years < 1582:
	print("Not within the Gregorian calendar period")
 
elif years % 4 != 0:
    print("its a common year")
    
elif years % 100 != 0:
    print("its a leap year")

elif years % 400 != 0:
    print("its a common year")
    
else:
    print("leap year")
    
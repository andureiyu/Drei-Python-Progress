import calendar

year = int(input("Enter Year: ")) 
month = int(input("Enter Month: ")) # make sure you use numbers when you input (1-12)
cal = calendar.month(year, month)

print(cal)
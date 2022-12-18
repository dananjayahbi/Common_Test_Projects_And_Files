#dates according to your bday

import datetime

def myFunction(byear,bmonth,bday):
    today = datetime.datetime.now()
    
    years = today.year - byear
    months = today.month - bmonth
    days = today.day - bday
    
    yDates = years * 365
    mDates = months * 30
    
    totDays = yDates + mDates + days
    
    return totDays

uYear = int(input("Enter the birth year : "))
uMonth = int(input("Enter the birth month : "))
uDate = int(input("Enter the birth Day : "))

datesToday = myFunction(uYear,uMonth,uDate)

print("Counts of days are : " , datesToday)
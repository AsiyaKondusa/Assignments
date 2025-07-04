def is_leap(year) -> bool:
    leap = False
    if (year%4) ==0:
        if(year % 100 ==0):
            if (year % 400 ==0):
                leap= True

            else:
                leap= False
        else:
            leap= True
    else:
        leap= False
    return leap
year= int(input("Type the year here: "))
print(is_leap(year))
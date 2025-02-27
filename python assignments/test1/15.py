def get_input():
    year=int(input("enter a year"))
    return year
def leap(year):
    if (year%4==0 and year/100!=0)  or (year%400==0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not leap year")
def  main():
    year=get_input()
    leap(year)
    
main()
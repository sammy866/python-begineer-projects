def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("LEAP YEAR")
            else:
                print("Not Leap Year")
        else:
            print("LEAP YEAR")
    else:
        print("Not Leap Year")


while (True):
    def main():

        year = eval(input("Enter the year: "))

        is_leap_year(year)

    main()

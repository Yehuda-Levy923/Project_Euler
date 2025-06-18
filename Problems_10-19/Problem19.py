# check if a year is a leap year
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# get number of days in a month
def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap(year) else 28 #February
    elif month in [4, 6, 9, 11]: #September, April, June and November.
        return 30
    else:
        return 31

# count how many Sundays fell on the 1st of the month between two chosen years
def count_sundays_on_first_of_month(start_year, end_year):
    count = 0 #how many sundays
    day_of_week = 1 #monday assuming sunday is 0
    #using the fact we know the day of Jan 1 year 1 (monday) we find the day of chosen year
    for year in range(1, start_year):
        for month in range(1, 13): #13 and not 12 because range is until num - 1
            day_of_week = (day_of_week + days_in_month(year, month)) % 7

    # now check every 1st of the month from start_year to end_year
    for year in range(start_year, end_year + 1): #end_year + 1 and not end_year because range is until num - 1
        for month in range(1, 13): #13 and not 12 because range is until num - 1
            if day_of_week == 0:  # sunday
                count += 1
            day_of_week = (day_of_week + days_in_month(year, month)) % 7

    return count

if __name__ == "__main__":
    n = int(input("Enter starting year: "))
    m = int(input("Enter ending year: "))
    print(count_sundays_on_first_of_month(n, m)) #printing number of sundays on the first of the month between start and end year
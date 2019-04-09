dict = {1: "January has 31 ", 2: "February has 28", 
                      3:"March has 31",4: "April has 30",
                      5: "May has 31", 6:"June has 30", 
                      7: "July has 31", 8:"August has 31",
                      9:"September has 30", 10:"October has 31",
                      11:"November has 30", 12:"December has 31",13:"February has 29"}

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

month = int(input("input month in number :"))
year = int(input("input year :"))

if(month != 2):
        print(dict[month],"days in ",year)

elif(month == 2):
    if(is_leap_year(year)== True):
        print(dict[13],"days in ",year)
    else:
        print(dict[month],"days in ",year)


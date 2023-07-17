import time
from colorama import Fore, Back, Style, init
init(autoreset=True)


print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '''
---- LEAP YEAR ----      
      
The concept of a leap year has been around for over 2000 years and is designed to keep our calendar year synchronized with the solar year, or the length of time it takes Earth to complete its orbit around the sun, which is about 365.2422 days.

The ancient Egyptians were among the first to develop a 365-day, 12-month calendar, but it was the Romans who introduced the concept of a leap year. The Julian calendar, introduced by Julius Caesar in 46 B.C., had a simple rule to account for the slight discrepancy of the solar year not being exactly 365 days: any year evenly divisible by 4 would be a leap year. This rule over-corrected the discrepancy of the solar year.

In 1582, Pope Gregory XIII refined the rule to improve accuracy, resulting in the Gregorian calendar most widely used today. According to the Gregorian calendar, a year is a leap year if:

The year is evenly divisible by 4;
If the year can be evenly divided by 100, it is NOT a leap year, unless;
The year is also evenly divisible by 400. Then it is a leap year.
      
While the Egyptians were among the first to use a 365-day calendar, the concept of a leap year was introduced and refined by the Romans and later by Pope Gregory XIII.
''')

# Function to simulate loading or processing time
def points():
    points = [Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\n.', Style.BRIGHT + Fore.LIGHTYELLOW_EX + '.', Style.BRIGHT + Fore.LIGHTYELLOW_EX + '.', Style.BRIGHT + Fore.LIGHTYELLOW_EX + '.', Style.BRIGHT + Fore.LIGHTYELLOW_EX + '.\n']
    for point in points:
        time.sleep(0.5)
        print(point, end=" ")

# Define class LeapYear with a constructor that accepts a year as a parameter.
class LeapYear:
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        if self.year % 4 == 0:
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'\n{self.year} the year is evenly divisible by 4.')
            if self.year % 100 == 0:
                print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'\n{self.year} the year is evenly divisible by 100.')
                if self.year % 400 == 0:
                    return (Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'\n{self.year} the year is evenly divisible by 400.' + Style.BRIGHT + Fore.LIGHTGREEN_EX + '\n\n---- Is a leap year ----\n')
                
                else:
                    return (Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'\n{self.year} the year is not evenly divisible by 400.' + Style.BRIGHT + Fore.LIGHTRED_EX + '\n\n---- Is not a leap year ----\n')
            else:
                return (Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'\n{self.year} the year is not evenly divisible by 100.' + Style.BRIGHT + Fore.LIGHTGREEN_EX + '\n\n---- Is a leap year ----\n')
        else:
            return (Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'\n{self.year} the year is not evenly divisible by 4.' + Style.BRIGHT + Fore.LIGHTRED_EX + '\n\n---- Is not a leap year ----\n')

# While loop to repeat the program.
while True:
    # input year from user and store it in a variable.
    while True:
        try:
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nThis program will check if the year is a leap year or not.')
            year = int(input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nPlease enter a year: '))
            break
        except ValueError:
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "\nInvalid input! please enter a valid request.\n")

    # call function points() to simulate loading time.
    points()

    # Call the method is_leap_year() to check if the year is a leap year or not.
    leap = LeapYear(year)

    # Print the result.
    print(leap.is_leap_year())

    # Ask the user if he wants to continue or not.
    if input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "\nDo you want to repeat the program again? (y/n): ") == "yes":
        continue
    else:
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "\nThanks for using our program!")
        break
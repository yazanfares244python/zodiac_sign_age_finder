# Important module
import datetime
# Storing valid months and valid days to handle invalid inputs in lists and storing each zodiac sign with their dates
valid_months = [month for month in range(1, 13)]
valid_days = [day for day in range(1, 32)]
zodiac_signs = {         
    "Capricorn": "22/12 - 19/01",
    "Aquarius": "20/01 - 18/02",
    "Pisces": "19/02 - 20/03",
    "Aries": "21/03 - 19/04",
    "Taurus": "20/04 - 20/05",
    "Gemini": "21/05 - 20/06",
    "Cancer": "21/06 - 22/07",
    "Leo": "23/07 - 22/08",
    "Virgo": "23/08 - 22/09",
    "Libra": "23/09 - 22/10",
    "Scorpio": "23/10 - 21/11",
    "Sagitarrius": "22/11 - 21/12"
}
# Create the main class
class BirthInfoFinder:
    # Initializing each variable
    def __init__(self, current_date, birth_date):
        self.current_date = current_date
        self.birth_date = birth_date
    # Creating a function that displays the age
    def display_age(self):
        # Checking if the month of the current year has passed the birth month
        if int(self.current_date[3:5]) > int(self.birth_date[3:5]):
            # Calculating the age by subtracting the birth year from the current year
            print(f'You are {int(self.current_date[6:])-int(self.birth_date[6:])} years old')
        # Checking if the month of the current year is the same as the month of the birth year
        elif int(self.current_date[3:5]) == int(self.birth_date[3:5]):
            # Checking if the birthday has surpassed or not to calculate the age correctly
            if int(self.current_date[0:2]) >= int(self.birth_date[0:2]):
                print(f'You are {int(self.current_date[6:])-int(self.birth_date[6:])} years old')
            else:
                print(f'You are {int(self.current_date[6:])-int(self.birth_date[6:])-1} years old')
        else:
            print(f'You are {(int(self.current_date[6:])-int(self.birth_date[6:]))-1} years old')
    # Creating a function that displays the zodiac sign
    def display_zodiac_sign(self):
        # Looping through each zodiac sign value to check which one matches the birthday
        for zodiac_sign_key, zodiac_sign_value in zodiac_signs.items():
            # Check if the month is the same
            if int(self.birth_date[3:5]) == int(zodiac_sign_value[3:5]):
                # Check if the day is in the requirements
                if int(self.birth_date[0:2]) >= int(zodiac_sign_value[0:2]):
                    print(f'Your zodiac sign is {zodiac_sign_key}')
                    break
                else:
                    continue
            elif int(self.birth_date[3:5]) == int(zodiac_sign_value[11:13]):
                # Check if the day is in the requirements
                if int(self.birth_date[0:2]) <= int(zodiac_sign_value[8:10]):
                    print(f'Your zodiac sign is {zodiac_sign_key}')
                    break
                else:
                    continue
if datetime.datetime.now().month < 10:
    current_date = str(datetime.datetime.now().day) + "/" + "0" + str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().year)
else:
    current_date = str(datetime.datetime.now().day) + "/" + str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().year)
def ask_birth_date():
    return input("Enter your birth date(seperate it like this day/month(include a zero at the beginning if its only a digit)/year) ->: ")
birth_date = ask_birth_date()
while True:
    # Check 1: Check if the date contains an alphabet
    if any(letter.isalpha() for letter in birth_date):
        print("The birth date must not contain a letter")
        birth_date = ask_birth_date()
    # Check 2: Check if the date is short so we would avoid users to not add a zero before a one digit day or month
    elif len(birth_date) < 10:
        print("Date is too short perhaps you forgot to add a zero before the one digit day or month or perhaps you misclicked a typo?")
        birth_date = ask_birth_date()
    # Check 3: Check if a day is valid or not
    elif int(birth_date[0:2]) not in valid_days:
        print("Enter a valid day")
        birth_date = ask_birth_date()
    # Check 4: Check if a month is valid or not
    elif int(birth_date[3:5]) not in valid_months:
        print("Enter a valid month")
        birth_date = ask_birth_date()
    else:
        break
find_birth_info = BirthInfoFinder(current_date, birth_date)
find_birth_info.display_age()
find_birth_info.display_zodiac_sign()
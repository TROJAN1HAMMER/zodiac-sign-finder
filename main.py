print("Hi!")
name = input("What is your name:")

# The input is given for getting zodiac signs

birth_date = int(input("What is your birth date:"))
birth_month = (input("What is the month of your birth:"))

print("Since your birth month is:", birth_month)
print("And Since your birth date is:", birth_date)

# For defying zodiac signs in january

if birth_month == "january":
    if birth_date in range(1, 23):
        print("Your zodiac sign is Capricornus.")
    if birth_date in range(23, 32):
        print("Your zodiac sign is Aquaiurs.")

# For defying zodiac signs in feburary

elif birth_month == "feburary":
    if birth_date in range(1, 19):
        print("Your zodiac sign is Aquaiurs.")
    if birth_date in range(19, 31):
        print("Your zodiac sign is Pisces.")

elif birth_month == "march":
    if birth_date in range(1, 21):
        print("Your zodiac sign is Pisces.")
    if birth_date in range(21, 32):
        print("Your zodiac sign is Aries.")

elif birth_month == "april":
    if birth_date in range(1, 20):
        print("Your zodiac sign is Aries.")
    if birth_date in range(20, 32):
        print("Your zodiac sign is Tarus.")

elif birth_month == "may":
    if birth_date in range(0, 21):
        print("Your zodiac sign is Tarus.")
    if birth_date in range(21, 32):
        print("Your zodiac sign is Gemini.")

elif birth_month == "june":
    if birth_date in range(1, 22):
        print("Your zodiac sign is Gemini.")
    if birth_date in range(22, 32):
        print("Your zodiac sign is Cancer.")

elif birth_month == "july":
    if birth_date in range(1, 23):
        print("Your zodiac sign is Cancer.")
    if birth_date in range(23, 32):
        print("Your zodiac sgn is Leo.")

elif birth_month == "august":
    if birth_date in range(1, 23):
        print("Your zodiac sign is Leo.")
    if birth_date in range(23, 32):
        print("Your zodiac sign is Virgo.")

elif birth_month == "september":
    if birth_date in range(1, 23):
        print("Your zodiac sign is Virgo.")
    if birth_date in range(23, 32):
        print("Your zodiac sign is Libra.")

elif birth_month == "October":
    if birth_date in range(1, 25):
        print("Your zodiac sign is Libra.")
    if birth_date in range(25, 32):
        print("Your zodiac sign is Scorpius")

elif birth_month == "november":
    if birth_date in range(1, 23):
        print("Your zodiac sign is Scorpius.")
    if birth_date in range(23, 32):
        print("Your zodiac sign is Sagattarius.")

elif birth_month == "december":
    if birth_date in range(1, 23):
        print("Your zodiac sign is Sagattarius.")
    if birth_date in range(23, 32):
        print("YOur zodiac sign is Capricornus.")

print("Thank you for using this, " ,name )
print("hope your found your zodiac sign.")

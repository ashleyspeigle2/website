## Ashley Speigle
## This program gives you a horoscope when you enter your birth month and day.

from datetime import date

def main():
    
    month = input("Please enter your birth month(1-12): ")
    day = input("Please enter you birth day: ")
    Zodiac = zodiac(month,day)
    print(Zodiac)

def zodiac(month,day):
    if((int(month)== 12 and int(day) >= 22)or(int(month)== 1 and int(day)<= 20)):
        return("\n Capricorn \n This month you will experience heartbreak.")
    
    elif((int(month)== 1) and (int(day)>= 21) or (int(month) == 2) and(int(day) <= 19)):
        return ("\n Aquarius \n You will get all A's on your test.")
            
    elif((int(month)== 2 and int(day) >= 20)or(int(month)== 3 and int(day)<= 20)):
        return("\n Pisces \n This month you will be asked out on a date.")

    elif((int(month)== 3 and int(day) >= 21)or(int(month)== 4 and int(day)<= 20)):
        return("\n Aries \n This month you will recieve a great amount of money.")

    elif((int(month)== 4 and int(day) >= 21)or(int(month)== 5 and int(day)<= 21)):
        return("\n Taurus \n This month you will have an accident.")

    elif((int(month)== 5 and int(day) >= 22)or(int(month)== 6 and int(day)<= 21)):
        return("\n Gemini \n This month you will win the lottery.")

    elif((int(month)== 6 and int(day) >= 22)or(int(month)== 7 and int(day)<= 22)):
        return("\n Cancer \n This month you will win a gaming console.")

    elif((int(month)== 7 and int(day) >= 23)or(int(month)== 8 and int(day)<= 23)):
        return("\n Leo \n This month no one is going to give you gifts.")

    elif((int(month)== 8 and int(day) >= 24)or(int(month)== 9 and int(day)<= 23)):
        return("\n Virgo \n You will have great luck.")

    elif((int(month)== 9 and int(day) >= 24)or(int(month)== 10 and int(day)<= 23)):
        return("\n Libra \n This month you will get A's on all your tests.")

    elif((int(month)== 10 and int(day) >= 24)or(int(month)== 11 and int(day)<= 22)):
        return("\n Scorpio \n This month your house will burn down.")
        
    elif((int(month)== 11 and int(day) >= 23)or(int(month)== 12 and int(day)<= 21)):
        return("\n Sagittarious \n This month you will get a raise at work.")


    
              
main()

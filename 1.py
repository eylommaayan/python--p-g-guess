import random
import time # סיפריית מעקב זמנים
print(" Hi Welcone to the guessing game. Pleas guess a number between 1 and 100")
time.sleep(3) # כמות זמן לחכות להמשך הקוד
print("Picking a number...")
time.sleep(2)
guess = int(input(" what is your guss?: ")) 
correct_number = random.randint(1, 100) # תשובה רנדומלית
guess_count =0 # התחלה ניחושים

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
     guess = int(input("worng, you need to guess higher: ")) 
    else:
     guess = int(input("worng, you need to guess lower: "))    

print(f"Congrats! you got the right answae {correct_number} it took you {guess_count} guesses ") # הדפסה עם פונקציות של מה יקרה כאשר ינחשו נכון
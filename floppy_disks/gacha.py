import random

chars = ["\033[35m★★★★ Hoshino", "\033[35m★★★★ Hina", "\033[33m★★★ Miyo", "\033[33m★★★ Mari", "\033[33m★★★ Junko", "\033[34m★★ Juri", "\033[34m★★ Suzumi", "\033[34m★★ Serina"]
# to other blue archive players, im so sorry because i forgot their star rating hehe

def gachaDice():
    roll = random.randint(0,7)
    return roll

money = 6
print("Welcome, Sensei, to The Cute & Funny Gacha Roll Page!!")

while money != 0:
    result = chars[gachaDice()]
    print("\n\nMoney counter: \033[32m" + str(money) + "\033[39m")
    input("Press 'Enter' to roll!")
    print("Congratulations! You got " + result + "\033[39m")
    money = money - 1

    retry = input("Do you want to try again? (Press anything, or type 'no'): ").lower()
    if retry == "no":
        print("Thank you for the generous donations!")
        break
    elif money == 0:
        topup = input("\n\033[31mUh oh, seems like you don't have any money left now Sensei... Do you want to topup? (yes/no): \033[39m").lower()
        if topup == "yes":
            money = 6
            print("ALright! Better luck this time, Sensei!")
            
        else:
            print("Thank you for the generous donations!")
            break
    else:
        print("Good luck, Sensei!")
    
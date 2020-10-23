from car import Car
from player import Player
from menu import menu
import time



#Menu.main_menu()
# name = (input("Enter your Name: "))
# player = Player(name)
# print(f"\nWelcome to RACING WORLD {player.name}!! You have ${player.bank_account} in your account!\n")



#======Races your car against an opponent of your choice
def race():
    race_menu()                  #=====opponent menu
    seconds= int(input("Enter race duration in seconds: "))
    winnings = int(input("Enter amount to bet:"))
    print("*********Your Opponent is Starting his Engine!!!!***********")
    time.sleep(0.5)
    clock = "fiv"
    for i in clock:
        print("*")
        time.sleep(0.5)
    i = 0
    print("*********Race is about to Start!!!***********")
    time.sleep(0.5)
    clock = "five"
    for i in clock:
        print("*")
        time.sleep(0.5)
    i = 0
    while i < seconds:
        for car_name in all_cars:
            opponent.move
            my_car.move()
        i += 1
    print("*********Race is over!!!***********")
    if my_car.postion > opponent.position:
        print(f"\n       !!!!!!You Won $${winnings}!!!!!!")
        Player.wins(self, winnings)
    else:
        print(f"\n       :(:(:(You Won $${winnings}:(:(:(")
        Player.loses(self,winnings)

menu.main_menu()
#options_menu()
#print(buy_car_menu())
#buy_mods()
#buy_decals()


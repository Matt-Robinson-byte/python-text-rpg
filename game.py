from car import Car
from player import Player
from menu import menu
import time
from colorama import Back
from subprocess import call
import os

def clear():
    call('clear' if os.name == 'posix' else 'cls')

#Menu.main_menu()
# name = (input("Enter your Name: "))
# player = Player(name)
# print(f"\nWelcome to RACING WORLD {player.name}!! You have ${player.bank_account} in your account!\n")



#======Races your car against an opponent of your choice
def race():
    menu.race_menu()                  #=====opponent menu
    seconds= int(input("Enter race duration in seconds: "))
    winnings = int(input("Enter amount to bet:"))
    print("*********Your Opponent is Starting his Engine!!!!***********")
    time.sleep(0.5)
    clock = "fiv"
    for i in clock:
        print("*")
        time.sleep(0.5)
    i = 3
    print("*********Race is about to Start!!!***********")
    time.sleep(0.5)
    clock = "five"
    for i in clock:
        print(Back.GREEN)
        time.sleep(0.5)
    i = 0
    while i < seconds:
        opponent.move()
        my_car.move()
        i += 1
    print("*********Race is over!!!***********")
    if my_car.position > opponent.position:
        print(f"\n   !!!!!!You Won $${winnings}!!!!!!")
        player.wins(winnings)
    else:
        print(f"\n       :(:(:(You lose $${winnings}:(:(:(")
        player.loses(winnings)
    print(f"Account balance {player.bank_account}")
    my_car.wear_tear()
    print(f"Your car health is at {my_car.wear}")
    menu.options_menu()


menu.main_menu()
#options_menu()
#print(buy_car_menu())
#buy_mods()
#buy_decals()


from car import Car
from player import Player
from menu import Menu
import time

name = (input("Enter your Name: "))
player = Player(name, 1000)

cars = {
    "PT Cruiser"     : Car(80,6),
    "Toyota Corolla" : Car(100,8),
    "Ford Mustang"   : Car(125,6),
    "Lambo Diablo"   : Car(130,7),
    "Bugatti Chiron" : Car(135,8)
}

#======Races your car against an opponent of your choice
def race():
    race_menu()                  #=====opponent menu
    seconds= int(input("Enter race duration in seconds: "))
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
        i += 1
    print("*********Race is over!!!***********")
    if my_car.postion > opponent.position:
        print(f"\n       !!!!!!You Won $${winnings}!!!!!!")
    else:
        print(f"\n       :(:(:(You Won $${winnings}:(:(:(")

Menu.main_menu(self)
#options_menu()
#print(buy_car_menu())
#buy_mods()
#buy_decals()


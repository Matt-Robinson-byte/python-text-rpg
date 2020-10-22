from car import Car
from player import Player
from menu import menu
import time


cars = [
    Car("PT Cruiser",80,6),
    Car("Toyota Corolla",100,8),
    Car("Ford Mustang",125,6),
    Car("Lambo Diablo",130,7),
    Car("Bugatti Chiron",135,8)
]
#Menu.main_menu()
# name = (input("Enter your Name: "))
# player = Player(name, 1000)



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
            my_car.move()
        i += 1
    print("*********Race is over!!!***********")
    if my_car.postion > opponent.position:
        print(f"\n       !!!!!!You Won $${winnings}!!!!!!")
    else:
        print(f"\n       :(:(:(You Won $${winnings}:(:(:(")

menu.main_menu()
#options_menu()
#print(buy_car_menu())
#buy_mods()
#buy_decals()


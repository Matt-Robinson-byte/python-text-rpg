from player import Player
from car import Car
import time
from subprocess import call
from colorama import Back, Style
import os

def clear():
    call('clear' if os.name == 'posix' else 'cls')
clear()

car = [
    Car("PT Cruiser",80,6, 500),
    Car("Toyota Corolla",100,8, 1500),
    Car("Ford Mustang",125,6, 3000),
    Car("Lambo Diablo",130,7, 5000),
    Car("Bugatti Chiron",135,8, 10000)
]
name = (input("Enter your Name: "))
player = Player(name)
print(f"\nWelcome to RACING WORLD {player.name}!! You have ${player.bank_account} in your account!\n")
time.sleep(2)    
# my_car = None
# opponent = None
winnings = 0
car_value = 0


class Menu():
    pass
    def main_menu(self):
        menu = '''********** Main Menu ************   \n Option         Description\n 1.             Purchase Car             
 2.              Exit      \n\n Enter option:  \n''' 
        try:
            option = int(input(menu))
        except ValueError:
            print("Not an option")
            self.main_menu()
        if option == 1:
            self.buy_car_menu()
        else:
            self.leave_game()
        clear()

    #options menu
    def options_menu(self):
        clear()
        options = f'''********** Menu ************    Account Balance: {player.bank_account}\n Option         \n 1.          Buy Mods         
 2.          Buy Decals     \n 3.          Race          \n 4.          Sell Car\n 5.          Main Menu\n\n Enter choice:  '''
        try:
            choice = (int(input(options)))
        except ValueError:
            print("Not a valid choice")
            self.options_menu()
        if choice == 1:
            self.buy_mods()
        elif choice == 2:
            self.buy_decals()
        elif choice == 3:
            race()
        elif choice == 4:
            try:
                player.sell_car(my_car.price)
                my_car.price = 0
                self.main_menu()
            except AttributeError:
                print("You don't own a car yet")
                time.sleep(2)
                self.options_menu()
        elif choice == 5:
            self.main_menu()
        else:
            print("Option not valid")
            self.options_menu()
        

    #player chooses car to purchase
    def buy_car_menu(self):
        global my_car
        clear()
        car_menu = f'''********** Car Options ************     Account Balance: {player.bank_account}\n Option         Car            Price\n 1.         PT Cruiser         $500
 2.        Toyota Corolla      $1,500\n 3.         Ford Mustang       $3,000\n 4.         Lambo Diablo       $5,000\n 5.        Bugatti Chiron      $10,000\n 6.        Options menu      
    \n\n Enter choice:  '''
        car_choice = int(input(car_menu))
        print("\n")
        i = 0
        while i < len(car):
            if car_choice == i + 1:
                my_car = car[i]
            i += 1  
        clear()
        if player.bank_account > my_car.price:
            player.purchase(my_car.price)
            print(f"Your balance is {player.bank_account}\n\n")
            print("*****We are getting your order ready*****")
            time.sleep(0.5)
            clock = "fiv"
            for i in clock:
                print("*")
                time.sleep(0.5)
            i = 0
            print(f"\nCongratulations!!  You bought a {my_car.name}\n")
            print(f"Your top speed is {my_car.top_speed} and accelerates {my_car.acceleration}")
        else:
            print("Not enough funds, choose a different car!\n\n")
            self.buy_car_menu()
        time.sleep(2) 
        self.options_menu()
        return my_car
        

    #allows player to modify his car by purchasing mods
    def buy_mods(self):
        clear()
        mod_menu = f'''********** Mods Menu ************         Account Balance: {player.bank_account}\n Option     Mod          Price\n 1.        Blower         $100\n 2.        Tires          $150\n 3.        Nos            $200\n 4.        Repair         $40\n 5.        Exit         \n\n Enter choice:  '''
        try: 
            mod = int(input(mod_menu))
        except ValueError:
            print("Not an option")
            self.buy_mods()
        if mod == 1:
            price = 100
            my_car.blower_mod()
            player.purchase(price)   
        elif mod == 2:
            price = 150
            my_car.tires_mod()
            player.purchase(price)
        elif mod == 3:
            price = 200
            my_car.nos_mod()
            player.purchase(price)
        elif mod == 4:
            price = 40
            my_car.repair_mod()
            player.purchase(price)
        elif mod == 5:
            self.options_menu()
        else:
            print("Not a valid option")
        print (f"Your new top speed is {my_car.top_speed} and your acceleration is {my_car.acceleration}")
        time.sleep(3)
        self.options_menu()


    # allows player to buy stickers for his car
    def buy_decals(self):
        clear()
        decal_menu =f'''********** Decals Menu ************       Account Balance: {player.bank_account}\n Option         Decal          Price\n 1.            **Fire**         $10
 2.       OO Spin Master OO     $15\n 3.          --==Speed          $20\n\n Enter choice to purchase:  ''' 
        decal = int(input(decal_menu))

    #======opponent menu to race------called in race()function
    def race_menu(self):
        clear()
        global opponent
        opponent_menu = f'''**** WHO DO YOU WANT TO RACE?!?! ****    Account Balance: {player.bank_account}\n Option         Car            \n 1.         PT Cruiser         
 2.        Toyota Corolla      \n 3.         Ford Mustang       \n 4.         Lambo Diablo       \n 5.        Bugatti Chiron     
    \n\n Enter choice:  '''
        try:
            choice = int(input(opponent_menu))
        except:
            print("Invalid choice")
            self.race_menu()
        i = 0
        if choice == 6:
            self.options_menu()
        else:
            while i < len(car):
                if choice == i + 1:
                    opponent = car[i]
                    damage = i + 1
                i += 1  
        return damage
     
def race():
    clear()
    my_car.reset()
    menu.race_menu()
    opponent.position = 0
    opponent.reset()                #=====opponent menu
    print(f"Your opponent's top speed is {opponent.top_speed} and accelerates {opponent.acceleration}")
    seconds= int(input("Enter race duration in seconds: "))
    winnings = int(input("Enter amount to bet:"))
    time.sleep(.5)
    clear()
    colors = ['RED','YELLOW','GREEN']
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
    while i < 4:
        if i == 0:
            print(Back.YELLOW + "                ")
        elif i == 1:
            print(Back.GREEN + "                ")
        else:
            print(Back.RED + "                ")
        time.sleep(1)
        i += 1
    print(Style.RESET_ALL)
    i = 0
    while i < seconds:
        opponent.move()
        my_car.move()
        i += 1
    print("*********Race is over!!!***********")
    print(f"You went {my_car.position} meters. Opponent {opponent.position}")
    if my_car.position > opponent.position:
        print(f"\n   !!!!!!You Won $${winnings}!!!!!!")
        player.wins(winnings)
    elif my_car.position == opponent.position:
        print("You tied!!!")
    else:
        print(f"\n       :(:(:(You lose $${winnings}:(:(:(")
        player.loses(winnings)
    print(f"Account balance {player.bank_account}")
    my_car.wear_tear()
    print(f"Your car health is at {my_car.wear}")
    time.sleep(6)
    menu.options_menu()
menu = Menu()


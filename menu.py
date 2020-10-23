from player import Player
from car import Car
import time


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
my_car = Car("PT Cruiser",80,6, 500)
opponent = Car("Bugatti Chiron",135,8, 10000)
winnings = 0


class Menu():
    pass
    def main_menu(self):
        menu = '''********** Main Menu ************   \n Option         Description\n 1.             Purchase Car             
 2.              Exit      \n\n Enter option:  \n''' 
        option = int(input(menu))
        if option == 1:
            self.buy_car_menu()
        else:
            self.leave_game()

    #options menu
    def options_menu(self):
        options = f'''********** Menu ************    Account Balance: {player.bank_account} \n Option         \n 1.          Buy Mods         
 2.          Buy Decals     \n 3.          Race          \n 4.          Sell Car\n 5.          Main Menu\n\n Enter choice:  '''
        choice = (int(input(options)))
        if choice == 1:
            self.buy_mods()
        elif choice == 2:
            self.buy_decals()
        elif choice == 3:
            race()
        elif choice == 4:
            self.sell_car()
        elif choice == 5:
            self.main_menu()
        else:
            print("Option not valid")
            self.options_menu()
        

    #player chooses car to purchase
    def buy_car_menu(self):
        car_menu = f'''********** Car Options ************     Account Balance: {player.bank_account}\n Option         Car            Price\n 1.         PT Cruiser         $500
 2.        Toyota Corolla      $1,500\n 3.         Ford Mustang       $3,000\n 4.         Lambo Diablo       $5,000\n 5.        Bugatti Chiron      $10,000\n 6.        Options menue      
    \n\n Enter choice:  '''
        car_choice = int(input(car_menu))
        print("\n")
        i = 0
        while i < len(car):
            if car_choice == i + 1:
                my_car = car[i]
            i += 1  
        
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
        print(f"\n Congratulations!!  You bought a {my_car.name}{my_car.top_speed}\n")
        self.options_menu()
        return my_car
        

    #allows player to modify his car by purchasing mods
    def buy_mods(self):
        mod_menu = f'''********** Mods Menu ************         Account Balance: {player.bank_account}\n Option     Mod          Price\n 1.        Blower         $100\n 2.        Tires          $150\n 3.        Nos            $200\n 4.        Repair         $40\n 5.        Exit         \n\n Enter choice:  '''
        mod = int(input(mod_menu))
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
        self.options_menu()


    # allows player to buy stickers for his car
    def buy_decals(self):
        decal_menu =f'''********** Decals Menu ************       Account Balance: {player.bank_account}\n Option         Decal          Price\n 1.            **Fire**         $10
 2.       OO Spin Master OO     $15\n 3.          --==Speed          $20\n\n Enter choice to purchase:  ''' 
        decal = int(input(decal_menu))

    #======opponent menu to race------called in race()function
    def race_menu(self):
        opponent_menu = '''**** WHO DO YOU WANT TO RACE?!?! ****\n Option         Car            \n 1.         PT Cruiser         
 2.        Toyota Corolla      \n 3.         Ford Mustang       \n 4.         Lambo Diablo       \n 5.        Bugatti Chiron     
    \n\n Enter choice:  '''
        try:
            choice = int(input(opponent_menu))
        except:
            print("Valid choice")
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
    menu.race_menu()                  #=====opponent menu
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
menu = Menu()


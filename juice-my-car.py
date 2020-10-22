import time
class Car():
    def __init__(self, top_speed , acceleration,tires = False,speed = 0,position = 0,nos = False,decals = "",blower = False,wear = 50):
        self.tires = False
        self.speed = 0
        self.top_speed = top_speed
        self.position = 0
        self.acceleration = acceleration
        self.nos = False
        self.decals = 0
        self.blower = False
        self.wear = 50
        
    def blower(self):
        self.blower != self.blower

    def nos(self):
        self.nos != self.nos

    def tires(self):
        self.tires != self.tires
    
    def repair(self):
        if wear < 50:
            wear = 50

    def wear_tear(self):
        self.wear -= 1


class player():
    def __init__(self, name,  mods, decals,bank_account = 1000):
        self.name = name
        self.mods = mods
        self.decals = decals
        self.bank_account = bank_account



def purchase(menu, item):
    self.bank_account -= menu[i][item]

def credit():
    self.bank_account += winnings




cars = {
    "PT Cruiser"     : Car(80,6),
    "Toyota Corolla" : Car(100,8),
    "Ford Mustang"   : Car(125,6),
    "Lambo Diablo"   : Car(130,7),
    "Bugatti Chiron" : Car(135,8)
}

def main_menu():
    menu = '''********** Main Menu ************\n Option         Description\n 1.             Purchase Car             
 2.              Exit      \n\n Enter option:  \n''' 
    option = int(input(menu))
    if option == 1:
        buy_car_menu()
    else:
        leave_game()

#options menu
def options_menu():
    options = '''********** Menu ************\n Option         \n 1.          Buy Mods         
 2.          Buy Decals     \n 3.          Race          \n 4.          Sell Car\n 5.          Main Menu\n\n Enter choice:  '''
    choice = (int(input(options)))
    if choice == 1:
        buy_mods()
    elif choice == 2:
        buy_decals()
    elif choice == 3:
        race()
    elif choice == 4:
        sell_car()
    elif choice == 5:
        main_menu()
    else:
        print("Option not valid")
        options_menu()

#player chooses car to purchase
def buy_car_menu():
    car_menu = '''********** Car Options ************\n Option         Car            Price\n 1.         PT Cruiser         $500
 2.        Toyota Corolla      $1,500\n 3.         Ford Mustang       $3,000\n 4.         Lambo Diablo       $5,000\n 5.        Bugatti Chiron      $10,000
 \n\n Enter choice to purchase:  '''
    car_choice = int(input(car_menu))
    my_car = cars[car_choice - 1]
    return my_car

#allows player to modify his car by purchasing mods
def buy_mods():
    mod_menu = '''********** Mods Menu ************\n Option     Mod          Price\n 1.        Blower         $100\n 2.        Tires          $150\n 3.        Nos            $200\n 4.        Repair            $40\n\n Enter choice to purchase:  '''
    mod = int(input(mod_menu))


# allows player to buy stickers for his car
def buy_decals():
    decal_menu ='''********** Decals Menu ************\n Option         Decal          Price\n 1.            **Fire**         $10
 2.       OO Spin Master OO     $15\n 3.          --==Speed          $20\n\n Enter choice to purchase:  ''' 
    decal = int(input(decal_menu))

#======opponent menu to race------called in race()function
def race_menu():
    opponent_menu = '''**** WHO DO YOU WANT TO RACE?!?! ****\n Option         Car            \n 1.         PT Cruiser         
 2.        Toyota Corolla      \n 3.         Ford Mustang       \n 4.         Lambo Diablo       \n 5.        Bugatti Chiron     
 \n\n Enter choice:  '''
    opponent = int(input(opponent_menu))
    return opponent


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

main_menu()
#options_menu()
print(buy_car_menu())
#buy_mods()
#buy_decals()


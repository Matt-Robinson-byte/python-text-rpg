from car import Cars
class Menu():
    pass
    def main_menu(self):
        menu = '''********** Main Menu ************\n Option         Description\n 1.             Purchase Car             
    2.              Exit      \n\n Enter option:  \n''' 
        option = int(input(menu))
        if option == 1:
            self.buy_car_menu()
        else:
            self.leave_game()

    #options menu
    def options_menu(self):
        options = '''********** Menu ************\n Option         \n 1.          Buy Mods         
    2.          Buy Decals     \n 3.          Race          \n 4.          Sell Car\n 5.          Main Menu\n\n Enter choice:  '''
        choice = (int(input(options)))
        if choice == 1:
            self.buy_mods()
        elif choice == 2:
            self.buy_decals()
        elif choice == 3:
            self.race()
        elif choice == 4:
            self.sell_car()
        elif choice == 5:
            self.main_menu()
        else:
            print("Option not valid")
            self.options_menu()

    #player chooses car to purchase
    def buy_car_menu(self):
        car_menu = '''********** Car Options ************\n Option         Car            Price\n 1.         PT Cruiser         $500
    2.        Toyota Corolla      $1,500\n 3.         Ford Mustang       $3,000\n 4.         Lambo Diablo       $5,000\n 5.        Bugatti Chiron      $10,000
    \n\n Enter choice to purchase:  '''
        car_choice = int(input(car_menu))
        if car_choice == 1:
            my_car = cars["PT Cruiser"]
        elif car_choice == 2:
            my_car = cars["Toyota Corolla"]
        elif car_choice == 3:
            my_car = cars["Ford Mustang"]
        elif car_choice == 4:
            my_car = cars["Lambo Diablo"]
        elif car_choice == 5:
            my_car = cars["Bugatti Chiron"]
        else: 
            print("Not a valid choice")
        
        return my_car

    #allows player to modify his car by purchasing mods
    def buy_mods(self):
        mod_menu = '''********** Mods Menu ************\n Option     Mod          Price\n 1.        Blower         $100\n 2.        Tires          $150\n 3.        Nos            $200\n 4.        Repair            $40\n\n Enter choice to purchase:  '''
        mod = int(input(mod_menu))


    # allows player to buy stickers for his car
    def buy_decals(self):
        decal_menu ='''********** Decals Menu ************\n Option         Decal          Price\n 1.            **Fire**         $10
    2.       OO Spin Master OO     $15\n 3.          --==Speed          $20\n\n Enter choice to purchase:  ''' 
        decal = int(input(decal_menu))

    #======opponent menu to race------called in race()function
    def race_menu(self):
        opponent_menu = '''**** WHO DO YOU WANT TO RACE?!?! ****\n Option         Car            \n 1.         PT Cruiser         
    2.        Toyota Corolla      \n 3.         Ford Mustang       \n 4.         Lambo Diablo       \n 5.        Bugatti Chiron     
    \n\n Enter choice:  '''
        choice = int(input(opponent_menu))
        if choice == 1:
            opponent = cars["PT Cruiser"]
        elif choice == 2:
            opponent = cars["Toyota Corolla"]
        elif choice == 3:
            opponent = cars["Ford Mustang"]
        elif choice == 4:
            opponent = cars["Lambo Diablo"]
        elif choice == 5:
            opponent = cars["Bugatti Chiron"]
        else: 
            print("Not a valid choice")    
        return opponent


menu = Menu()

from player import Player
class Car():
    def __init__(self,name, top_speed , acceleration, price, tires = False,speed = 0,position = 0,nos = False,decals = "",blower = False,wear = 50):
        self.name = name
        self.tires = tires
        self.speed = 0
        self.top_speed = top_speed
        self.position = 0
        self.acceleration = acceleration
        self.nos = nos
        self.decals = 0
        self.blower = blower
        self.wear = 50
        self.price = price
    
    def accelerate(self):
        self.speed += self.acceleration
        if self.speed > self.top_speed:
            self.speed = self.top_speed

    def move(self):
        self.accelerate()
        self.position += self.speed

    def blower_mod(self):
        self.blower = True
        self.top_speed += 10
        self.acceleration += 1
        

    def nos_mod(self):
        self.top_speed += 20
        self.acceleration += 3

    def tires_mod(self):
        self.top_speed += 5
        self.acceleration += 2
    
    def repair_mod(self):
        if self.wear < 50:
            self.wear = 50

    def wear_tear(self):
        self.wear -= 5
    
    def has_decals(self):
        self.top_speed += 2
    

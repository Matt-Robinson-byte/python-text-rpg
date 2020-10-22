class Car():
    def __init__(self, top_speed , acceleration,tires = False,speed = 0,position = 0,nos = False,decals = "",blower = False,wear = 50):
        self.tires = tires
        self.speed = 0
        self.top_speed = top_speed
        self.position = 0
        self.acceleration = acceleration
        self.nos = nos
        self.decals = 0
        self.blower = blower
        self.wear = 50
        
    def blower(self):
        if self.blower == False:
            self.blower = True
        else:
            self.blower = False
        

    def nos(self):
        if self.nos == False:
            self.nos = True
        else:
            self.nos = False

    def tires(self):
        if self.tires == False:
            self.tires = True
        else:
            self.tires = False
    
    def repair(self):
        if wear < 50:
            wear = 50

    def wear_tear(self):
        self.wear -= 1
    
    
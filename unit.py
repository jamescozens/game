from location import Location
from movementVector import MovementVector
from weapon import Weapon

class Unit:

    def __init__(self):
        # self.location = Location(0,0)
        # self.movement = MovementVector(1,2)
        print("Calling child constructor")
        self.__name = "infantry"
        self.__skillRatio = 40
        self.__moraleRatio = 50   
        self.__exhausionRatio = 20
        self.__weaponsArray = [Weapon(), Weapon()]

    def __str__( self ):   
        return  f'x= {self.__name} y = {self.__skillRatio} '

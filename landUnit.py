from unit import Unit
from location import Location
from movementVector import MovementVector

class LandUnit(Unit):

    def __init__(self):
        #super().__init__(self)

        self.__name = "infantry"
        self.__skillRatio = 40
        self.__moraleRatio = 50   
        self.__exhausionRatio = 20
        self.__weaponsArray = []

        self.__location = Location(0,0)
        self.movement = MovementVector(1,2)

    def __str__( self ):   
        return  f'The square root of {self.__name} is {self.__skillRatio} (roughly).'
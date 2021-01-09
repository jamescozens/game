from weaponEffect import WeaponEffect

class Weapon:

    def __init__(self):
        print("Calling child constructor")
        # self.effectiveness = WeaponEffect()
        self.__name = "rifle"
        self.__movementPenalty = 34


    def __str__( self ):   
        return  f'x= {self.__name} y = {self.__movementPenalty} '

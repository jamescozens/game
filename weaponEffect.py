class WeaponEffect:

    def __init__(self):
        print("Calling child constructor")
        self.__damagePerSecond = 10 
        self.__range = 1 
        self.__hitProbabilty = 90
        self.__areaOfEffectRadius  =  1 #  (damage dispersal)
        self.__relaibility  = 40
        self.__ammoPerSecond = 1 
        self.__productionResource = 20        


    def __str__( self ):   
        return  f'x= {self.__damagePerSecond} y = {self.__areaOfEffectRadius} '

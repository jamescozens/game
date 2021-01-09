


class ArmourEffect:

    def __init__(self):
        print("Calling child constructor")
        self.__effectiveness
        self.__productionResource = 20        


    def __str__( self ):   
        return "Calling child constructor xxxxx"


x = ArmourEffect()
print(x)
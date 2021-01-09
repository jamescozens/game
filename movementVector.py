class MovementVector:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__( self ): 
        return   f'x= {self.__x} y = {self.__y} '
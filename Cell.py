from Pos import Pos
from Checker import Checker


class Cell:
    def __init__(self,x=0,y=0,c=None):
        self.__pos = Pos(x,y)
        self.__checker = None
        if c and c!='e':
            self.__checker = Checker(self,c)

    def get_checker(self):
        return self.__checker

    def get_pos(self):
        return self.__pos

    def set_pos(self,newPos):
        self.__pos=newPos

    def set_checker(self,newChecker):
        self.__checker = newChecker
from Pos import Pos

class Checker:
    def __init__(self,cell,c):
        if(c=='m'):
            self.__ismychecker = True
        else:
            self.__ismychecker = False
        self.__cell = cell

    def isMyChecker(self):
        return self.__ismychecker

    def get_cell(self):
        return self.__cell

    def get_pos(self):
        return self.__cell.get_pos()

from Cell import Cell
from Pos import Pos
from Checker import Checker

class Board:
    def __init__(self):
        self.__cells = {}
        self.__myCells = {}
        self.__oppCells = {}
        self.__emptyCells = {}
        for i in range(0, 8):
            for j in range(0, 3):
                    self.__cells[(i,j)] = Cell(i,j)

    def update(self, s):
        self.__myCells.clear()
        self.__oppCells.clear()
        self.__emptyCells.clear()
        for i in range(0,8):
            for j in range(0,3):
                cell = self.__cells[(i,j)]
                cell.set_checker(None)
                if s[0] != 'e':
                    # if self.__cells[(i,j)].get_checker() != None:
                    #     del self.__cells([i,j]).get_checker()
                    cell.set_checker(Checker(cell, s[0]))
                    if s[0]=='m':
                        self.__myCells[(i,j)] = cell
                    else:
                        self.__oppCells[(i,j)] = cell
                else:
                    self.__emptyCells[(i, j)] = cell
                if len(s) > 2:
                    s = s[2:]

    def get_neighbors(self, cell):
        if hasattr(cell, "neigbors"):
            return cell.neigbors
        cell.neighbors = []
        y = cell.get_pos().gety()
        x = cell.get_pos().getx()
        if y < 2:
            cell.neighbors.append(self.__cells[(x,y + 1)])
        elif y > 0:
            cell.neighbors.append(self.__cells[(x,y - 1)])
        cell.neighbors.append(self.__cells[((x + 1) % 8,y)])
        cell.neighbors.append(self.__cells[((x - 1) % 8,y)])
        return cell.neighbors


    def get_cells(self):
        return self.__cells

    def get_mycells_dict(self):
        return self.__myCells

    def get_mycells(self):
        return list(self.__myCells.values())

    def get_oppcells_dict(self):
        return self.__oppCells

    def get_oppcells(self):
        return list(self.__oppCells.values())

    def get_emptycells_dict(self):
        return self.__emptyCells

    def get_emptycells(self):
        return list(self.__emptyCells.values())

    def get_cell(self, x=0, y=0, p=None):
        if p is None:
            return self.__cells[(x,y)]
        else:
            return self.__cells[(p.getx(),p.gety())]

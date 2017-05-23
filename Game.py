from Board import Board
from Checker import Checker
from put_strategy import put_strategy
from pop_strategy import pop_strategy
from move_strategy import move_strategy
import socket
from time import sleep

def simplelinesplit(sock):
    data = ""
    try:
        while True:
            # sock.settimeout(1)
            data += (sock.recv(1).decode())
            if len(data) > 0 and data[-1] == '\n':
                break
    except Exception as e:
        pass
    finally:
        return data


class Game:
    def __init__(self, s):
        self.__board = Board()
    def __init__(self,serveraddress, serverport, name):
        self.__board = Board()
        self.__msg_send=""
        self.__msg_recieved=""
        self.__server_address = serveraddress
        self.__server_port = serverport
        self.__teamname = name
        self.__socket = None

    def get_board(self):
        return self.__board

    def start_client(self):
        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.connect((self.__server_address, self.__server_port))
            return True
        except:
            return False

    def start(self):
        self.__socket.sendall(bytes('REGISTER %s\n' % self.__teamname, "utf-8"))
        while(True):
            data = str(simplelinesplit(self.__socket))
            if data is None or len(data) == 0 or data == "FINISH":
                print("Game is Over")
                break
            self.play_round(data)


    def play_round(self,message):
        self.__board.update(message[0:47])
        message = message[48:]
        ss = list(map(int,message.split(',')))
        self.__myinhandcheckernum = ss[0]
        self.__oppinhandcheckernum = ss[1]
        self.__cycle = ss[2]

        if self.__myinhandcheckernum > 0:
            dooz = put_strategy(self)
        else:
            dooz = move_strategy(self)

        if dooz:
            pop_strategy(self)

        self.__socket.sendall(bytes("%s\n" % self.__msg_send, "utf-8"))

    def getMyinhandcheckernum(self):
        return self.__myinhandcheckernum

    def getOppinhandcheckernum(self):
        return self.__oppinhandcheckernum

    def put(self,p):
        self.__msg_send= "put %d,%d" % (p.getx(), p.gety())
        cell = self.__board.get_cell(p = p)
        cell.set_checker(Checker(cell, 'm'))
        return self.is_line(p)

    def pop(self,c):
        if c:
            cell = self.__board.get_cell(p=c.get_pos())
            cell.set_checker(None)
            self.__msg_send += " %d,%d" %(c.get_pos().getx(), c.get_pos().gety())

    def move(self, c, newpos):
        self.__msg_send = "mov %d,%d,%d,%d" % (c.get_pos().getx(), c.get_pos().gety(), newpos.getx(), newpos.gety())
        cell = self.__board.get_cell(p = c.get_pos())
        newcell = self.__board.get_cell(p = newpos)
        cell.set_checker(None)
        newcell.set_checker(Checker(newcell,'m'))
        return self.is_line(newpos)

    def is_line(self, p):
        board = self.get_board()
        cell = board.get_cell(p.getx(),p.gety())
        y = cell.get_pos().gety()
        x = cell.get_pos().getx()
        if board.get_cell(x, 0).get_checker() is not None and \
            board.get_cell(x, 1).get_checker() is not None and \
            board.get_cell(x, 2).get_checker() is not None and \
                board.get_cell(x, 0).get_checker().isMyChecker() == board.get_cell(x, 1).get_checker().isMyChecker() \
                and board.get_cell(x, 0).get_checker().isMyChecker() == board.get_cell(x, 2).get_checker().isMyChecker():
            return True

        if x % 2 == 0:

            if   board.get_cell((x) % 8, y).get_checker() is not None and\
                 board.get_cell((x - 1) % 8, y).get_checker() is not None and\
                 board.get_cell((x - 2) % 8, y).get_checker() is not None and\
                 board.get_cell((x - 1) % 8, y).get_checker().isMyChecker() == board.get_cell(x, y).get_checker().isMyChecker() and \
                 board.get_cell((x - 2) % 8, y).get_checker().isMyChecker() == board.get_cell(x, y).get_checker().isMyChecker():
                return True

            if   board.get_cell((x) % 8, y).get_checker() is not None and\
                 board.get_cell((x + 1) % 8, y).get_checker() is not None and\
                 board.get_cell((x + 2) % 8, y).get_checker() is not None and\
                 board.get_cell((x + 1) % 8, y).get_checker().isMyChecker() == board.get_cell(x, y).get_checker() and \
                 board.get_cell((x + 2) % 8, y).get_checker().isMyChecker() == board.get_cell(x, y).get_checker():
                return True
        else:
            if   board.get_cell((x) % 8, y).get_checker() is not None and\
                 board.get_cell((x - 1) % 8, y).get_checker() is not None and\
                 board.get_cell((x + 1) % 8, y).get_checker() is not None and\
                 board.get_cell((x - 1) % 8, y).get_checker().isMyChecker() == board.get_cell(x, y).get_checker().isMyChecker() and \
                 board.get_cell((x + 1) % 8, y).get_checker().isMyChecker() == board.get_cell(x, y).get_checker().isMyChecker():
                return True
        return False


    def get_cycle(self):
        return self.__cycle

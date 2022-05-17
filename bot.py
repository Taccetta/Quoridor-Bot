import numpy as np


class BotQuoridor():


    def __init__(self,data):
        #self.board = data['board']
        self.board = "NN      N     N                     N                                                                                                                                                                                                           S                                       S     S  "


    def split_char(self):
        self.board = [char for char in self.board]


    def board_logic(self):
        self.board = np.array(self.board).reshape(17,17)
        #print(self.board[0][0])

    def move_piece(self):




if __name__ == '__main__':

    data = None
    test = BotQuoridor(data)
    test.split_char()
    test.board_logic()
    print(test.board[0][1])
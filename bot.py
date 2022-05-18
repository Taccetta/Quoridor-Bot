from tkinter import N
import numpy as np
from itertools import product as iteration

class BotQuoridor():


    def __init__(self):
        self.board = None
        self.side = None
        self.opp_side = None
        self.from_row = 0
        self.from_col = 0
        self.to_row = 0
        self.to_col = 0
        self.my_pawn = [[0 for i in range(2)] for i in range(3)] #check
        self.opp_pawn = [[0 for i in range(2)] for i in range(3)]
        #self.my_pawn = [[0, 3],[0, 5],[0, 7]] if self.side == 'N' else [[9, 3],[9, 5],[9, 7]]
        #self.opp_pawn = [[9, 3],[9, 5],[9, 7]] if self.side == 'N' else [[0, 3],[0, 5],[0, 7]]


    def split_char(self):
        self.board = [char for char in self.board]


    def board_logic_table(self):
        self.board = np.array(self.board).reshape(17,17)


    def opponent_side_set(self):
        if self.side == 'N':
            self.opp_side = 'S'
        else:
            self.opp_side = 'N'


    def check_pawns_and_walls_position(self):
        my_pawn_number = 0
        opp_pawn_number = 0
        for row, col in iteration(range(0, 17, 2), range(0, 17, 2)):
            if self.board[row][col] == self.side:
                self.my_pawn[my_pawn_number] = [row//2, col//2]
                my_pawn_number += 1
                #print("N", self.my_pawn)
            elif self.board[row][col] == self.opp_side:
                self.opp_pawn[opp_pawn_number] = [row//2, col//2]
                opp_pawn_number += 1
                #print("S", self.opp_pawn)


    def move_foward(self):
        for row, col in iteration(range(0, 17, 2), range(0, 17, 2)):
            if self.board[row][col] == self.side:
                self.from_row = row // 2
                self.from_col = col // 2
                self.to_col = col // 2
                self.to_row = self.from_row + (2 if self.side == 'N' else -2) // 2
                print(self.from_row, self.from_col, self.to_row, self.to_col)
                #self.check_move()
                break


    def check_move(self):
        if self.board[self.to_row][self.to_col] != "":
            self.to_col = self.from_col + (- 2 // 2 if self.from_row != 0 else +2 // 2)
            self.to_row = self.from_row + (-2 if self.side == 'N' else 2) // 2

    def bot_play(self):
        self.split_char()
        self.board_logic_table()
        self.opponent_side_set()
        self.check_pawns_and_walls_position()
        print(self.board)
        self.move_foward()

if __name__ == '__main__':

    data = None
    test = BotQuoridor()
    test.board = "                                                                                     -*-                S                            -*-              N S                                                                                       N     N                                 S        "
    test.side = "N"
    test.split_char()
    test.board_logic_table()
    test.opponent_side_set()
    test.check_pawns_and_walls_position()
    print(test.board)
    print(test.board[0][0])
    test.move_foward()
from bot import BotQuoridor
import unittest
from parameterized import parameterized

class TestBot(unittest.TestCase):


    @parameterized.expand([(('                               -*-              '
                            '                 -*-         |                * '
                            '             |N|              *-*-             |'
                            '                 -*-              S             '
                            '                            S                   '
                            '                                                 '),
"""[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '-' '*' '-']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '-' '*' '-']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '|' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '*' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' '|' 'N' '|' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' '*' '-' '*' '-' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' '|' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '-' '*' '-' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'S' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'S']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]""")])

    def test_board_state_creator(self, boardstring, boardresult):
        testingbot = BotQuoridor()
        testingbot.board = boardstring
        testingbot.board_state_creator()
        self.assertEqual(len(testingbot.board), 17)
        self.assertEqual(str(testingbot.board), boardresult)


    @parameterized.expand([ ('N', 'S'),
                            ('S', 'N')])
    def test_opponent_side_set(self, side, oppside):
        testingbot = BotQuoridor()
        testingbot.side = side
        testingbot.opponent_side_set()
        self.assertNotEqual(side, oppside)
        self.assertEqual(testingbot.opp_side, oppside)


    @parameterized.expand([(('                                                '
                            '                                                '
                            '              N                                 '
                            '                                                '
                            '                                                '
                            '                                                 '),'N',[(6, 8)], []),

                            (('                                                '
                            '                                                '
                            '                                                '
                            '                                                '
                            '            N                                   '
                            '                                                 '),'N',[(12, 0)], []),

                            (('                                                  '
                            '                                                  '
                            '                                                  '
                            '                      S                           '
                            '                                                  '
                            '                                       '),'S',[(10, 2)], []),

                            (('                                                  '
                            '                                                  '
                            '                                                  '
                            '                 -*-                              '
                            '                                                  '
                            '                                       '),'S',[], [(9, 14), (9, 16)])
                        ])

    def test_check_pawns_and_walls_position(self, boardstring, side, pawn_coordinates, wall_coordinates):
        testingbot = BotQuoridor()
        testingbot.board = boardstring
        testingbot.side = side
        testingbot.board_state_creator()
        testingbot.check_pawns_and_walls_position()
        self.assertEqual(testingbot.my_pawn_coordinates, pawn_coordinates)
        self.assertEqual(testingbot.walls, wall_coordinates)


    @parameterized.expand([(None,[(6, 8)],'N',[],[],[((6, 8), (8, 8), 16), ((6, 8), (6, 6), 0), ((6, 8), (6, 10), 0)])])
    def test_pawn_call(self, boardstring, pawn_coordinates, side, wall_coordinates,opp_pawns, posible_moves):
        testingbot = BotQuoridor()
        testingbot.board = boardstring
        testingbot.side = side
        testingbot.my_pawn_coordinates = pawn_coordinates
        testingbot.walls = wall_coordinates
        testingbot.opp_pawns = opp_pawns
        testingbot.pawn_call()
        self.assertEqual(testingbot.possible_moves, posible_moves)


    @parameterized.expand([([((6, 8), (8, 8), 16), ((6, 8), (6, 6), 0), ((6, 8), (6, 10), 0)], 'N', ((6, 8), (8, 8)), 'pawn')])
    def test_decide_move_pawn(self, posible_moves, side, choice, im_going_to_move):
        testingbot = BotQuoridor()
        testingbot.possible_moves = posible_moves
        testingbot.side = side
        testingbot.decide_move()
        self.assertEqual(testingbot.final_choice, choice)
        self.assertEqual(testingbot.im_going_to_move, im_going_to_move)


if __name__ == '__main__':
    unittest.main()


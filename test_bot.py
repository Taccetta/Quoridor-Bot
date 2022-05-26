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
                            "[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '-' '*' '-']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '-' '*' '-']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '|' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '*' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' '|' 'N' '|' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' '*' '-' '*' '-' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' '|' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '-' '*' '-' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'S' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'S']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]"),
                            (('                                                 '
                            '                                                 '
                            '       |     |     |    *     *     *   N|    N| '
                            '   N| -*-   -*-   -*-                     -*-    '
                            '            S            -*- -*- -*-   -*-S      '
                            '       S            -*-                     '),
                            "[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' '|' ' ' ' ' ' ' ' ' ' ' '|' ' ' ' ' ' ' ' ' ' ' '|' ' ']\n "
                            "[' ' ' ' ' ' '*' ' ' ' ' ' ' ' ' ' ' '*' ' ' ' ' ' ' ' ' ' ' '*' ' ']\n "
                            "[' ' ' ' 'N' '|' ' ' ' ' ' ' ' ' 'N' '|' ' ' ' ' ' ' ' ' 'N' '|' ' ']\n "
                            "['-' '*' '-' ' ' ' ' ' ' '-' '*' '-' ' ' ' ' ' ' '-' '*' '-' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' '-' '*' '-' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' 'S' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']\n "
                            "['-' '*' '-' ' ' '-' '*' '-' ' ' '-' '*' '-' ' ' ' ' ' ' '-' '*' '-']\n "
                            "['S' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'S' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '-' '*' '-' ' ' ' ' ' ' ' ']\n "
                            "[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]")
                            ])

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
                            '                                       '),'S',[], [(9, 14), (9, 16)]),
                            (('                                                  '
                            '                                 |                '
                            '*               N|                                '
                            '                                                  '
                            '                                                  '
                            '                                       '),'N',[(6, 14)],[(4, 15), (6, 15)])
                        ])

    def test_check_pawns_and_walls_position(self, boardstring, side, pawn_coordinates, wall_coordinates):
        testingbot = BotQuoridor()
        testingbot.board = boardstring
        testingbot.side = side
        testingbot.board_state_creator()
        testingbot.check_pawns_and_walls_position()
        self.assertEqual(testingbot.my_pawn_coordinates, pawn_coordinates)
        self.assertEqual(testingbot.walls, wall_coordinates)


    @parameterized.expand([ (None,[(6, 8)],'N',[],[],[((6, 8), (8, 8), 16), ((6, 8), (6, 6), 0), ((6, 8), (6, 10), 0)]),
                            (None,[(0, 4)],'N',[],[],[((0, 4), (2, 4), 2), ((0, 4), (0, 2), 0), ((0, 4), (0, 6), 0)]),
                            (None,[(10, 10)],'N',[],[],[((10, 10), (12, 10), 64), ((10, 10), (10, 8), 0), ((10, 10), (10, 12), 0)]),
                            (None,[(12, 4)],'N',[],[],[((12, 4), (14, 4), 128), ((12, 4), (12, 2), 0), ((12, 4), (12, 6), 0)]),
                            (None,[(0, 0)],'N',[],[],[((0, 0), (2, 0), 2), ((0, 0), (0, 2), 0)]),
                            (None,[(10, 6)],'S',[],[],[((10, 6), (8, 6), 16), ((10, 6), (10, 4), 0), ((10, 6), (10, 8), 0)]),
                            (None,[(14, 14)],'S',[],[],[((14, 14), (12, 14), 4), ((14, 14), (14, 12), 0), ((14, 14), (14, 16), 0)]),
                            (None,[(6, 2)],'S',[],[],[((6, 2), (4, 2), 64), ((6, 2), (6, 0), 0), ((6, 2), (6, 4), 0)]),
                            (None,[(2, 2)],'S',[],[],[((2, 2), (0, 2), 1000), ((2, 2), (2, 0), 0), ((2, 2), (2, 4), 0)]),
                            (None,[(16, 2)],'S',[],[],[((16, 2), (14, 2), 2), ((16, 2), (16, 0), 0), ((16, 2), (16, 4), 0)])
                        ])
    def test_pawn_call(self, boardstring, pawn_coordinates, side, wall_coordinates,opp_pawns, posible_moves):
        testingbot = BotQuoridor()
        testingbot.board = boardstring
        testingbot.side = side
        testingbot.my_pawn_coordinates = pawn_coordinates
        testingbot.walls = wall_coordinates
        testingbot.opp_pawns = opp_pawns
        testingbot.pawn_call()
        self.assertEqual(testingbot.possible_moves, posible_moves)


    @parameterized.expand([([((6, 8), (8, 8), 16), ((6, 8), (6, 6), 0), ((6, 8), (6, 10), 0)], 'N', ((6, 8), (8, 8)), 'pawn'),
                            ([((16, 2), (14, 2), 2), ((16, 2), (16, 0), 0), ((16, 2), (16, 4), 0)], 'S', ((16, 2), (14, 2)), 'pawn'),
                            ([((2, 2), (0, 2), 1000), ((2, 2), (2, 0), 0), ((2, 2), (2, 4), 0)], 'S', ((2, 2), (0, 2)), 'pawn'),
                            ([((6, 2), (4, 2), 64), ((6, 2), (6, 0), 0), ((6, 2), (6, 4), 0)], 'S', ((6, 2), (4, 2)), 'pawn'),
                            ([((14, 14), (12, 14), 4), ((14, 14), (14, 12), 0), ((14, 14), (14, 16), 0)], 'S', ((14, 14), (12, 14)), 'pawn'),
                            ([((10, 6), (8, 6), 16), ((10, 6), (10, 4), 0), ((10, 6), (10, 8), 0)], 'N', ((10, 6), (8, 6)), 'pawn'),
                            ([((0, 0), (2, 0), 2), ((0, 0), (0, 2), 0)], 'S', ((0, 0), (2, 0)), 'pawn'),
                            ([((12, 4), (14, 4), 128), ((12, 4), (12, 2), 0), ((12, 4), (12, 6), 0)], 'N', ((12, 4), (14, 4)), 'pawn'),
                            ([((10, 10), (12, 10), 64), ((10, 10), (10, 8), 0), ((10, 10), (10, 12), 0)], 'N', ((10, 10), (12, 10)), 'pawn'),
                            ([((0, 4), (2, 4), 2), ((0, 4), (0, 2), 0), ((0, 4), (0, 6), 0)], 'N', ((0, 4), (2, 4)), 'pawn'),
                            ([((6, 8), (8, 8), 16), ((4, 8), (4, 6), 0), ((8, 8), (8, 10), 0)], 'S', ((6, 8), (8, 8)), 'pawn')
                        ])
    def test_decide_move_pawn(self, posible_moves, side, choice, im_going_to_move):
        testingbot = BotQuoridor()
        testingbot.possible_moves = posible_moves
        testingbot.side = side
        testingbot.decide_move()
        self.assertEqual(testingbot.final_choice, choice)
        self.assertEqual(testingbot.im_going_to_move, im_going_to_move)


if __name__ == '__main__':
    unittest.main()

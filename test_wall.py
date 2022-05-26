from wall import MyWall
import unittest
from parameterized import parameterized


class TestBot(unittest.TestCase):

    @parameterized.expand([ (('N',[(7,16)],[(2,4)],[(8,16), (6, 16)], [6, 14])),
                            (('N',[(9,7),(9,9)],[],[(8,8)], [8, 8])),
                            (('S',[(5,7),(3,3)],[],[(4,2)], [4, 2])),
                        ])
    def test_decide_pawn_to_walling(self, side, walls, allypawn, opp_pawns, result):
        testingwall = MyWall(side, walls, allypawn, opp_pawns)
        testingwall.decide_pawn_to_walling()
        self.assertEqual(result, testingwall.final_wall_choice)


if __name__ == '__main__':
    unittest.main()
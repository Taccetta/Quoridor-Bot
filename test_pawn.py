from cgi import test
from bot import BotQuoridor
from pawns import MyPawn
import unittest
from parameterized import parameterized


class TestBot(unittest.TestCase):


    @parameterized.expand([((7,4), (7,4))])
    def test_check_if_wall(self, coordinates, walls):
        testingpwan = MyPawn(8,4,'N',walls,[],[])
        t_or_f = testingpwan.check_if_wall(coordinates)
        self.assertTrue(coordinates, t_or_f)


    @parameterized.expand([ ((8,4), [(8,4)], [(8,4)], 'N'),
                            ((8,4), [(10,4)], [(8,4)], 'S')
                        ])
    def test_check_if_pawn(self, coordinates, allypawn, opp_pawns, side):
        testingpwan = MyPawn(8,4,side,[],allypawn,opp_pawns)
        team = testingpwan.check_if_pawn(coordinates)
        if side == 'N':
            self.assertEqual(side, team)
        else:
            self.assertNotEqual(side, team)


    @parameterized.expand([ (6,4,[(11,4)],[(2,4)],[(4,4)],'N', 
                            [((6, 4), (8, 4), 16),((6, 4), (6, 2), 0),
                            ((6, 4),(6, 6), 0),((6, 4), (8, 4), 16)])
                        ])
    def test_moving_forward_success(self, row, col, walls, allypawn, opp_pawns, side, result):
        testingpwan = MyPawn(row,col,side,walls,allypawn,opp_pawns)
        testingpwan.move_foward()
        self.assertEqual(testingpwan.my_movements, result)


    @parameterized.expand([ (6,4,[(7,4)],[(2,4)],[(4,4)],'N', ((6, 4), (8, 4), 16)),       #facing wall
                            (6,4,[],[(8,4)],[(4,4)],'N', ((6, 4), (8, 4), 16)),            #facing ally
                            (14,4,[(7,4)],[(2,4)],[(16,4)],'N', ((14, 4), (18, 4), 16))    #outside of board
                        ])
    def test_cant_moving_forward(self, row, col, walls, allypawn, opp_pawns, side, result):
        testingpwan = MyPawn(row,col,side,walls,allypawn,opp_pawns)
        testingpwan.move_foward()
        self.assertNotIn(result, testingpwan.my_movements)


    @parameterized.expand([ (6,4,[(3,4)],[(2,4)],[(8,4)],'N', ((6, 4), (10, 4), 48)),       #Facing Opp
                            (6,4,[(9,4)],[(2,4)],[(8,4)],'N', ((6, 4), (8, 2), 16))         #Facing Opp wall behind
                        ])
    def test_jumping_foward(self, row, col, walls, allypawn, opp_pawns, side, result):
        testingpwan = MyPawn(row,col,side,walls,allypawn,opp_pawns)
        testingpwan.jumping_foward()
        self.assertIn(result, testingpwan.my_movements)


    @parameterized.expand([ (6,4,[(7,4)],[(2,4)],[(4,4)],'N', ((6, 4), (6, 6), 0)),        #facing wall
                            (6,4,[],[(8,4)],[(4,4)],'N', ((6, 4), (6, 2), 0)),             #facing ally
                            (14,4,[(7,4)],[(2,4)],[(16,4)],'N', ((14, 4), (14, 2), 0))     #outside of board
                        ])
    def test_move_left(self, row, col, walls, allypawn, opp_pawns, side, result):
        testingpwan = MyPawn(row,col,side,walls,allypawn,opp_pawns)
        testingpwan.move_left()
        self.assertIn(result, testingpwan.my_movements)


if __name__ == '__main__':
    unittest.main()
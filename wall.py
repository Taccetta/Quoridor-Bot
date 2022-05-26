from random import randint


class MyWall():


    def __init__(self, team, walls, ally_pawns, opp_pawns):

        self.team = team
        self.walls = walls
        self.ally_pawns = ally_pawns
        self.opp_pawns = opp_pawns
        self.direction = -1 if self.team == 'N' else 1
        self.opponent_team = 'S' if self.team == 'N' else 'N'
        self.final_wall_choice = []
        self.decide_pawn_to_walling()


    def check_if_wall(self, coordinates):
        return coordinates in self.walls


    def decide_pawn_to_walling(self):
        opp_pawns_count = self.opp_pawns
        for pawn in opp_pawns_count:
            embedded_wall = self.check_if_wall((pawn[0] + self.direction, pawn[1]))
            if embedded_wall:
                self.opp_pawns.remove(pawn)
            else:
                embedded_wall_right= self.check_if_wall((pawn[0] + self.direction, pawn[1]+1))
                if embedded_wall_right:
                    self.opp_pawns.remove(pawn)

        if self.team == 'N':
            self.final_wall_choice.append(min(self.opp_pawns)[0])
        else:
            self.final_wall_choice.append(max(self.opp_pawns)[0])

        for pawn in self.opp_pawns:
            if self.final_wall_choice[0] == pawn[0]:
                self.final_wall_choice.append(pawn[1])
                break
        
        if len(self.final_wall_choice) > 2:
            for i in range(len(self.final_wall_choice)-2):
                self.final_wall_choice.pop()

        if len(self.final_wall_choice) == 0:
            self.final_wall_choice.append(randint(0, 16))
            self.final_wall_choice.append(randint(0, 16))

        if self.final_wall_choice[1] == 16:
            self.final_wall_choice[1] = 14
        
        if self.final_wall_choice[1] < 0:
            self.final_wall_choice[0]+= self.direction

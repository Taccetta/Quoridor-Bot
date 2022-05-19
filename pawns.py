

class MyPawn():


    def __init__(self, row, col, team, board, walls, ally_pawns, opp_pawns):
        self.board = board
        self.row = row
        self.col = col
        self.team = team
        self.walls = walls
        self.ally_pawns = ally_pawns
        self.opp_pawns = opp_pawns
        self.direction = 1 if self.team == 'N' else -1
        self.opponent_team = 'S' if self.team == 'N' else 'N'
        self.right_border = col == 16
        self.left_border = col == 0
        self.my_movements = []
        self.move_foward()
        self.move_left()
        self.move_right()


    def __repr__(self):
        return str(self.team)


    def check_if_wall(self, coordinates):
        return coordinates in self.walls


    def check_if_pawn(self, coordinates):
        if coordinates in self.ally_pawns:
            return self.team
        if coordinates in self.opp_pawns:
            return self.opponent_team
        return False


    def move_foward(self):
        landing_coordinates = (self.row + self.direction * 2, self.col)
        facing_wall = self.check_if_wall((self.row + self.direction, self.col))

        if facing_wall:
            return

        claimed_square = self.check_if_pawn(landing_coordinates)

        if not claimed_square:
            self.my_movements.append(((self.row, self.col),(landing_coordinates), 
                                        self.score(landing_coordinates[0])))

        if not self.opponent_team == claimed_square:
            return

        if self.row + self.direction*3 > 16 or self.row + self.direction*3 < 0:
            return

        jumping_wall = self.check_if_wall((self.row + self.direction*3, self.col))

        if not jumping_wall:
            jumping_coordinates = (self.row + self.direction * 4, self.col)
            claimed_jumping_square = self.check_if_pawn(jumping_coordinates)

            if not claimed_jumping_square:
                self.my_movements.append(((self.row, self.col),(jumping_coordinates), 
                                            self.score(jumping_coordinates[0])))

        if jumping_wall:
            jumping_coordinates_left_wall = (self.row + self.direction * 2, self.col-1)
            foward_left_wall = self.check_if_wall(jumping_coordinates_left_wall)

            if not foward_left_wall:
                jumping_coordinates_left_pawn = (self.row + self.direction * 2, self.col-2)
                claimed_forward_left_pawn = self.check_if_pawn(jumping_coordinates_left_pawn)
                
                if not claimed_forward_left_pawn:
                    self.my_movements.append(((self.row, self.col),(jumping_coordinates_left_pawn), 
                                            self.score(jumping_coordinates_left_pawn[0])))

            jumping_coordinates_right_wall = (self.row + self.direction * 2, self.col+1)
            foward_right_wall = self.check_if_wall(jumping_coordinates_right_wall)

            if not foward_right_wall:
                jumping_coordinates_right_pawn = (self.row + self.direction * 2, self.col+2)
                claimed_forward_right_pawn = self.check_if_pawn(jumping_coordinates_right_pawn)

                if not claimed_forward_right_pawn:
                    self.my_movements.append(((self.row, self.col),(jumping_coordinates_right_pawn), 
                                            self.score(jumping_coordinates_right_pawn[0])))


    def move_left(self):
        score = 0
        landing_coordinates = (self.row, self.col-2)
        facing_left_wall = self.check_if_wall((self.row, self.col-1))

        if facing_left_wall or self.left_border:
            return

        claimed_square = self.check_if_pawn(landing_coordinates)
    
        if not claimed_square:
            jumping_coordinates_wall = (self.row + 1*self.direction, self.col - 2)
            wall_in_front = self.check_if_wall(jumping_coordinates_wall)
            if wall_in_front:
                score -= 1
            self.my_movements.append(((self.row, self.col),(landing_coordinates), 
                                        score))
        
        if not self.opponent_team == claimed_square:
            return

        if self.col - 4 > 16 or self.col - 4 < 0:
            return
        jumping_wall = self.check_if_wall((self.row, self.col - 3))

        if not jumping_wall:
            jumping_coordinates = (self.row, self.col - 4)
            claimed_jumping_square = self.check_if_pawn(jumping_coordinates)

            if not claimed_jumping_square:
                    self.my_movements.append(((self.row, self.col),(jumping_coordinates), 
                                                score))
        
        if jumping_wall:
            jumping_coordinates_left_wall = (self.row + self.direction * 2, self.col-1)
            foward_left_wall = self.check_if_wall(jumping_coordinates_left_wall)
            
            if not foward_left_wall:
                jumping_coordinates_left_pawn = (self.row + self.direction * 2, self.col-2)
                claimed_forward_left_pawn = self.check_if_pawn(jumping_coordinates_left_pawn)
                
                if not claimed_forward_left_pawn:
                    self.my_movements.append(((self.row, self.col),(jumping_coordinates_left_pawn), 
                                            score))
    
    def move_right(self):
        score = 0
        landing_coordinates = (self.row, self.col+2)
        facing_right_wall = self.check_if_wall((self.row, self.col+1))

        if facing_right_wall or self.right_border:
            return

        claimed_square = self.check_if_pawn(landing_coordinates)
    
        if not claimed_square:
            jumping_coordinates_wall = (self.row + 1 * self.direction, self.col + 2)
            wall_in_front = self.check_if_wall(jumping_coordinates_wall)
            if wall_in_front:
                score -= 1
            self.my_movements.append(((self.row, self.col),(landing_coordinates), 
                                        score))
        
        if not self.opponent_team == claimed_square:
            return
        
        if self.col + 4 > 16 or self.col + 4 < 0:
            return
        
        jumping_wall = self.check_if_wall((self.row, self.col + 3))

        if not jumping_wall:
            jumping_coordinates = (self.row, self.col + 4)
            claimed_jumping_square = self.check_if_pawn(jumping_coordinates)

            if not claimed_jumping_square:
                    self.my_movements.append(((self.row, self.col),(jumping_coordinates), 
                                                score))
        
        if jumping_wall:
            jumping_coordinates_left_wall = (self.row + self.direction * 2, self.col+1)
            foward_left_wall = self.check_if_wall(jumping_coordinates_left_wall)
            
            if not foward_left_wall:
                jumping_coordinates_left_pawn = (self.row + self.direction * 2, self.col+2)
                claimed_forward_left_pawn = self.check_if_pawn(jumping_coordinates_left_pawn)
                
                if not claimed_forward_left_pawn:
                    self.my_movements.append(((self.row, self.col),(jumping_coordinates_left_pawn), 
                                            score))

    def score(self, row):
            value = 0
            exponent = 0
            if self.team == 'S':
                exponent = 8-row//2
            else:
                exponent = row//2
            if exponent == 8:
                value = 1000
            else:
                value = 2**exponent
            if abs(self.row - row) == 4:
                value += 2**(exponent-1)
            return value
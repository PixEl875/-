class P1:
    def __init__(self,x,y,points=0):
        self.x=x
        self.y=y
        self.points=points
    def status(self):
        return f'P1: x {self.x},y {self.y},points {self.points}'
class P2:
    def __init__(self,x,y,points=0):
        self.x=x
        self.y=y
        self.points=points
    def status(self):
        return f'P2: x {self.x},y {self.y},points {self.points}'
class Ball:
    def __init__(self,ball_positionx,ball_positiony,direction,speed):
        self.ball_positionx=ball_positionx
        self.ball_positiony=ball_positiony
        self.direction=direction
        self.speed=speed
    def status(self):
        return f'Ball: x {self.ball_positionx},y {self.ball_positiony},speed {self.speed}, direction {self.direction}'
class Mesh:
    def __init__(self,placex,placey):
        self.placex=placex
        self.placey=placey
    def status(self):
        return f'Mesh: x {self.placex},y {self.placey}'
def show_game_world(world):
    for unit in world:
        print(unit.status())
   
player1=P1(10,20)       
player2=P2(50,20)
ball=Ball(40,0,45,5)
mesh=Mesh(40,20)
world=[player1,player2,ball,mesh]
show_game_world(world)   


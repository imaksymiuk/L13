#4.(Optional) Create a Robot class with the following attributes: orientation 
#(left, right, up, down), position_x, position_y. The Robot class should have 
#the following methods: move, turn, and display_position. The move method 
#should take a number of steps and move the robot in the direction it is 
#currently facing. The turn method should take a direction (left or right) 
#and turn the robot in that direction. The display_position method should 
#print the current position of the robot.

class Robot:
    def __init__(self, orientation, position_x, position_y):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        if self.orientation == 'left':
            self.position_x -= steps
        if self.orientation == 'right':
            self.position_x += steps
        if self.orientation == 'up':
            self.position_y += steps
        if self.orientation == 'down':
            self.position_y -= steps

    def turn(self, direction):
        next_orientation = {
            'up' : {'left': 'left', 'right': 'right'},
            'right' : {'left': 'up','right': 'down'},
            'down' : {'left': 'right', 'right': 'left'},
            'left' : {'left': 'down', 'right': 'up'}
        }
        self.orientation = next_orientation[self.orientation][direction]

    def display_position(self):
        print (f'Current position: x={self.position_x}, y={self.position_y}; facing -{self.orientation}')


robot = Robot('up', 0, 0)
robot.move(5)
robot.display_position()
robot.turn('right')
robot.move(3)
robot.display_position()
robot.turn('right')
robot.move(2)
robot.display_position()

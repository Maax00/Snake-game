from turtle import Turtle

Starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
right = 0
left = 180


class Snake(Turtle):
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def move(self):
        for part in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[part-1].xcor()
            new_y = self.snake_body[part-1].ycor()
            self.snake_body[part].goto(new_x, new_y)
        self.head.forward(move_distance)

    def create_snake(self):
        for position in Starting_position:
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            self.snake_body.append(tim)

    def new_snake(self):
        for position in self.snake_body:
            position.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def add_body(self):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        position = self.snake_body[-1].position()
        tim.goto(position)
        self.snake_body.append(tim)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

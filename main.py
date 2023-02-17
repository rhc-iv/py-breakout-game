# Import Statements:
from turtle import Screen, Turtle
import time
from obstacles import Blocks

# Create the game window:
screen = Screen()
screen.bgcolor('#3E4451')
screen.setup(width=800, height=600)
screen.title('CLASSIC BREAKOUT!')
screen.tracer(0)

# Create the player's paddle:
paddle = Turtle()
paddle.color('#C678DD')
paddle.penup()
paddle.goto(0, -240)
paddle.shape('square')
paddle.shapesize(stretch_wid=1, stretch_len=10)

# Create the game ball:
ball = Turtle()
ball.color('#B6BDCA')
ball.penup()
ball.goto(0, 0)
ball.shape('circle')

x_move = 1
y_move = 1

# Create a score display on-screen:
points = 0

score = Turtle()
score.color('#D19A66')
score.penup()
score.goto(0, 250)
score.hideturtle()
score.shape('square')
score.speed(0)
score.write(
    f'Score: {points}',
    align='center',
    font=(
        'SF Pro Display',
        24,
        'bold',
    )
)

# Create a list of block colors:
colors = ['#61AFEF', '#98C379', '#BE5046', '#E5C07B']
block_list = []
x_pos = -335
y_pos = 50

# Add the blocks to the game screen:
for color in colors:
    for num in range(0, 7):
        block = Blocks(
            color=color,
            position=(
                x_pos,
                y_pos,
            )
        )
        block_list.append(block)
        x_pos += 110
    y_pos += 50
    x_pos = -335


# Create paddle movement functions:
def move_left():
    new_x = paddle.xcor() - 20
    paddle.goto(new_x, paddle.ycor())


def move_right():
    new_x = paddle.xcor() + 20
    paddle.goto(new_x, paddle.ycor())


# Create a function that moves the ball on-screen:
def move_ball():
    new_x = ball.xcor() + x_move
    new_y = ball.ycor() - y_move
    ball.goto(new_x, new_y)


# Create a function to detect ball/wall collisions:
def bounce_wall():
    global x_move
    x_move *= -1


# Create a function to detect ball/paddle collisions:
def bounce_paddle():
    global y_move
    y_move *= -1


# Create a function to update the on-screen score display:
def increase_score():
    global points, x_move, y_move
    points += 1
    score.clear()
    score.write(
        f'Score: {points}',
        align='center',
        font=(
            'SF Pro Display',
            24,
            'bold',
        )
    )
    if points > 10:
        x_move = 1.4
        y_move = 1.4
    if points > 20:
        x_move = 1.8
        y_move = 1.8



# Set event listeners for player keypresses:
screen.listen()
screen.onkey(move_left, 'Left')
screen.onkey(move_right, 'Right')

# Set starting game condition:
game_is_on = True

# Main game loop:
while game_is_on:
    time.sleep(0.005)
    move_ball()
    screen.update()

    # Detect ball/wall(sides) collisions:
    if ball.xcor() > 380 or ball.xcor() < -390:
        bounce_wall()

    # Detect ball/paddle collisions:
    if ball.distance(paddle) < 100 and ball.ycor() < -220 or ball.ycor() > 290:
        bounce_paddle()

    # Show blocks on-screen and detect ball/block collisions:
    for block in block_list:
        if block.distance(ball) < 60 and ball.ycor() > 20:
            bounce_paddle()
            increase_score()
            block.hideturtle()
            x_axis_difference = ball.distance(block)
            y_axis_difference = ball.distance(block)

            block_list.remove(block)

    # Detect ball/wall(bottom) collisions for loss condition:
    if ball.ycor() < - 270 or not block_list:
        game_is_on = False

screen.exitonclick()
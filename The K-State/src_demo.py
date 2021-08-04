# ---------------------------------------------------------------------------
# --
# @ Author: Marcello Belanda
# @ Date:   20/03
# @ Name: The K-State
# --
# ---------------------------------------------------------------------------


import turtle
from random import randint
import math

# window config
w = turtle.Screen()
w.bgcolor('black')
w.title('The K-State')

# border
border = turtle.Turtle()
border.color('white')
border.pensize(3)
border.shape('blank')
border.speed(10)
border.penup()
border.setpos(-250, 150)
border.pendown()
for side in range(4):
    border.fd(300)
    border.right(90)
border.hideturtle()

# title border
titleb = turtle.Turtle()
titleb.color('gray')
titleb.shape('blank')
titleb.speed(10)
titleb.pensize(3)
titleb.penup()
titleb.setpos(-55, 250)
titleb.pendown()
titleb.fd(120)
titleb.left(90)
titleb.fd(25)
titleb.left(90)
titleb.fd(120)
titleb.left(90)
titleb.fd(25)
titleb.hideturtle()

# title
title = turtle.Turtle()
title.color('white')
title.shape('blank')
title.speed(0)
title.penup()
title.setpos(-50, 250)
title.pendown()
title.write('The K-State', font=('Terminal', 20, 'normal'))
title.hideturtle()

# lbl 1 border
lbl1b = turtle.Turtle()
lbl1b.color('blue')
lbl1b.shape('blank')
lbl1b.speed(10)
lbl1b.pensize(3)
lbl1b.penup()
lbl1b.setpos(-250, 158)
lbl1b.pendown()
lbl1b.fd(55)
lbl1b.left(90)
lbl1b.fd(28)
lbl1b.left(90)
lbl1b.fd(55)
lbl1b.left(90)
lbl1b.fd(28)
lbl1b.hideturtle()

# lbl 1
lbl1 = turtle.Turtle()
lbl1.color('white')
lbl1.shape('blank')
lbl1.speed(0)
lbl1.penup()
lbl1.setpos(-250, 160)
lbl1.pendown()
lbl1.write('Ready',font=('Terminal', 20, 'normal'))
lbl1.hideturtle()


# credits border
credtb = turtle.Turtle()
credtb.color('gray')
credtb.shape('blank')
credtb.speed(10)
credtb.pensize(3)
credtb.penup()
credtb.setpos(-255, -250)
credtb.pendown()
credtb.fd(300)
credtb.left(90)
credtb.fd(50)
credtb.left(90)
credtb.fd(300)
credtb.left(90)
credtb.fd(50)
credtb.hideturtle()

# credits
credits_ = turtle.Turtle()
credits_.color('white')
credits_.shape('blank')
credits_.speed(0)
credits_.penup()
credits_.setpos(-250, -228)
credits_.pendown()
credits_.write('[AUTHOR] - MARCELLO BELANDA',font=('Terminal', 20, 'normal'))
credits_.hideturtle()

# credits 2
credits_2 = turtle.Turtle()
credits_2.color('white')
credits_2.shape('blank')
credits_2.speed(0)
credits_2.penup()
credits_2.setpos(-250, -250)
credits_2.pendown()
credits_2.write('[DATE]   - 20/03',font=('Terminal', 20, 'normal'))
credits_2.hideturtle()

# tutorial
tuttext = 'TUTORIAL\n\n[SPACE] - SHOOT\n[LEFT ARROW] - MOVE LEFT\n[RIGHT ARROW] - MOVE RIGHT\n\n[ESC] - EXIT'
tut = turtle.Turtle()
tut.color('gray')
tut.shape('blank')
tut.speed(0)
tut.penup()
tut.setpos(70, -15)
tut.pendown()
tut.write(tuttext, font=('Terminal', 20, 'normal'))
tut.hideturtle()

# score border
scoreb = turtle.Turtle()
scoreb.color('blue')
scoreb.shape('blank')
scoreb.speed(10)
scoreb.pensize(3)
scoreb.penup()
scoreb.setpos(-105, 155)
scoreb.pendown()
scoreb.fd(100)
scoreb.left(90)
scoreb.fd(25)
scoreb.left(90)
scoreb.fd(100)
scoreb.left(90)
scoreb.fd(25)
scoreb.hideturtle()

# score
score = 0

scoretext = 'Score - %s' %score
score_ = turtle.Turtle()
score_.color('white')
score_.shape('blank')
score_.speed(0)
score_.penup()
score_.setpos(-100, 160)
score_.pendown()
score_.write(scoretext, font=('Terminal', 20, 'normal'))
score_.hideturtle()

# lbl2
lbl2 = turtle.Turtle()
lbl2.color('white')
lbl2.shape('blank')
lbl2.speed(0)
lbl2.penup()
lbl2.setpos(-400, 110)
lbl2.pendown()
lbl2.write('[BLUE] - You\n[RED] - Enemies', font=('Terminal',20,'normal'))
lbl2.hideturtle()

# player
playerspeed = 15
player = turtle.Turtle()
player.color('blue')
player.shape('square')
player.speed(0)
player.penup()
player.setpos(-200, -120) #starts: (-200, -120) ; ends: (0, -120)
player.setheading(90)

# bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('square')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.3, 0.3)
bullet.hideturtle()


# game over border
game_overb = turtle.Turtle()
game_overb.color('gray')
game_overb.shape('blank')
game_overb.speed(10)
game_overb.pensize(3)
game_overb.penup()
game_overb.setpos(100, -105)
game_overb.pendown()

# game over lbl
game_over = turtle.Turtle()
game_over.color('white')
game_over.shape('blank')
game_over.speed(0)
game_over.penup()
game_over.setpos(100, -100)
game_over.pendown()

# enemies
enemiespeed = 2
    
enemie = turtle.Turtle()
enemie.color('red')
enemie.shape('square')
enemie.speed(0)
enemie.penup()

x = randint(-200, 0)
y = randint(0, 130)
    
enemie.setpos(x, y) #starts: (0, 130) ; ends: (-200, 130)
enemie.pendown()

bulletspeed = 20
bulletstate = 'ready'

def exit_game():
    w.bye()

def move_right():
    x = player.xcor()
    x += playerspeed 
    if x > 40:
        x = 40
    player.setx(x)

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -240:
        x = -240
    player.setx(x)

def firebullet():
    global bulletstate

    if bulletstate == 'ready':
        bulletstate == 'fire'
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setpos(x, y)
        bullet.showturtle()

def iscollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 15:
        return True
    return False

# key bindings
turtle.listen()
turtle.onkeypress(exit_game, 'Escape')
turtle.onkeypress(move_right, 'Right')
turtle.onkeypress(move_left, 'Left')
turtle.onkeypress(firebullet, 'space')

'''
if score == 0:
    # draw lbl
    game_over.write('GAME OVER', font=('Terminal', 20, 'normal'))
    game_over.hideturtle()

    # draw border
    game_overb.fd(95)
    game_overb.left(90)
    game_overb.fd(30)
    game_overb.left(90)
    game_overb.fd(95)
    game_overb.left(90)
    game_overb.fd(30)
    game_overb.hideturtle()
'''

# main loop
while True:
    
        #move enemy
        x = enemie.xcor()
        x += enemiespeed
        enemie.setx(x)

        if enemie.xcor() < 120:#>
           
                y = enemie.ycor()
                y -= 40
                enemie.sety(y)
                
                enemiespeed *= -1

        if enemie.xcor() < -190:
            
                y = enemie.ycor()
                y -= 40
                enemie.sety(y)

                enemiespeed *= -1
            
        if bulletstate == 'fire':
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        if bullet.ycor() > 140:
            bullet.hideturtle()
            bulletstate = 'ready'

        if iscollision(bullet, enemie):
            bullet.hideturtle()
            bulletstate = 'ready'
            bullet.setpos(0, -400)
            
            score += 10
            scoretext = "Score: {}".format(score)
            score_.clear()
            score_.write(scoretext, font=('Terminal',20, 'normal'))

            x = randint(-200, 0)
            y = randint(0, 130)
            
            enemie.setpos(x, y) #starts: (0, 130) ; ends: (-200, 130)

        if iscollision(player, enemie):
            player.hideturtle()
            enemie.hideturtle()
            # draw lbl
            game_over.write('GAME OVER', font=('Terminal', 20, 'normal'))
            game_over.hideturtle()

            # draw border
            game_overb.fd(95)
            game_overb.left(90)
            game_overb.fd(30)
            game_overb.left(90)
            game_overb.fd(95)
            game_overb.left(90)
            game_overb.fd(30)
            game_overb.hideturtle()
            break
   
if bulletstate == 'fire':
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

if bullet.ycor() > 140:
    bullet.hideturtle()
    bulletstate = 'ready'

input('>')
                
            
        



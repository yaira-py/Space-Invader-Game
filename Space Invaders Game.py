import turtle

win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders Game")
win.tracer(0)  

# Player
player = turtle.Turtle()
player.shape("triangle")
player.color("green")
player.penup()
player.sety(-250)
player.setheading(90)


enemy = turtle.Turtle()
enemy.shape("circle")
enemy.color("orange")
enemy.penup()
enemy.sety(200)


bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("white")
bullet.penup()
bullet.hideturtle()
bullet.setheading(90)
bullet.sety(-240)

bullet_state = "ready"

def left():
    x = player.xcor() - 20
    if x > -280:
        player.setx(x)

def right():
    x = player.xcor() + 20
    if x < 280:
        player.setx(x)

def fire():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.showturtle()
        bullet.setx(player.xcor())
        bullet.sety(-240)
        print("FIRE!")  

win.listen()
win.onkey(left, "Left")
win.onkey(right, "Right")
win.onkey(fire, "space")

def game_loop():
    global bullet_state
    
    enemy.setx(enemy.xcor() + 2)
    if enemy.xcor() > 280 or enemy.xcor() < -280:
        enemy.sety(enemy.ycor() - 20)
        enemy.setx(-enemy.xcor())

    
    if bullet_state == "fire":
        bullet.sety(bullet.ycor() + 15)
        if bullet.ycor() > 280:
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.sety(-240)
        # Hit check
        if abs(bullet.xcor() - enemy.xcor()) < 20 and abs(bullet.ycor() - enemy.ycor()) < 20:
            print("HIT!")
            enemy.setx(-200)
            enemy.sety(200)
            bullet.hideturtle()
            bullet_state = "ready"

    win.update()
    win.ontimer(game_loop, 20)  

game_loop()
win.mainloop()

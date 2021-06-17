import os
import pickle
import random
import time
import turtle

if __name__ == "__main__":

    os.getcwd()

    try:
        highScore = pickle.load(open("highscore.txt", "rb"))
    except (OSError, IOError) as e:
        highScore = 0


    delay = 0.1
    score = 0

    # Set up the screen
    window = turtle.Screen()
    window.title("Snake Game by Kostas Poime")
    window.bgcolor("purple")
    window.setup(width=1000, height=700)
    window.tracer(0)
    image = "python.gif"
    if os.path.isfile(image):
        window.addshape(image)



    # Snake head
    head = turtle.Turtle()
    if os.path.isfile(image):
        head.shape(image)
    else:
        head.shape("square")
        head.color("white")
    head.speed(0)
    head.penup()
    head.goto(0,0)
    head.direction = "stop"

    #Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)

    # Snake food
    extraFood = turtle.Turtle()
    extraFood.speed(0)
    extraFood.shape("triangle")
    extraFood.color("green")
    extraFood.penup()
    extraFood.goto(0, 100)

    bodies = []

    def changeLetters(score,highScore):
        letters.clear()
        letters.write("Score: {} High Score: {}".format(score, highScore), align="center",
                      font=("Courier", 24, "normal"))

    # Letters
    letters = turtle.Turtle()
    letters.speed(0)
    letters.hideturtle()
    letters.color("white")
    letters.goto(0,260)
    changeLetters(score,highScore)

    def changeLetters(score,highScore):
        letters.clear()
        letters.write("Score: {} High Score: {}".format(score, highScore), align="center",
                      font=("Courier", 24, "normal"))


    def endGame():
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for b in bodies:
            b.goto(2000, 2000)

        bodies.clear()

        score = 0
        changeLetters(score,highScore)

        #save highScore into a file
        pickle.dump(highScore, open("highscore.txt", "wb"))

        return score


    # Functions
    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"


    # Keyboard Bindings
    window.listen()
    window.onkeypress(go_up, 'Up')
    window.onkeypress(go_down, 'Down')
    window.onkeypress(go_left, 'Left')
    window.onkeypress(go_right, 'Right')


    # Main game loop
    while True:
        window.update()

        #check the walls of our border
        if head.xcor()>490 or head.xcor()<-490 or head.ycor()>340 or head.ycor()<-340:
            score = endGame()
            delay = 0.1

        # Check if snake bites its body
        for b in bodies:
            if b.distance(head) < 20:
                score = endGame()
                delay = 0.1


        #snake touches food
        if head.distance(food) < 20:
            #Move the food randomly
            x = random.randint(-430,430)
            y = random.randint(-330, 330)
            food.goto(x,y)

            # Add body
            new_body = turtle.Turtle()
            new_body.speed(0)
            new_body.shape("square")
            new_body.color("yellow")
            new_body.penup()
            bodies.append(new_body)

            score = score + 10
            if score>highScore:
                highScore = score

            changeLetters(score,highScore)

            if delay>=0.03:
                delay -=0.002

        # snake touches extra food
        if head.distance(extraFood) < 20:

            # Add 3 bodies
            new_body = turtle.Turtle()
            new_body.speed(0)
            new_body.shape("square")
            new_body.color("yellow")
            new_body.penup()
            bodies.append(new_body)
            bodies.append(new_body)
            bodies.append(new_body)

            score = score + 30
            if score > highScore:
                highScore = score

            changeLetters(score, highScore)

            # Move the food randomly
            extraFood.goto((2000, 2000))
            x = random.randint(-430, 430)
            y = random.randint(-330, 330)
            extraFood.goto(x,y)

            if delay >= 0.03:
                delay -= 0.006


        for i in range(len(bodies)-1, 0 , -1):
            x = bodies[i-1].xcor()
            y = bodies[i-1].ycor()
            bodies[i].goto(x,y)

        if len(bodies)>0:
            x = head.xcor()
            y = head.ycor()
            bodies[0].goto(x,y)

        move()
        time.sleep(delay)

    window.mainloop()

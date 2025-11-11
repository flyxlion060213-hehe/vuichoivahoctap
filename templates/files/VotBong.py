import tkinter
from tkinter import messagebox
import time
canvasWidth = 750
canvasHeight = 500
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
canvas.pack()
bat = canvas.create_rectangle(0, 0, 40, 10, fill="dark turquoise")
ball = canvas.create_oval(20, 0, 30, 10, fill="deep pink")
windowOpen = True
score = 0
bounceCount = 0
leftPressed = 0
rightPressed = 0
batSpeed = 6
ballMoveX = 4
ballMoveY = -4
setBatTop = canvasHeight - 40
setBatBottom = canvasHeight - 30
def move_bat():
    batMove = batSpeed * rightPressed - batSpeed * leftPressed
    batLeft, batTop, batRight, batBottom = canvas.coords(bat)
    if (batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
        canvas.move(bat, batMove, 0)
def move_ball():
    global ballMoveX, ballMoveY, score, bounceCount, batSpeed
    ballLeft, ballTop, ballRight, ballBottom = canvas.coords(ball)
    if ballRight + ballMoveX > canvasWidth or ballLeft + ballMoveX < 0:
        ballMoveX = -ballMoveX
    if ballTop + ballMoveY < 0:
        ballMoveY = -ballMoveY
    if ballMoveY > 0 and ballBottom + ballMoveY >= setBatTop:
        batLeft, batTop, batRight, batBottom = canvas.coords(bat)
        if ballRight >= batLeft and ballLeft <= batRight:
            ballMoveY = -ballMoveY
            score += 1
            bounceCount += 1
            if bounceCount == 4:
                bounceCount = 0
                batSpeed += 1
                ballMoveX += 1 if ballMoveX > 0 else -1
    canvas.move(ball, ballMoveX, ballMoveY)
def check_game_over():
    ballLeft, ballTop, ballRight, ballBottom = canvas.coords(ball)
    if ballTop > canvasHeight:
        print("Điểm của bạn là " + str(score))
        playAgain = messagebox.askyesno(message="Bạn có muốn chơi lại không?")
        if playAgain:
            reset()
        else:
            close()
def close():
    global windowOpen
    windowOpen = False
    window.destroy()
def reset():
    global score, bounceCount, batSpeed, leftPressed, rightPressed, ballMoveX, ballMoveY
    leftPressed = 0
    rightPressed = 0
    ballMoveX = 4
    ballMoveY = -4
    canvas.coords(bat, 10, setBatTop, 50, setBatBottom)
    canvas.coords(ball, 20, setBatTop-10, 30, setBatTop)
    score = 0
    bounceCount = 0
    batSpeed = 6
def on_key_press(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 1
    elif event.keysym == "Right":
        rightPressed = 1
def on_key_release(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 0
    elif event.keysym == "Right":
        rightPressed = 0
def main_loop():
    while windowOpen:
        move_bat()
        move_ball()
        window.update()
        time.sleep(0.02)
        check_game_over()
window.protocol("WM_DELETE_WINDOW", close)
window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)

reset()
main_loop()

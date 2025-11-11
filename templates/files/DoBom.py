import tkinter
import random
gameOver = False
score = 0
squaresToClear = 0
bombfield = []
def create_bombfield():
    global squaresToClear, bombfield
    bombfield = []
    squaresToClear = 0
    for row in range(10):
        rowList = []
        for column in range(10):
            if random.randint(1, 100) < 20:
                rowList.append(1)  
            else:
                rowList.append(0)
                squaresToClear += 1
        bombfield.append(rowList)
def bomb_color(num):
    if num == 1:
        return "blue"
    elif num == 2:
        return "green"
    elif num == 3:
        return "orange"
    elif num == 4:
        return "purple"
    elif num >= 5:
        return "red"
    else:
        return "black"
def layout_window(window):
    for rowNumber, rowList in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(rowList):
            if random.randint(1, 100) < 25:
                square = tkinter.Label(window, text="    ", bg="darkgreen", width=4, height=2, borderwidth=2, relief="raised")
            elif random.randint(1, 100) > 75:
                square = tkinter.Label(window, text="    ", bg="seagreen", width=4, height=2, borderwidth=2, relief="raised")
            else:
                square = tkinter.Label(window, text="    ", bg="green", width=4, height=2, borderwidth=2, relief="raised")
            square.grid(row=rowNumber, column=columnNumber)
            square.bind("<Button-1>", on_click)
def on_click(event):
    global score, gameOver, squaresToClear
    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currentText = square.cget("text")
    if gameOver or currentText.strip() != "":
        return
    totalBombs = 0
    if bombfield[row][column] == 1:
        gameOver = True
        square.config(bg="red")
        print("Game over! Bạn đã giẫm phải bom.")
        print("Your score was:", score)
        return
    else:
        square.config(bg="lightgrey")
        for r in range(max(0, row-1), min(10, row+2)):
            for c in range(max(0, column-1), min(10, column+2)):
                if bombfield[r][c] == 1:
                    totalBombs += 1
        square.config(text=" " + str(totalBombs) + " ", fg=bomb_color(totalBombs))
        squaresToClear -= 1
        score += 1
        if squaresToClear == 0:
            gameOver = True
            print("Chúc mừng! Bạn đã tìm thấy các ô an toàn!")
            print("Số điểm của bạn là:", score)
def play_bombdodger():
    create_bombfield()
    window = tkinter.Tk()
    window.title("Bomb Dodger")
    layout_window(window)
    window.mainloop()
play_bombdodger()

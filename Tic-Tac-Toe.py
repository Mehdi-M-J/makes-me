# from cgitb import text
# from tkinter import font
# from unittest import result
import tkinter as tk
from tkinter.messagebox import showinfo

Window = tk.Tk()
Window.title("Tic-Tac-To GAME")

global turn, results, Player_points
turn = "P1"
results = ["", "", "", "", "", "", "", "", ""]
Player_points = [0, 0]

def clicked(btn):
    global turn
    btn = int(btn)

    if results[btn] == "":
        if turn == "P1":
            results[btn] = "P1"
            buttons[btn]["bg"] = "red"
            buttons[btn]["fg"] = "yellow"
            buttons[btn]["text"] = "P1"
            buttons[btn]["relief"] = tk.GROOVE
            turn = "P2"  # تغییر نوبت به P2
        else:
            results[btn] = "P2"
            buttons[btn]["bg"] = "blue"
            buttons[btn]["fg"] = "yellow"
            buttons[btn]["text"] = "P2"
            turn = "P1"  # تغییر نوبت به P1
    rule()


def rule():
    if (results[0]==results[1]==results[2] and results[0] != ""):
        show_winner(results[0])
    elif (results[3]==results[4]==results[5] and results[3] != ""):
        show_winner(results[3])
    elif (results[6]==results[7]==results[8] and results[6] != ""):
        show_winner(results[6])
    elif (results[0]==results[3]==results[6] and results[0] != ""):
        show_winner(results[0])
    elif (results[1]==results[4]==results[7] and results[1] != ""):
        show_winner(results[1])
    elif (results[2]==results[5]==results[8] and results[2] != ""):
        show_winner(results[2])
    elif (results[0]==results[4]==results[8] and results[0] != ""):
        show_winner(results[0])
    elif (results[2]==results[4]==results[6] and results[2] != ""):
        show_winner(results[2])
    else:
        check_draw()

def show_winner(winner):
    if winner == "P1":
        Player_points[0] += 1
        showinfo("Game ended", "PLAYER-1 Winner!")
    else:
        Player_points[1] += 1
        showinfo("Game ended", "PLAYER-2 Winner!")
    rest()

def rest():
    global results, turn
    results = ["", "", "", "", "", "", "", "", ""]
    turn = "P1"  # تغییر نوبت به P1
    points()
    Board()

def check_draw():
    if "" not in results:
        showinfo("Game ended", "DRAW!")
        rest()

def points():
    global Player_points

    Board_frame = tk.Frame(Window)
    Board_frame.grid(row=0)
    label_player_one = tk.Label(Board_frame, text="بازیکن 1", font=("Mj_Modern_1",16), padx=10)
    label_player_two = tk.Label(Board_frame, text="بازیکن 2", font=("Mj_Modern_1",16), padx=10)
    label_player_one.grid(row=0, column=0)
    label_player_two.grid(row=0, column=2)

    point_frame = tk.Frame(Window)
    point_frame.grid(row=1)
    point_player_one = tk.Label(point_frame, text=Player_points[0], padx=20, font=("Mj_Modern_1",18))
    point_player_two = tk.Label(point_frame, text=Player_points[1], padx=20, font=("Mj_Modern_1",18))
    point_player_one.grid(row=0, column=0)
    point_player_two.grid(row=0 , column=1)

def Board():
    global buttons
    buttons = []
    counter = 0
    Board_frame = tk.Frame(Window)
    Board_frame.grid(row=2)
    for row in range(1, 4):
        for column in range(1, 4):
            index = counter
            buttons.append(index)
            buttons[index] = tk.Button(Board_frame, command=lambda x=f"{index}":clicked(x))
            buttons[index].config(width=10, height=4, font=("irannastaliq", 12, "bold"))
            buttons[index].grid(row=row, column=column)
            counter += 1


points()
Board()

Window.mainloop()
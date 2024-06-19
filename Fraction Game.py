import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class node:
    def __init__(self, name):
        self.name = name

def openStart():
    print("Opening start...")
    def playGame():
        if combo.get() == "":
            print("Select a year level dummy")
            no_year_level=messagebox.showinfo("Select a year level dummy", "Select a year level dummy")
        else:
            print("Playing game at", combo.get())
            combo.place_forget()
            username.place_forget()
            year_level.place_forget()
            play.place_forget()
            start.place(x=558, y=375)

    start.place_forget()
    highscores.place_forget()
    username = Label(window, text="Username: ", font=("Helvetica", 10))
    username.place(x=500, y=350)
    year_level = Label(window, text="Year level: ", font=("Helvetica", 10))
    year_level.place(x=500, y=375)
    combo = ttk.Combobox(
    state="readonly",
    values=["Year 5-6", "Year 7-8", "Year 9-10"])
    combo.place(x=600, y=375)
    play = Button(window, text = "Play", command = playGame, font = ("Helvetica", 30), padx = 10, pady = 10)
    play.place(x=560, y=450)
    #msg=messagebox.showinfo("Hello Python", "Hello World")

def openHighscores():
    print("Opening highscores...")
    highscore_window = tk.Toplevel(window)
    highscore_window.title("Highscores")
    highscore_window.config(bg="#DDDDDD") #Grey
    highscore_window.geometry("500x800")

def doNothing():
    pass

window = Tk()
window.title("Fractions")
window.config(bg="#300040") #Dark purple
window.geometry("1200x800")

start = Button(window, text = "Start", command = openStart, font = ("Helvetica", 30), padx = 10, pady = 10)
start.place(x=558, y=375)
highscores = Button(window, text = "Highscores", command = openHighscores, font = ("Helvetica", 24), padx = 10, pady = 10)
highscores.place(x=520, y=525)

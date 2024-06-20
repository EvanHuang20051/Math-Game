import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class seed:
    def __init__(self):
        self.name = name

def openStart():
    print("Opening start...")
    def cleanLevelSelect():
        #Getting rid of everything on the level section screen as we move away
        back.place_forget()
        username_label.place_forget()
        year_level_label.place_forget()
        username.place_forget()
        year_level.place_forget()
        play.place_forget()
        
    def playGame():
        print(username.get(), "started a game at", year_level.get())
        #Get rid of these as the game is starting
        cleanLevelSelect()
        start.place(x=532, y=375)

    def checkBoxes():
        #Check username and year level are filled
        if username.get() == "":
            print("Enter a username dummy")
            no_username=messagebox.showinfo("Enter a username dummy", "Enter a username dummy")
        elif year_level.get() == "":
            print("Select a year level dummy")
            no_year_level=messagebox.showinfo("Select a year level dummy", "Select a year level dummy")
        else:
            #Start the game
            playGame()
    
    def goBack():
        print("Going back...")
        #Get rid of these as we return to main menu
        cleanLevelSelect()
        startUp()
        
    #Get rid of these as we enter level selection
    start.place_forget()
    highscores.place_forget()
    #Back button
    back = Button(window, text = "Back", command = goBack, font = ("Helvetica", 30), padx = 10, pady = 10)
    back.place(x=10, y=10)
    #"Username" label
    username_label = Label(window, text="Username: ", font=("Helvetica", 24), width = 9)
    username_label.place(x=360, y=320)
    #Username textbox
    username = Entry(window, font=("Helvetica", 24), width = 16)
    #username.place(x=600, y=340)
    username.place(x=560, y=320)
    #"Year level" label
    year_level_label = Label(window, text="Year level: ", font=("Helvetica", 24), width = 9)
    year_level_label.place(x=360, y=370)
    #Year level dropdown
    year_level = ttk.Combobox(state="readonly", values=["Year 5-6", "Year 7-8", "Year 9-10"], font=("Helvetica", 24), width = 15)
    year_level.place(x=560, y=370)
    #Play button
    play = Button(window, text = "Play", command = checkBoxes, font = ("Helvetica", 30), padx = 10, pady = 10)
    play.place(x=536, y=450)
    #msg=messagebox.showinfo("Hello Python", "Hello World")

def openHighscores():
    print("Opening highscores...")
    highscore_window = tk.Toplevel(window)
    highscore_window.title("Highscores")
    highscore_window.config(bg="#DDDDDD") #Grey
    highscore_window.geometry("500x800")

def doNothing():
    pass

def startUp():
    #Start button
    global start
    start = Button(window, text = "Start", command = openStart, font = ("Helvetica", 30), padx = 10, pady = 10)
    start.place(x=532, y=375)
    #Highscores button
    global highscores
    highscores = Button(window, text = "Highscores", command = openHighscores, font = ("Helvetica", 24), padx = 10, pady = 10)
    highscores.place(x=499, y=525)

window = Tk()
window.title("Fractions")
window.config(bg="#300040") #Dark purple
window.geometry("1200x800")

startUp()

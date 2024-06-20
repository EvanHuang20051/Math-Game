import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class seed:
    def __init__(self):
        self.name = name

def closeProgram():
    print("Quitting program")
    exit()

def generateQuestion():
    

def openStart():
    print("Opening level selection")
    def cleanLevelSelect():
        #Getting rid of everything on the level section screen
        back.place_forget()
        username_label.place_forget()
        year_level_label.place_forget()
        username.place_forget()
        year_level.place_forget()
        play.place_forget()
    
    def playGame():
        print(username.get(), "started a game at", year_level.get())
        def tryAgain():
            end_text.place_forget()
            username_text.place_forget()
            time_text.place_forget()
            try_again_label.place_forget()
            yes.place_forget()
            no.place_forget()
            startUp()

        def cleanGame():
            #Getting rid of game visuals
            pass
        
        #Get rid of these as the game is starting
        cleanLevelSelect()
        #Game starts
        generateQuestion()
        #Game finished, clear game visuals
        win = True
        cleanGame()
        if win:
            end_text = Label(window, text="You Win!", font=("Helvetica", 72), fg="#00FF00", bg="#300040")
            end_text.place(x=400, y=150)
        else:
            end_text = Label(window, text="You Lose!", font=("Helvetica", 72), fg="#FF0000", bg="#300040")
            end_text.place(x=400, y=150)
        #Username: {username}
        username_text = Label(window, text=f"Username: {username.get()}", font=("Helvetica", 36))
        username_text.place(x=400, y=300)
        #Time: {time}
        time_text = Label(window, text=f"Time: 1:13", font=("Helvetica", 36))
        time_text.place(x=400, y=370)
        #Try again? text
        try_again_label = Label(window, text="Try again?", font=("Helvetica", 30), width = 10)
        try_again_label.place(x=501, y=450)
        #Yes and No button
        yes = Button(window, text = "Yes", command = tryAgain, font = ("Helvetica", 24), padx = 10, pady = 10)
        yes.place(x=490, y=530)
        no = Button(window, text = "No", command = closeProgram, font = ("Helvetica", 24), padx = 10, pady = 10)
        no.place(x=640, y=530)

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
        #Get rid of these as we return to main menu
        cleanLevelSelect()
        startUp()
        
    #Get rid of these as we enter level selection
    title.place_forget()
    start.place_forget()
    highscores.place_forget()
    quit_button.place_forget()
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
    print("Opening highscores window")
    highscore_window = tk.Toplevel(window)
    highscore_window.title("Highscores")
    highscore_window.config(bg="#DDDDDD") #Grey
    highscore_window.geometry("500x800")

def doNothing():
    pass

def startUp():
    print("Entering main menu")
    #Title
    global title
    title = Label(window, text = "Fractions", font = ("Helvetica", 72), fg="#FFFFFF", bg="#300040", padx = 10, pady = 10)
    title.place(x=392, y=150)
    #Start button
    global start
    start = Button(window, text = "Start", command = openStart, font = ("Helvetica", 30), padx = 10, pady = 10)
    start.place(x=532, y=370)
    #Highscores button
    global highscores
    highscores = Button(window, text = "Highscores", command = openHighscores, font = ("Helvetica", 24), padx = 10, pady = 10)
    highscores.place(x=499, y=520)
    #Quit button
    global quit_button
    quit_button = Button(window, text = "Quit", command = closeProgram, font = ("Helvetica", 24), padx = 10, pady = 10)
    quit_button.place(x=550, y=630)

window = Tk()
window.title("Fractions")
window.config(bg="#300040") #Dark purple
window.geometry("1200x800")
window.resizable(False, False)

startUp()

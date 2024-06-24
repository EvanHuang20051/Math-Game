import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import math

'''
Inclusive
Year 5-6
Add/sub: 1-5/2-5
Mult/div: 1-5/2-5

Year 7-8
Add/sub: 1-7/2-8
Mult/div: 1-7/2-8

Year 9-10
Add/sub: 1-10/2-10
Mult/div: 1-10/2-10
'''
#Using random choice and delete values we don't want to be cleaner and remove chance of random delay
class seed:
    def __init__(self):
        self.operator = random.choice(('+', '-', '*', '/'))
        if self.operator == '+' or self.operator == '-':
            valid_list1 = base_list[1:]
            valid_list2 = base_list[1:]
            self.num1 = random.choice(base_list)
            self.num2 = random.choice(base_list) #Generating the numerators
            if self.num1 in valid_list1:
                valid_list1.remove(self.num1)
            if self.num2 in valid_list2:
                valid_list2.remove(self.num2) #Don't want same numerator and denominator
            self.den1 = random.choice(valid_list1)
            if self.den1 in valid_list2:
                valid_list2.remove(self.den1) #Don't want same denominators
            self.den2 = random.choice(valid_list2)

            if self.operator == '+':
                rawnum = self.num1 * self.den2 + self.num2 * self.den1
                rawden = self.den1 * self.den2
                self.answernum, self.answerden = simplifyFraction(rawnum, rawden)
            else:
                if self.num1 * self.den2 < self.num2 * self.den1: #Swapping so answer isn't negative
                    temp = self.num1, self.den1
                    self.num1, self.den1 = self.num2, self.den2
                    self.num2, self.den2 = temp
                rawnum = self.num1 * self.den2 - self.num2 * self.den1
                rawden = self.den1 * self.den2
                self.answernum, self.answerden = simplifyFraction(rawnum, rawden)
        elif self.operator == '*':
            self.num1 = random.choice(base_list)
            self.num2 = random.choice(base_list) #Generating the numerators
            valid_list = base_list[1:]
            if self.num1 in valid_list:
                valid_list.remove(self.num1)
            if self.num2 in valid_list:
                valid_list.remove(self.num2) #Don't want same numerator and denominator or same numerator to other denominator
            self.den1 = random.choice(valid_list)
            self.den2 = random.choice(valid_list)

            rawnum = self.num1 * self.num2
            rawden = self.den1 * self.den2
            self.answernum, self.answerden = simplifyFraction(rawnum, rawden)
        else:
            self.num1 = random.choice(base_list)
            self.den2 = random.choice(base_list[1:]) #Generating a numerator and other denominator
            valid_list = base_list.copy()
            if self.num1 in valid_list:
                valid_list.remove(self.num1)
            if self.den2 in valid_list:
                valid_list.remove(self.den2) #Don't want same numerators or denominators
            self.num2 = random.choice(valid_list)
            if 1 in valid_list:
                valid_list.remove(1)
            self.den1 = random.choice(valid_list)

            rawnum = self.num1 * self.den2
            rawden = self.den1 * self.num2
            self.answernum, self.answerden = simplifyFraction(rawnum, rawden)

def simplifyFraction(num, den):
    hcf = math.gcd(num, den)
    num = num / hcf
    den = den / hcf
    return int(num), int(den)

'''class rand_fraction:
    def __init__(self):
        self.numerator = random.randrange(1, upper)
        self.denominator = random.randrange(2, upper)
        while self.numerator == self.denominator:
            self.numerator = random.randrange(1, upper)'''

def generateQuestion():
    for i in range(20):
        a_seed = seed()
        print(f"{a_seed.num1}/{a_seed.den1} {a_seed.operator} {a_seed.num2}/{a_seed.den2} = {a_seed.answernum}/{a_seed.answerden}")
        '''fraction1 = rand_fraction()
        fraction2 = rand_fraction()
        operator = random.choice(('+', '-', '*', '/'))
        if operator == '-':
            fraction1_val = fraction1.numerator / fraction1.denominator
            fraction2_val = fraction2.numerator / fraction2.denominator
            if fraction2_val > fraction1_val:
                temp = fraction1
                fraction1 = fraction2
                fraction2 = temp
        print(f"{fraction1.numerator}/{fraction1.denominator} {operator} {fraction2.numerator}/{fraction2.denominator}")'''

def startUp():
    print("Entering main menu")
    #Title
    global title
    title = Label(window, text = "Fractions", font = ("Helvetica", 72), fg="#FFFFFF", bg="#300040", padx = 10, pady = 10)
    title.place(x=392, y=140)
    #Start button
    global start
    start = Button(window, text = "Start", command = openStart, font = ("Helvetica", 30), padx = 10, pady = 10)
    start.place(x=532, y=320)
    global instructions
    instructions = Button(window, text = "Instructions", command = openInstructions, font = ("Helvetica", 24), padx = 10, pady = 10)
    instructions.place(x=496, y=440)
    #Highscores button
    global highscores
    highscores = Button(window, text = "Highscores", command = openHighscores, font = ("Helvetica", 24), padx = 10, pady = 10)
    highscores.place(x=499, y=535)
    #Quit button
    global quit_button
    quit_button = Button(window, text = "Quit", command = closeProgram, font = ("Helvetica", 24), padx = 10, pady = 10)
    quit_button.place(x=550, y=630)

def openStart():
    print("Opening level selection")
    def cleanLevelSelect():
        #Getting rid of level section screen visuals
        back.place_forget()
        username_label.place_forget()
        year_level_label.place_forget()
        username.place_forget()
        year_level.place_forget()
        play.place_forget()

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
            global base_list
            if year_level.get() == "Year 5-6":
                base_list = [1, 2, 3, 4, 5]
            elif year_level.get() == "Year 7-8":
                base_list = [1, 2, 3, 4, 5, 6, 7, 8]
            else:
                base_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            playGame()
    
    def playGame():
        print(username.get(), "started a game at", year_level.get())
        def tryAgain():
            #Getting rid of end screen visuals
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
        #"Try again?" text
        try_again_label = Label(window, text="Try again?", font=("Helvetica", 30), width = 10)
        try_again_label.place(x=501, y=450)
        #Yes and No button
        yes = Button(window, text = "Yes", command = tryAgain, font = ("Helvetica", 24), padx = 10, pady = 10)
        yes.place(x=490, y=530)
        no = Button(window, text = "No", command = closeProgram, font = ("Helvetica", 24), padx = 10, pady = 10)
        no.place(x=640, y=530)
    
    def goBack():
        #Get rid of these as we return to main menu
        cleanLevelSelect()
        startUp()
        
    #Get rid of these as we enter level selection
    title.place_forget()
    start.place_forget()
    instructions.place_forget()
    highscores.place_forget()
    quit_button.place_forget()
    #Back button
    back = Button(window, text = "Back", command = goBack, font = ("Helvetica", 30), padx = 10, pady = 10)
    back.place(x=10, y=10)
    #"Username" text
    username_label = Label(window, text="Username: ", font=("Helvetica", 24), width = 9)
    username_label.place(x=360, y=320)
    #Username textbox
    username = Entry(window, font=("Helvetica", 24), width = 16)
    username.place(x=560, y=320)
    #"Year level" text
    year_level_label = Label(window, text="Year level: ", font=("Helvetica", 24), width = 9)
    year_level_label.place(x=360, y=370)
    #Year level dropdown
    year_level = ttk.Combobox(state="readonly", values=["Year 5-6", "Year 7-8", "Year 9-10"], font=("Helvetica", 24), width = 15)
    year_level.place(x=560, y=370)
    #Play button
    play = Button(window, text = "Play", command = checkBoxes, font = ("Helvetica", 30), padx = 10, pady = 10)
    play.place(x=536, y=450)
    #msg=messagebox.showinfo("Hello Python", "Hello World")

def openInstructions():
    print("Opening instructions window")
    instructions_window = tk.Toplevel(window)
    instructions_window.title("Instructions")
    instructions_window.config(bg="#500060") #Purple
    instructions_window.geometry("600x600")
    instructions_window.resizable(False, False)
    instructions_label = Label(instructions_window, text="Instructions", font=("Helvetica", 36))
    instructions_label.place(x=200, y=30)
    line1 = Label(instructions_window, text="Fractions is a game designed to practice your fraction addition, subtraction, multiplication, and division",
                  font=("Helvetica", 12))
    line1.place(x=10, y=100)

def openHighscores():
    print("Opening highscores window")
    highscores_window = tk.Toplevel(window)
    highscores_window.title("Highscores")
    highscores_window.config(bg="#DDDDDD") #Grey
    highscores_window.geometry("500x800")

def closeProgram():
    print("Quitting program")
    exit()

window = Tk()
window.title("Fractions")
window.config(bg="#300040") #Dark purple
window.geometry("1200x800")
window.resizable(False, False)

startUp()

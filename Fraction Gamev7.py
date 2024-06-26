import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import math

class seed:
    def __init__(self):
        self.operator = random.choice(('+', '-', '*', '/'))
        #Denominators cannot be 1
        if self.operator == '+' or self.operator == '-':
            valid_list1 = base_list[1:] #Valid list for first denominator
            valid_list2 = base_list[1:] #Valid list for second denominator
            self.num1 = random.choice(base_list)
            self.num2 = random.choice(base_list) #Generating the numerators
            if self.num1 in valid_list1:
                valid_list1.remove(self.num1)
            if self.num2 in valid_list2:
                valid_list2.remove(self.num2) #Don't want same numerator and denominator
            self.den1 = random.choice(valid_list1) #Generating the first denominator
            if self.den1 in valid_list2:
                valid_list2.remove(self.den1) #Don't want same denominators
            self.den2 = random.choice(valid_list2) #Generating the second denominator

            if self.operator == '+':
                rawnum = self.num1 * self.den2 + self.num2 * self.den1
                rawden = self.den1 * self.den2 #Numerator and denominator of answer
                self.answernum, self.answerden = simplifyFraction(rawnum, rawden) #Simplifying
            else:
                if self.num1 * self.den2 < self.num2 * self.den1:
                    temp = self.num1, self.den1
                    self.num1, self.den1 = self.num2, self.den2
                    self.num2, self.den2 = temp #Swapping so answer isn't negative
                rawnum = self.num1 * self.den2 - self.num2 * self.den1
                rawden = self.den1 * self.den2 #Numerator and denominator of answer
                self.answernum, self.answerden = simplifyFraction(rawnum, rawden) #Simplifying
        elif self.operator == '*':
            self.num1 = random.choice(base_list)
            self.num2 = random.choice(base_list) #Generating the numerators
            valid_list = base_list[1:] #Valid list for denominators
            if self.num1 in valid_list:
                valid_list.remove(self.num1)
            if self.num2 in valid_list:
                valid_list.remove(self.num2) #Don't want same numerator and denominator or numerator to other denominator
            self.den1 = random.choice(valid_list)
            self.den2 = random.choice(valid_list) #Generating the denominators

            rawnum = self.num1 * self.num2
            rawden = self.den1 * self.den2 #Numerator and denominator of answer
            self.answernum, self.answerden = simplifyFraction(rawnum, rawden) #Simplifying
        else:
            self.num1 = random.choice(base_list)
            self.den2 = random.choice(base_list[1:]) #Generating a numerator and other denominator
            valid_list = base_list.copy() #Valid list for denominator and other numerator
            if self.num1 in valid_list:
                valid_list.remove(self.num1)
            if self.den2 in valid_list:
                valid_list.remove(self.den2) #Don't want same numerators or denominators
            self.num2 = random.choice(valid_list) #Generating other numerator
            if 1 in valid_list:
                valid_list.remove(1) #Don't want denominator to be 1
            self.den1 = random.choice(valid_list) #Generating denominator

            rawnum = self.num1 * self.den2
            rawden = self.den1 * self.num2
            self.answernum, self.answerden = simplifyFraction(rawnum, rawden)

def simplifyFraction(num, den):
    hcf = math.gcd(num, den)
    num = num / hcf #Error when divide by zero, need to prevent this in earlier function
    den = den / hcf
    return int(num), int(den)

def generateQuestion():
    question = seed()
    print(f"{question.num1}/{question.den1} {question.operator} {question.num2}/{question.den2}") # = {question.answernum}/{question.answerden}

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
        def cleanGame():
            #Getting rid of game visuals
            submit_num.place_forget()
            submit_den.place_forget()
            submit_button.place_forget()

        def submit(submit_num, submit_den):
            global number_correct
            if not (submit_num.isdigit() and submit_den.isdigit()):
                print("Enter integers dummy, and no negatives")
            else:
                submit_num = int(submit_num)
                submit_den = int(submit_den)
                if (submit_num, submit_den) == (1, 1):
                    print("Correct!")
                    number_correct += 1
                    if number_correct < 5:
                        generateQuestion()
                    else:
                        endGame()
                elif simplifyFraction(submit_num, submit_den) == (1, 1):
                    print("Remember to simplify your answer!")
                else:
                    print("Wrong!")
                    if number_correct < 5:
                        generateQuestion()
                    else:
                        endGame()

        def endGame():
            def tryAgain():
                #Getting rid of end screen visuals
                end_text.place_forget()
                username_text.place_forget()
                time_text.place_forget()
                try_again_label.place_forget()
                yes.place_forget()
                no.place_forget()
                startUp()
            
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
        
        #Get rid of these as the game is starting
        cleanLevelSelect()
        #Game starts
        global number_correct
        number_correct = 0
        submit_num = Entry(window, font=("Helvetica", 24), width = 5, justify = "center")
        submit_num.place(x=570, y=450)
        submit_den = Entry(window, font=("Helvetica", 24), width = 5, justify = "center")
        submit_den.place(x=570, y=500)
        submit_button = Button(window, text = "Submit", command = lambda:submit(submit_num.get(), submit_den.get()), font = ("Helvetica", 30), padx = 10, pady = 10)
        submit_button.place(x=532, y=600)
        
        generateQuestion()
        
        #Game finished, clear game visuals
        
    
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

def startUp():
    global title, start, instructions, highscores, quit_button
    print("Entering main menu")
    #Title
    title = Label(window, text = "Fractions", font = ("Helvetica", 72), fg="#FFFFFF", bg="#300040", padx = 10, pady = 10)
    title.place(x=392, y=140)
    #Start button
    start = Button(window, text = "Start", command = openStart, font = ("Helvetica", 30), padx = 10, pady = 10)
    start.place(x=532, y=320)
    instructions = Button(window, text = "Instructions", command = openInstructions, font = ("Helvetica", 24), padx = 10, pady = 10)
    instructions.place(x=496, y=440)
    #Highscores button
    highscores = Button(window, text = "Highscores", command = openHighscores, font = ("Helvetica", 24), padx = 10, pady = 10)
    highscores.place(x=499, y=535)
    #Quit buttons
    quit_button = Button(window, text = "Quit", command = closeProgram, font = ("Helvetica", 24), padx = 10, pady = 10)
    quit_button.place(x=550, y=630)

window = Tk()
window.title("Fractions")
window.config(bg="#300040") #Dark purple
window.geometry("1200x800")
window.resizable(False, False)

startUp()

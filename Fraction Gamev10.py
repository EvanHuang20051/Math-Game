import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import math
import time
import os

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
    num = num / hcf
    den = den / hcf
    return int(num), int(den)


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

    def checkEntries():
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
            if year_level.get() == "Year 7-8":
                base_list = [1, 2, 3, 4, 5]
            elif year_level.get() == "Year 9-10":
                base_list = [1, 2, 3, 4, 5, 6, 7]
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

        def generateQuestion():
            question = seed()
            global question_label
            question_label = Label(window, text=f"{question.num1}/{question.den1} {question.operator} {question.num2}/{question.den2}", font=("Helvetica", 48), width = 9, justify = "center")
            question_label.place(x=428, y=300)
            print(f"Answer: {question.answernum}/{question.answerden}")
            global answer
            answer = (question.answernum, question.answerden)
            global q_start
            q_start = time.time()
        
        def submit(num, den):
            global number_correct
            if not (num.isdigit() and den.isdigit()):
                print("Enter integers dummy, and no symbols")
            else:
                num = int(num)
                den = int(den)
                if (num, den) == answer:
                    print("Correct!")
                    number_correct += 1
                    q_end = time.time()
                    q_time_taken = q_end - q_start
                    print(f"You spent {round(q_time_taken, 2)} seconds on that question")
                    submit_num.delete(0, 'end')
                    submit_den.delete(0, 'end')
                    question_label.place_forget()
                    if number_correct < 6:
                        generateQuestion()
                    else:
                        endGame()
                elif (num, den) == (0, 0):
                    print("You're doing this on purpose, aren't you. Don't do 0 over 0") #Otherwise this would produce an error
                elif simplifyFraction(num, den) == answer:
                    print("Remember to simplify your answer!") #Remind player to simplify their answer
                else:
                    print("Wrong!")
                    submit_num.delete(0, 'end')
                    submit_den.delete(0, 'end')
                    question_label.place_forget()
                    generateQuestion()

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

            end = time.time() #Record time at end of game
            time_taken = end - start #Calculates total time taken
            if time_taken < 90:
                win = True
            else:
                win = False
            cleanGame() #Getting rid of game visuals
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
            time_text = Label(window, text=f"Time: {round(time_taken, 2)}", font=("Helvetica", 36))
            time_text.place(x=400, y=370)
            #"Try again?" text
            try_again_label = Label(window, text="Try again?", font=("Helvetica", 30), width = 10)
            try_again_label.place(x=479, y=450)
            #Yes and No button
            yes = Button(window, text = "Yes", command = tryAgain, font = ("Helvetica", 24), padx = 10, pady = 10)
            yes.place(x=475, y=530)
            no = Button(window, text = "No", command = closeProgram, font = ("Helvetica", 24), padx = 10, pady = 10)
            no.place(x=625, y=530)
        
        #Get rid of these as the game is starting
        cleanLevelSelect()
        #Game starts
        global number_correct
        number_correct = 0
        #Submission boxes
        submit_num = Entry(window, font=("Helvetica", 24), width = 5, justify = "center")
        submit_num.place(x=551, y=450)
        submit_den = Entry(window, font=("Helvetica", 24), width = 5, justify = "center")
        submit_den.place(x=551, y=500)
        #Submit button
        submit_button = Button(window, text = "Submit", command = lambda:submit(submit_num.get(), submit_den.get()), font = ("Helvetica", 30), padx = 10, pady = 10)
        submit_button.place(x=511, y=600)
        #Finish line graphic
        #finish_line = PhotoImage(file=os.getcwd()+"\filename.png")
        #label_name Label(window, image=image_variable_name)
        start = time.time() #Record time at start of game
        generateQuestion()
    
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
    year_level = ttk.Combobox(state="readonly", values=["Year 7-8", "Year 9-10", "Year 11-12"], font=("Helvetica", 24), width = 15)
    year_level.place(x=560, y=370)
    #Play button
    play = Button(window, text = "Play", command = checkEntries, font = ("Helvetica", 30), padx = 10, pady = 10)
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
    line1 = Label(instructions_window, text="Fractions is a game designed to practice your basic fraction operations ( + - * / )",
                  font=("Helvetica", 12))
    line2 = Label(instructions_window, text="After pressing start, choose a username and select a year level difficulty",
                  font=("Helvetica", 12))
    line3 = Label(instructions_window, text="Year 7-8 uses numbers 1 to 5, Year 9-10 uses 1 to 7, Year 11-12 uses 1 to 10",
                  font=("Helvetica", 12))
    line4 = Label(instructions_window, text="Each correct answer advances your rocket. Race to get to the finish line before the AI!",
                  font=("Helvetica", 12))
    line5 = Label(instructions_window, text="Your numerator and denominator must be integers with no symbols, and simplified",
                  font=("Helvetica", 12))
    line6 = Label(instructions_window, text="If your answer is invalid or not simplified, you are given another chance",
                  font=("Helvetica", 12))
    line7 = Label(instructions_window, text="If your answer is correct or wrong, we move on to the next question",
                  font=("Helvetica", 12))
    line8 = Label(instructions_window, text="At the end of the game, your score is recorded to the Highscores window",
                  font=("Helvetica", 12))
    line1.place(x=5, y=100)
    line2.place(x=5, y=125)
    line3.place(x=5, y=150)
    line4.place(x=5, y=175)
    line5.place(x=5, y=200)
    line6.place(x=5, y=225)
    line7.place(x=5, y=250)
    line8.place(x=5, y=275)


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

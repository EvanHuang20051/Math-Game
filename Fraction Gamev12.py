'''
This program is a game designed to practice basic fraction operations ( + - × ÷ )
The target audience is students in years 7-12
'''
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
        '''Generates a random fraction question, avoiding questions that are too easy'''
        #Note that denominators cannot be 1
        self.operator = random.choice(('+', '-', '×', '÷'))        
        if self.operator == '+' or self.operator == '-':
            valid_list1 = base_list[1:] #Valid list for denominators
            valid_list2 = base_list[1:]
            self.num1 = random.choice(base_list) #Generating numerator
            self.num2 = random.choice(base_list)
            if self.num1 in valid_list1:
                valid_list1.remove(self.num1) #Don't want same numerator and denominator
            if self.num2 in valid_list2:
                valid_list2.remove(self.num2)
            self.den1 = random.choice(valid_list1)
            if self.den1 in valid_list2:
                valid_list2.remove(self.den1) #Don't want same denominators
            self.den2 = random.choice(valid_list2)

            if self.operator == '+':
                rawnum = self.num1 * self.den2 + self.num2 * self.den1 #Numerator and denominator of answer
                rawden = self.den1 * self.den2
                self.answernum, self.answerden = simplifyFraction(rawnum, rawden) #Simplifying
            else:
                if self.num1 * self.den2 < self.num2 * self.den1:
                    temp = self.num1, self.den1
                    self.num1, self.den1 = self.num2, self.den2
                    self.num2, self.den2 = temp #Swapping so answer isn't negative
                rawnum = self.num1 * self.den2 - self.num2 * self.den1 #Numerator and denominator of answer
                rawden = self.den1 * self.den2
                self.answernum, self.answerden = simplifyFraction(rawnum, rawden) #Simplifying
        elif self.operator == '×':
            valid_list = base_list[1:] #Valid list for denominators
            self.num1 = random.choice(base_list) #Generating the numerators
            self.num2 = random.choice(base_list)
            if self.num1 in valid_list:
                valid_list.remove(self.num1) #Don't want same numerator and denominator or numerator to other denominator
            if self.num2 in valid_list:
                valid_list.remove(self.num2)
            self.den1 = random.choice(valid_list) #Generating the denominators
            self.den2 = random.choice(valid_list)

            rawnum = self.num1 * self.num2
            rawden = self.den1 * self.den2
            self.answernum, self.answerden = simplifyFraction(rawnum, rawden) #Simplifying
        else:
            valid_list = base_list.copy() #Valid list for denominator and other numerator
            self.num1 = random.choice(base_list) #Generating numerator and other denominator
            self.den2 = random.choice(base_list[1:])
            if self.num1 in valid_list:
                valid_list.remove(self.num1) #Don't want same numerators or denominators
            if self.den2 in valid_list:
                valid_list.remove(self.den2)
            self.num2 = random.choice(valid_list)
            if 1 in valid_list:
                valid_list.remove(1) #Don't want denominator to be 1
            self.den1 = random.choice(valid_list)

            rawnum = self.num1 * self.den2
            rawden = self.den1 * self.num2
            self.answernum, self.answerden = simplifyFraction(rawnum, rawden) #Simplifying


def simplifyFraction(num, den):
    '''Simplifies the given fraction'''
    hcf = math.gcd(num, den)
    num = num / hcf
    den = den / hcf
    return int(num), int(den)


def openStart():
    '''Functions for the level select screen'''
    print("Opening level selection")
    def cleanLevelSelect():
        '''Gets rid of level section screen visuals'''
        back.place_forget()
        username_label.place_forget()
        year_level_label.place_forget()
        AI_difficulty_label.place_forget()
        username.place_forget()
        year_level.place_forget()
        AI_difficulty.place_forget()
        play.place_forget()


    def checkEntries():
        '''Checks if entry boxes are filled, beginning the game if they are and warning if they are not'''
        if username.get() == "":
            print("Enter a username, dummy")
            no_username=messagebox.showinfo("Enter a username, dummy", "Enter a username, dummy")
        elif year_level.get() == "":
            print("Select a year level, dummy")
            no_year_level=messagebox.showinfo("Select a year level, dummy", "Select a year level, dummy")
        elif AI_difficulty.get() == "":
            print("Select an AI difficulty, dummy")
            no_AI_difficulty=messagebox.showinfo("Select an AI difficulty, dummy", "Select an AI difficulty, dummy")
        else:
            #Start the game
            global base_list
            if year_level.get() == "Year 7-8":
                base_list = [1, 2, 3, 4, 5]
            elif year_level.get() == "Year 9-10":
                base_list = [1, 2, 3, 4, 5, 6, 7]
            else:
                base_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            global time_limit
            if AI_difficulty.get() == "Easy":
                time_limit = 120
            elif AI_difficulty.get() == "Medium":
                time_limit = 105
            else:
                time_limit = 90
            playGame()

    
    def playGame():
        '''Functions for the gameplay'''
        print(username.get(), "started a game at", year_level.get())
        def cleanGame():
            '''Gets rid of game visuals'''
            submit_num.place_forget()
            submit_den.place_forget()
            submit_button.place_forget()
            game_canvas.itemconfig(1, state='hidden')

        def generateQuestion():
            '''Prompts question generation and displays it'''
            question = seed()
            global fraction1num_label, fraction1den_label, operator_label, fraction2num_label, fraction2den_label
            fraction1num_label = Label(window, text=f"{question.num1}", font=("Helvetica", 48), width = 2, justify = "center")
            fraction1den_label = Label(window, text=f"{question.den1}", font=("Helvetica", 48), width = 2, justify = "center")
            operator_label = Label(window, text=f"{question.operator}", font=("Helvetica", 48), width = 2, justify = "center")
            fraction2num_label = Label(window, text=f"{question.num2}", font=("Helvetica", 48), width = 2, justify = "center")
            fraction2den_label = Label(window, text=f"{question.den2}", font=("Helvetica", 48), width = 2, justify = "center")
            fraction1num_label.place(x=450, y=265)
            fraction1den_label.place(x=450, y=350)
            operator_label.place(x=560, y=305)
            fraction2num_label.place(x=670, y=265)
            fraction2den_label.place(x=670, y=350)
            print(f"Answer: {question.answernum}/{question.answerden}")
            global answer
            answer = (question.answernum, question.answerden)
            global q_start
            q_start = time.time()

        
        def submit(num, den):
            '''Functions when submitting an answer'''
            def cleanEntries():
                '''Clears entry boxes and gets rid of question'''
                submit_num.delete(0, 'end')
                submit_den.delete(0, 'end')
                fraction1num_label.place_forget()
                fraction1den_label.place_forget()
                operator_label.place_forget()
                fraction2num_label.place_forget()
                fraction2den_label.place_forget()

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
                    cleanEntries()
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
                    cleanEntries()
                    generateQuestion()


        def endGame():
            '''Functions when the gameplay ends'''
            def tryAgain():
                '''Gets rid of end screen visuals and restarts program'''
                end_text.place_forget()
                username_text.place_forget()
                time_text.place_forget()
                try_again_label.place_forget()
                yes.place_forget()
                no.place_forget()
                startUp()

            end = time.time() #Record time at end of game
            time_taken = end - start #Calculates total time taken
            if time_taken < time_limit:
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
            #Record result
        
        cleanLevelSelect() #Get rid of these as the game is starting
        #Game starts
        game_canvas = Canvas(window, bg="#300040", height=800, width=1200, bd=0, highlightthickness=0)
        game_canvas.place(x=0, y=0)
        #window.wm_attributes("-transparentcolor", "yellow")
        
        global number_correct
        number_correct = 0
        #Submission boxes
        submit_num = Entry(window, font=("Helvetica", 24), width = 5, justify = "center")
        submit_num.place(x=551, y=500)
        submit_den = Entry(window, font=("Helvetica", 24), width = 5, justify = "center")
        submit_den.place(x=551, y=550)
        #Submit button
        submit_button = Button(window, text = "Submit", command = lambda:submit(submit_num.get(), submit_den.get()), font = ("Helvetica", 30), padx = 10, pady = 10)
        submit_button.place(x=511, y=630)
        
        #Finish line graphic
        finish_line_image = PhotoImage(file="Finish-flag-removebg20%.png")
        #finish_line_label = Label(window, image=finish_line_image)
        
        finish_line_image.image = finish_line_image #Prevent garbage collection
        #finish_line_label.place(x=1000, y=20)

        game_canvas.create_image(1000,100,image=finish_line_image)
        
        #current_time = time.time()
        #elapsed_time = current_time - start
        #round(elaspsed_time, 2)
        
        start = time.time() #Record time at start of game
        generateQuestion()

    
    def goBack():
        '''Go back to main menu'''
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
    username_label = Label(window, text="Username: ", font=("Helvetica", 24), width = 10)
    username_label.place(x=350, y=320)
    #Username textbox
    username = Entry(window, font=("Helvetica", 24), width = 16)
    username.place(x=560, y=320)
    #"Year level" text
    year_level_label = Label(window, text="Year level: ", font=("Helvetica", 24), width = 10)
    year_level_label.place(x=350, y=370)
    #Year level dropdown
    year_level = ttk.Combobox(state="readonly", values=["Year 7-8", "Year 9-10", "Year 11-12"], font=("Helvetica", 24), width = 15)
    year_level.place(x=560, y=370)
    #Add AI difficulty text
    AI_difficulty_label = Label(window, text="AI difficulty: ", font=("Helvetica", 24), width = 10)
    AI_difficulty_label.place(x=350, y=420)
    #Add AI difficulty dropdown
    AI_difficulty = ttk.Combobox(state="readonly", values=["Easy", "Medium", "Hard"], font=("Helvetica", 24), width = 15)
    AI_difficulty.place(x=560, y=420)
    #Play button
    play = Button(window, text = "Play", command = checkEntries, font = ("Helvetica", 30), padx = 10, pady = 10)
    play.place(x=536, y=500)
    #msg=messagebox.showinfo("Hello Python", "Hello World")


def openInstructions():
    '''Opens the Intructions window'''
    print("Opening instructions window")
    instructions_window = tk.Toplevel(window)
    instructions_window.title("Instructions")
    instructions_window.config(bg="#500060") #Purple
    instructions_window.geometry("600x600")
    instructions_window.resizable(False, False)
    instructions_label = Label(instructions_window, text="Instructions", font=("Helvetica", 36))
    instructions_label.place(x=200, y=30)
    line1 = Label(instructions_window, text="Fractions is a game designed to practice your basic fraction operations ( + - × ÷ )",
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
    '''Opens the Highscores window'''
    print("Opening highscores window")
    highscores_window = tk.Toplevel(window)
    highscores_window.title("Highscores")
    highscores_window.config(bg="#CCCCCC") #Grey
    highscores_window.geometry("1000x600")
    highscores_window.resizable(False, False)
    #Username | Time | Year level | AI difficulty | Win status
    username_label = Label(highscores_window, text="Username", font=("Helvetica", 24), width = 9)
    time_label = Label(highscores_window, text="Time", font=("Helvetica", 24), width = 9)
    year_level_label = Label(highscores_window, text="Year Level", font=("Helvetica", 24), width = 9)
    AI_difficulty_label = Label(highscores_window, text="AI Difficulty", font=("Helvetica", 24), width = 9)
    win_status_label = Label(highscores_window, text="Result", font=("Helvetica", 24), width = 9)
    #Placing labels
    username_label.place(x=10, y=10)
    time_label.place(x=210, y=10)
    year_level_label.place(x=410, y=10)
    AI_difficulty_label.place(x=610, y=10)
    win_status_label.place(x=810, y=10)
    #Sort by: Year level, Time, AI difficulty


def closeProgram():
    '''Closes the program'''
    print("Quitting program")
    exit()


def startUp():
    '''Opens the main menu'''
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

'''
Author: Evan Huang
Date: 02/09/24
This program is a game designed to practice basic fraction operations ( + - × ÷ ).
The target audience is students in years 7-12.
'''
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import math
import time
import os
import json


class Seed:
    '''Randomly generated fraction question.'''

    def __init__(self):
        '''Generates a random fraction question, avoiding questions that are too easy.'''

        # Note that denominators cannot be 1
        self.operator = random.choice(('+', '-', '×', '÷'))        
        if self.operator == '+' or self.operator == '-':
            valid_list1 = base_list[1:] # Valid list for denominators
            valid_list2 = base_list[1:]
            self.num1 = random.choice(base_list) # Generating numerators
            self.num2 = random.choice(base_list)
            if self.num1 in valid_list1:
                valid_list1.remove(self.num1) # Don't want same numerator and denominator
            if self.num2 in valid_list2:
                valid_list2.remove(self.num2)
            self.den1 = random.choice(valid_list1)
            if self.den1 in valid_list2:
                valid_list2.remove(self.den1) # Don't want same denominators
            self.den2 = random.choice(valid_list2)

            if self.operator == '+':
                rawnum = self.num1 * self.den2 + self.num2 * self.den1 # Numerator and denominator of answer
                rawden = self.den1 * self.den2
                self.answernum, self.answerden = simplifyFraction(rawnum, rawden) # Simplifying
            else:
                if self.num1 * self.den2 < self.num2 * self.den1:
                    temp = self.num1, self.den1
                    self.num1, self.den1 = self.num2, self.den2
                    self.num2, self.den2 = temp # Swapping so answer isn't negative
                rawnum = self.num1 * self.den2 - self.num2 * self.den1 # Numerator and denominator of answer
                rawden = self.den1 * self.den2
                self.answernum, self.answerden = simplifyFraction(rawnum, rawden)
        elif self.operator == '×':
            valid_list = base_list[1:] # Valid list for denominators
            self.num1 = random.choice(base_list) # Generating the numerators
            self.num2 = random.choice(base_list)
            if self.num1 in valid_list:
                valid_list.remove(self.num1) # Don't want same numerator and denominator or numerator to other denominator
            if self.num2 in valid_list:
                valid_list.remove(self.num2)
            self.den1 = random.choice(valid_list) # Generating the denominators
            self.den2 = random.choice(valid_list)

            rawnum = self.num1 * self.num2
            rawden = self.den1 * self.den2
            self.answernum, self.answerden = simplifyFraction(rawnum, rawden) # Simplifying
        else:
            valid_list = base_list.copy() # Valid list for denominator and other numerator
            self.num1 = random.choice(base_list) # Generating numerator and other denominator
            self.den2 = random.choice(base_list[1:])
            if self.num1 in valid_list:
                valid_list.remove(self.num1) # Don't want same numerators or denominators
            if self.den2 in valid_list:
                valid_list.remove(self.den2)
            self.num2 = random.choice(valid_list)
            if 1 in valid_list:
                valid_list.remove(1) # Don't want denominator to be 1
            self.den1 = random.choice(valid_list)

            rawnum = self.num1 * self.den2
            rawden = self.den1 * self.num2
            self.answernum, self.answerden = simplifyFraction(rawnum, rawden)


def simplifyFraction(num, den):
    '''Returns the simplified fraction'''
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
        '''Checks if entry boxes are filled, beginning the game if they are and giving a warning if they are not'''
        if username.get() == "":
            print("Please enter a Username")
            no_username = messagebox.showwarning("Username missing", "Please enter a Username")
        elif year_level.get() == "":
            print("Please select a Year Level")
            no_year_level = messagebox.showwarning("Year Level missing", "Please select a Year Level")
        elif AI_difficulty.get() == "":
            print("Please select an AI difficulty")
            no_AI_difficulty = messagebox.showwarning("AI difficulty missing", "Please select an AI difficulty")
        elif len(username.get()) > 18:
            shorten_username = messagebox.showwarning("Username exceeds maximum length", "Username must be 18 characters or less!")
            print("Username must be 18 characters or less!")
        else:
            # Start the game
            global base_list
            if year_level.get() == "Year 7-8":
                base_list = [1, 2, 3, 4, 5]
            elif year_level.get() == "Year 9-10":
                base_list = [1, 2, 3, 4, 5, 6, 7]
            else:
                base_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            global time_limit
            if AI_difficulty.get() == "Easy":
                time_limit = 170
            elif AI_difficulty.get() == "Medium":
                time_limit = 140
            else:
                time_limit = 110
            playGame()

    
    def playGame():
        '''Functions for the gameplay'''
        print(username.get(), "started a game at", year_level.get())
        def cleanGame():
            '''Gets rid of game visuals and bindings'''
            submit_num.place_forget()
            submit_den.place_forget()
            submit_button.place_forget()
            window.unbind("<Return>") # Unbind Enter key

        def generateQuestion():
            '''Prompts question generation and displays it'''
            question = Seed()
            global fraction1num_label, fraction1den_label, operator_label, fraction2num_label, fraction2den_label
            fraction1num_label = Label(window, text=f"{question.num1}", font=("Helvetica", 48), width = 2, justify = "center")
            fraction1den_label = Label(window, text=f"{question.den1}", font=("Helvetica", 48), width = 2, justify = "center")
            operator_label = Label(window, text=f"{question.operator}", font=("Helvetica", 48), width = 2, justify = "center")
            fraction2num_label = Label(window, text=f"{question.num2}", font=("Helvetica", 48), width = 2, justify = "center")
            fraction2den_label = Label(window, text=f"{question.den2}", font=("Helvetica", 48), width = 2, justify = "center")
            fraction1num_label.place(x=449, y=265)
            fraction1den_label.place(x=449, y=350)
            operator_label.place(x=559, y=305)
            fraction2num_label.place(x=669, y=265)
            fraction2den_label.place(x=669, y=350)
            print(f"Answer: {question.answernum}/{question.answerden}")
            global answer
            answer = (question.answernum, question.answerden)
            global q_start
            q_start = time.time()
        
        def submit(num, den): # event = None unecessary
            '''Functions when submitting an answer'''
            def PlayerStep(steps):
                '''Animates Player Rocket sprite moving to the right for a total of 10 * 10 = 100 units'''
                if steps != 0:
                    game_canvas.move(player, 10, 0)
                    window.after(4, lambda:PlayerStep(steps - 1))

            def displayText(text, x_cord, colour):
                '''Function for temporarily displaying text like "Correct!" or "Simplify your answer!"'''
                def removeText():
                    text_label.place_forget()
                text_label = Label(window, text=text, font=("Helvetica", 36), fg=colour, bg="#300040")
                text_label.place(x=x_cord, y=180)
                window.after(2000, removeText)
            
            def cleanEntries():
                '''Clears entry boxes and gets rid of question'''
                submit_num.delete(0, 'end')
                submit_den.delete(0, 'end')
                fraction1num_label.place_forget()
                fraction1den_label.place_forget()
                operator_label.place_forget()
                fraction2num_label.place_forget()
                fraction2den_label.place_forget()

            global number_correct, dest_x
            if not (num.isdigit() and den.isdigit()):
                print("Enter integers only!")
                displayText("Enter integers only!", 390, "#FF0000")
            else:
                num = int(num)
                den = int(den)
                if (num, den) == answer:
                    print("Correct!")
                    displayText("Correct!", 511, "#00FF00")
                    number_correct += 1
                    q_end = time.time()
                    q_time_taken = q_end - q_start
                    print(f"You spent {round(q_time_taken, 2)} seconds on that question")
                    cleanEntries()
                    PlayerStep(10)
                    if number_correct < 8:
                        generateQuestion()
                    else:
                        endGame()
                elif den == 0:
                    print("Don't divide by zero!") # Otherwise this would produce an error
                    displayText("Don't divide by zero!", 380, "#FF0000")
                elif simplifyFraction(num, den) == answer:
                    print("Simplify your answer!") # Remind player to simplify their answer
                    displayText("Simplify your answer!", 371, "Cyan")
                else:
                    print("Wrong!")
                    displayText("Wrong!", 519, "#FF0000")
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
                game_canvas.itemconfig(1, state='hidden')
                game_canvas.itemconfig(2, state='hidden')
                startUp()

            end = time.time() # Record time at end of game
            time_taken = end - start # Calculates total time taken
            global stop
            stop = True
            cleanGame() # Getting rid of game visuals and bindings
            if time_taken < time_limit:
                win = True
            else:
                win = False
            if win:
                end_text = Label(window, text="You Win!", font=("Helvetica", 72), fg="#00FF00", bg="#300040")
                end_text.place(x=404, y=150)
            else:
                end_text = Label(window, text="You Lose!", font=("Helvetica", 72), fg="#FF0000", bg="#300040")
                end_text.place(x=385, y=150)
            # Username: {username}
            username_text = Label(window, text=f"Username: {username.get()}", font=("Helvetica", 36))
            username_text.place(x=400, y=300)
            # Time: {time}
            time_text = Label(window, text=f"Time: {time_taken:.2f}", font=("Helvetica", 36))
            time_text.place(x=400, y=370)
            # "Try again?" text
            try_again_label = Label(window, text="Try again?", font=("Helvetica", 30), width = 10)
            try_again_label.place(x=481, y=450)
            # Record result
            record_score(username.get(), time_taken, year_level.get(), AI_difficulty.get(), win)
            print(year_level.get(), AI_difficulty.get())
            # Yes and No button
            yes = Button(window, text = "Yes", command = tryAgain, font = ("Helvetica", 24), padx = 10, pady = 10)
            yes.place(x=481, y=530)
            no = Button(window, text = "No", command = closeProgram, font = ("Helvetica", 24), padx = 10, pady = 10)
            no.place(x=631, y=530)

        def record_score(username, time_taken, year_level, AI_difficulty, win):
            '''Recording score into the scores.json file, placing it at its correct rank'''
            my_score = {"username": username, "time_taken": time_taken, "year_level": year_level, "AI_difficulty": AI_difficulty, "win_status": "Win" if win else "Loss"}
            try:
                with open("scores.json", 'r') as file:
                    data_list = json.load(file)
            except FileNotFoundError:
                data_list = []
            except json.decoder.JSONDecodeError:
                data_list = []
            index = 0
            while index < len(data_list) and not(my_score_better(my_score, data_list[index])): index +=1
            data_list.insert(index, my_score)
            with open("scores.json", 'w') as file:
                json.dump(data_list, file)

        def my_score_better(my_score, data):
            '''Checks if the "data" score should be considered better than the "my_score" score'''
            # Rank by: 1. Win status, 2. Year level, 3. AI difficulty, 4. Time, 5. Recency
            if my_score["win_status"] == "Win" and data["win_status"] == "Loss":
                return True
            elif my_score["win_status"] == "Loss" and data["win_status"] == "Win":
                return False
            if (my_score["year_level"] == "Year 11-12" and data["year_level"] != "Year 11-12") or (my_score["year_level"] == "Year 9-10" and data["year_level"] == "Year 7-8"):
                return True
            elif my_score["year_level"] != data["year_level"]:
                return False
            if (my_score["AI_difficulty"] == "Hard" and data["AI_difficulty"] != "Hard") or (my_score["AI_difficulty"] == "Medium" and data["AI_difficulty"] == "Easy"):
                return True
            elif my_score["AI_difficulty"] != data["AI_difficulty"]:
                return False
            if my_score["time_taken"] < data["time_taken"]:
                return True
            else:
                return False
        
        cleanLevelSelect() # Get rid of these as the game is starting
        # Game starts
        game_canvas = Canvas(window, bg="#300040", height=800, width=1200, bd=0, highlightthickness=0)
        game_canvas.place(x=0, y=0)
        
        global number_correct
        number_correct = 0
        # Submission boxes
        submit_num = Entry(window, font=("Helvetica", 24), width = 5, justify = "center")
        submit_num.place(x=552, y=500)
        submit_den = Entry(window, font=("Helvetica", 24), width = 5, justify = "center")
        submit_den.place(x=552, y=550)
        # Submit button
        submit_button = Button(window, text = "Submit", command = lambda:submit(submit_num.get(), submit_den.get()), font = ("Helvetica", 30), padx = 10, pady = 10)
        submit_button.place(x=511, y=630)
        # Bind enter key
        window.bind("<Return>", lambda event:submit(submit_num.get(), submit_den.get()))
        # Finish line graphic
        finish_line_image = PhotoImage(file="Finish-flag-removebg20%.png")
        game_canvas.image = finish_line_image # Prevent garbage collection
        game_canvas.create_image(1000,100,image=finish_line_image)
        
        global player_image, AI_image # This also prevents garbage collection
        player_image = PhotoImage(file="PlayerRocket30%.png")
        player = game_canvas.create_image(150,100,image=player_image)

        generateQuestion()
        global stop
        stop = False
        start = time.time() # Record time at start of game
        timer_label = Label(window, text=f"{0.00}", font=("Helvetica", 24), width = 6)
        timer_label.place(x=540, y=10)
        def minusTime():
            '''Live stopwatch'''
            if stop:
                timer_label.place_forget()
                return
            current_time = time.time()
            elapsed_time = current_time - start
            timer_label.config(text=f"{elapsed_time:.2f}")
            window.after(90, minusTime) # Updated every 90 milliseconds
        minusTime()
    
    def goBack():
        '''Go back to main menu'''
        cleanLevelSelect()
        startUp()
        
    # Get rid of these as we enter level selection
    title.place_forget()
    start.place_forget()
    instructions.place_forget()
    highscores.place_forget()
    quit_button.place_forget()
    # Back button
    back = Button(window, text = "Back", command = goBack, font = ("Helvetica", 30), padx = 10, pady = 10)
    back.place(x=10, y=10)
    # "Username" text
    username_label = Label(window, text="Username: ", font=("Helvetica", 24), width = 10)
    username_label.place(x=350, y=300)
    # Username textbox
    username = Entry(window, font=("Helvetica", 24), width = 16)
    username.place(x=559, y=300)
    # "Year level" text
    year_level_label = Label(window, text="Year level: ", font=("Helvetica", 24), width = 10)
    year_level_label.place(x=350, y=350)
    # Year level dropdown
    year_level = ttk.Combobox(state="readonly", values=["Year 7-8", "Year 9-10", "Year 11-12"], font=("Helvetica", 24), width = 15)
    year_level.place(x=559, y=350)
    # Add AI difficulty text
    AI_difficulty_label = Label(window, text="AI difficulty: ", font=("Helvetica", 24), width = 10)
    AI_difficulty_label.place(x=350, y=400)
    # Add AI difficulty dropdown
    AI_difficulty = ttk.Combobox(state="readonly", values=["Easy", "Medium", "Hard"], font=("Helvetica", 24), width = 15)
    AI_difficulty.place(x=559, y=400)
    # Play button
    play = Button(window, text = "Play", command = checkEntries, font = ("Helvetica", 30), padx = 10, pady = 10)
    play.place(x=536, y=490)


def openInstructions():
    '''Opens the Intructions window'''
    print("Opening instructions window")
    instructions_window = Toplevel(window)
    instructions_window.title("Instructions")
    instructions_window.config(bg="#400050") # Dark Purple
    instructions_window.geometry("600x600")
    instructions_window.resizable(False, False)
    instructions_label = Label(instructions_window, text="Instructions", font=("Helvetica", 36))
    instructions_label.place(x=175, y=30)
    line1 = Label(instructions_window, text="Fractions is a game designed to practice your basic fraction operations ( + - × ÷ )",
                  font=("Helvetica", 12), width = 65, anchor = 'w')
    line2 = Label(instructions_window, text="After pressing start, choose a username and select a year level difficulty",
                  font=("Helvetica", 12), width = 65, anchor = 'w')
    line3 = Label(instructions_window, text="Year 7-8 uses numbers 1 to 5, Year 9-10 uses 1 to 7, Year 11-12 uses 1 to 10",
                  font=("Helvetica", 12), width = 65, anchor = 'w')
    line4 = Label(instructions_window, text="Each correct answer advances your rocket. Race to get to the finish line before the AI!",
                  font=("Helvetica", 12), width = 65, anchor = 'w')
    line5 = Label(instructions_window, text="Your numerator and denominator must be integers with no symbols, and simplified",
                  font=("Helvetica", 12), width = 65, anchor = 'w')
    line6 = Label(instructions_window, text="If your answer is invalid or not simplified, you are prompted to re-enter",
                  font=("Helvetica", 12), width = 65, anchor = 'w')
    line7 = Label(instructions_window, text="If your answer is correct or wrong, the game moves on to the next question",
                  font=("Helvetica", 12), width = 65, anchor = 'w')
    line8 = Label(instructions_window, text="At the end of the game, your score is recorded to the Highscores window",
                  font=("Helvetica", 12), width = 65, anchor = 'w')
    line1.place(x=5, y=100)
    line2.place(x=5, y=124)
    line3.place(x=5, y=148)
    line4.place(x=5, y=172)
    line5.place(x=5, y=196)
    line6.place(x=5, y=220)
    line7.place(x=5, y=244)
    line8.place(x=5, y=268)
    
    #Notes and tips
    tips_label = Label(instructions_window, text="Tips", font=("Helvetica", 36))
    tips_label.place(x=252, y=310)
    line9 = Label(instructions_window, text="You can press tab and shift+tab to alternate between numerator and denominator",
                  font=("Helvetica", 12), width = 65, anchor = 'w')
    line10 = Label(instructions_window, text="You can press enter to submit rather than pressing the submit button",
                  font=("Helvetica", 12), width = 65, anchor = 'w')
    line11 = Label(instructions_window, text="If the answer is 0, enter 0 / 1",
                  font=("Helvetica", 12), width = 65, anchor = 'w')
    line9.place(x=5, y=380)
    line10.place(x=5, y=404)
    line11.place(x=5, y=428)


def openHighscores():
    '''Opens the Highscores window'''
    def reset_scores():
        '''Confirms if user wants to reset their scores'''
        confirm_reset = messagebox.askquestion("Confirm Reset", "This will reset all of your scores! Do you wish to proceed?")
        if confirm_reset == "yes":
            output_file = open("scores.json", 'w').close()
            print("Scores reset")

    class score_label():
        '''A specific score that is displayed'''
        def __init__(self, username, time_taken, year_level, AI_difficulty, win_status, y_cord):
            self.username_label = Label(highscores_window, text=username, font=("Courier", 24), width = 18)
            self.time_taken_label = Label(highscores_window, text=time_taken, font=("Helvetica", 24), width = 6)
            self.year_level_label = Label(highscores_window, text=year_level, font=("Helvetica", 24), width = 9)
            self.AI_difficulty_label = Label(highscores_window, text=AI_difficulty, font=("Helvetica", 24), width = 9)
            self.win_status_label = Label(highscores_window, text=win_status, font=("Helvetica", 24), width = 5)
            # Placing details of score
            self.username_label.place(x=12.5, y=y_cord)
            self.time_taken_label.place(x=373.5, y=y_cord)
            self.year_level_label.place(x=506.5, y=y_cord)
            self.AI_difficulty_label.place(x=696.5, y=y_cord)
            self.win_status_label.place(x=886.5, y=y_cord)
    
    def load_scores():
        '''Display scores stored in the scores.json file'''
        try:
            with open("scores.json", 'r') as file:
                data_list = json.load(file)
            y_cord = 70
            for data in data_list:
                score_label(data["username"], f"{data['time_taken']:.2f}", data["year_level"], data["AI_difficulty"], data["win_status"], y_cord)
                y_cord += 50
                if y_cord > 500:
                    break
        except FileNotFoundError:
            print("No data found.")
        except json.decoder.JSONDecodeError:
            print("No scores submitted.")
    
    print("Opening highscores window")
    highscores_window = Toplevel()
    highscores_window.title("Highscores")
    highscores_window.config(bg="#CCCCCC") # Grey
    highscores_window.geometry("1000x600")
    highscores_window.resizable(False, False)
    # Username | Time | Year level | AI difficulty | Win status
    username_label = Label(highscores_window, text="Username", font=("Helvetica", 24), width = 18)
    time_label = Label(highscores_window, text="Time(s)", font=("Helvetica", 24), width = 6)
    year_level_label = Label(highscores_window, text="Year Level", font=("Helvetica", 24), width = 9)
    AI_difficulty_label = Label(highscores_window, text="AI Difficulty", font=("Helvetica", 24), width = 9)
    win_status_label = Label(highscores_window, text="Result", font=("Helvetica", 24), width = 5)
    # Placing header labels
    username_label.place(x=12.5, y=10)
    time_label.place(x=373.5, y=10)
    year_level_label.place(x=506.5, y=10)
    AI_difficulty_label.place(x=696.5, y=10)
    win_status_label.place(x=886.5, y=10)
    # Loading scores and placing reset button
    load_scores()
    reset_button = Button(highscores_window, text = "Reset", command = reset_scores, font = ("Helvetica", 20), padx = 5, pady = 5)
    reset_button.place(x=447.5, y=524)


def closeProgram():
    '''Closes the program'''
    print("Quitting program")
    exit()


def startUp():
    '''Opens the main menu'''
    global title, start, instructions, highscores, quit_button
    print("Entering main menu")
    # Title
    title = Label(window, text = "Fractions", font = ("Helvetica", 72), fg="#FFFFFF", bg="#300040", padx = 10, pady = 10)
    title.place(x=388, y=130)
    # Start button
    start = Button(window, text = "Start", command = openStart, font = ("Helvetica", 30), width = 14, pady = 0)
    start.place(x=434, y=320)
    # Instructions button
    instructions = Button(window, text = "Instructions", command = openInstructions, font = ("Helvetica", 30), width = 14, pady = 0)
    instructions.place(x=434, y=410)
    # Highscores button
    highscores = Button(window, text = "Highscores", command = openHighscores, font = ("Helvetica", 30), width = 14, pady = 0)
    highscores.place(x=434, y=500)
    # Quit buttons
    quit_button = Button(window, text = "Quit", command = closeProgram, font = ("Helvetica", 30), width = 14, pady = 0)
    quit_button.place(x=434, y=590)


window = Tk()
window.title("Fractions") 
window.config(bg="#300040") # Dark purple
window.geometry("1200x800")
window.resizable(False, False)

startUp()

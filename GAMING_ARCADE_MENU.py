# Importing tkinter module for graphics
import tkinter as tk

# Importing all games
import main  
import Hangman
import rock_paper_scissor 
import love_calc
import blackjack
import Higher_vs_Lower
import quiz_main
import turtle_main
import US_States_main

def launch_snake():
    main.start_game()

def launch_turtle():
    turtle_main.start_game()
    
def launch_US_States():
    US_States_main.start_game()
    
def launch_hangman():
    Hangman.start_game()
    
def launch_rock_paper_scissor():
    rock_paper_scissor.start_game()
    
def launch_calc():
    love_calc.start_game()

def launch_blackjack():
    blackjack.start_game()
    

def launch_Higher_vs_Lower():
    Higher_vs_Lower.start_game()
    
def launch_quiz():
    quiz_main.start_game()

    
def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("🎮 Python Gaming Arcade 🎮")
root.geometry("600x600")

# Heading label
title = tk.Label(root, text="Welcome to the Python Gaming Arcade", font=("Arial", 14, "bold"), pady=20)
title.pack()

# Snake Game Button
snake_button = tk.Button(root, text="Play Snake Game", font=("Arial", 12), width=20, command=launch_snake)
snake_button.pack(pady=10)

# Tutle Game Button
turtle_button = tk.Button(root, text="Play Turtle Crossing", font=("Arial", 12), width=20, command=launch_turtle)
turtle_button.pack(pady=10)

# US STATES Game Button
US_states_button = tk.Button(root, text="Play US States Game", font=("Arial", 12), width=20, command=launch_US_States)
US_states_button.pack(pady=10)

# Hangman button
hangman_button = tk.Button(root, text="Play Hangman", font=("Arial", 12), width=20, command=launch_hangman)
hangman_button.pack(pady=10)

# Rock Paper Scissor button
rockpprscissor_button = tk.Button(root, text="Play Rock-Ppr-Scissor", font=("Arial", 12), width=20, command=launch_rock_paper_scissor)
rockpprscissor_button.pack(pady=10)

# Black Jack button
blackjack_button = tk.Button(root, text="Play Black Jack", font=("Arial", 12), width=20, command=launch_blackjack)
blackjack_button.pack(pady=10)

# Followers Coparison Game button
followers_button = tk.Button(root, text="Play Followers Comparison Game", font=("Arial", 12), width=30, command=launch_Higher_vs_Lower)
followers_button.pack(pady=10)

# Love CalculatorButton
calc_button = tk.Button(root, text="Try Love Calculator!", font=("Arial", 12), width=20, command=launch_calc)
calc_button.pack(pady=10)

# Quiz Button
quiz_button = tk.Button(root, text="Play Quiz Game", font=("Arial", 12), width=20, command=launch_quiz)
quiz_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), width=20, command=exit_app)
exit_button.pack(pady=10)

# Run the main loop
root.mainloop()

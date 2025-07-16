import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Game Logic
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Handle User Selection
def play(user_choice):
    comp_choice = random.choice(choices)
    result = determine_winner(user_choice, comp_choice)

    # Update labels
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    comp_choice_label.config(text=f"Computer's Choice: {comp_choice}")
    result_label.config(text=result)

    # Update score
    global user_score, comp_score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        comp_score += 1
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")

# Main Window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x350")
root.resizable(False, False)
root.config(bg="#f0f0f0")

# Title
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Choices Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Result Display
user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12), bg="#f0f0f0")
user_choice_label.pack()

comp_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 12), bg="#f0f0f0")
comp_choice_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

# Score Tracking
user_score = 0
comp_score = 0
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="#f0f0f0")
score_label.pack()

# Play Again Info
info_label = tk.Label(root, text="Click a button to play again!", font=("Arial", 10), fg="gray", bg="#f0f0f0")
info_label.pack(pady=5)

# Start GUI
root.mainloop()

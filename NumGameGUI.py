# August 27th, 2026 | GUI version of previous project (Number Guessing Game)
# It's too confusing to think whether to build the logic first or GUI. I guess both bit by bit
import random
import tkinter as tk
from tkinter import ttk
secret_number = random.randint(1,10)
tries = 0
BG = "#184f1f"
BG2 = "#09420b"
FG = "#00ff08"
window = tk.Tk()
window.title("Number Game")
window.geometry("400x260")
window.config(bg=BG) # configure window's background to BG (containing hex code)
front_label = tk.Label(window, text="〚Guess The Number Between 1 to 10〛", bg=BG, fg=FG, font=("Georgia", 19))
front_label.grid(padx=34, pady=10)
try_label = tk.Label(window, text=f"-  You Have 3 Tries!    |   Current tries: {tries}", bg=BG, fg=FG, font=("georgia", 13))
try_label.grid(row=1, sticky=tk.W, padx=40)
entry_label = tk.Label(window, text="Enter Your Number: ", bg=BG, fg=FG, font=("georgia", 14))
entry_label.grid(row=2, sticky=tk.W, padx=45)
entry = tk.Entry(window, bg=BG, fg=FG, highlightthickness=1, highlightbackground=FG, width=2)
entry.grid(padx=60, pady=15, row=2)
feedback_label = tk.Label(window, text="", bg=BG, fg=FG, font=("georgia", 13))
feedback_label.grid(row=5)
correct_img = tk.PhotoImage(file="correct.png").subsample(4, 4)
wrong_img= tk.PhotoImage(file="wrong.png").subsample(14, 14)
lose_img = tk.PhotoImage(file="lose.png").subsample(190, 190)
image_label = tk.Label(window, bg=BG)
image_label.grid(row=6)
# what needs to happen now: entry collects input --> function (button) checks user's input
def check_num():
    global tries
    guess = int(entry.get())
    if tries >= 3:
        feedback_label.config(text="Game Over! Out of tries Loser..")
        image_label.config(image=lose_img)
        return
    tries += 1
    if guess == secret_number:
        feedback_label.config(text="Correct! 🎉")
        image_label.config(image=correct_img)
    elif tries == 2:
        image_label.config(image=wrong_img)
    elif guess < secret_number:
        feedback_label.config(text="Too low!")
        image_label.config(image=lose_img)
    else:
        feedback_label.config(text="Too high!")
        image_label.config(image=lose_img)
    try_label.config(text=f"Current Tries: {tries}")
style = ttk.Style()
style.theme_use('default')
style.configure("Custom.TButton", background=BG2, foreground=FG, font=("georgia", 13))
button = ttk.Button(window, text="Click To Check", command=check_num, width=11, style="Custom.TButton")
button.grid(row=4, column=0)
window.mainloop()
import tkinter as tk
import random
from tkinter import messagebox

secret_number = None
attempts = 0

def start_game():
    global secret_number, attempts
    try:
        start = int(start_entry.get())
        end = int(end_entry.get())

        if start >= end:
            messagebox.showerror("Error", "Start must be less than End")
            return

        secret_number = random.randint(start, end)
        attempts = 0
        result_label.config(text=f"Guess a number between {start} and {end}")
        entry.config(state="normal")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if guess < secret_number:
            result_label.config(text="Too Low!")
        elif guess > secret_number:
            result_label.config(text="Too High!")
        else:
            messagebox.showinfo("Success",f"Congratulations!\nYou guessed the number in {attempts} attempts.")
            root.destroy()
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a number")

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x350")

tk.Label(root,text="Number Guessing Game",font=("Arial", 16, "bold")).pack(pady=10)

range_frame = tk.Frame(root)
range_frame.pack(pady=10)

tk.Label(range_frame, text="Start:").grid(row=0, column=0, padx=5)
start_entry = tk.Entry(range_frame, width=6)
start_entry.grid(row=0, column=1)

tk.Label(range_frame, text="End:").grid(row=0, column=2, padx=5)
end_entry = tk.Entry(range_frame, width=6)
end_entry.grid(row=0, column=3)

tk.Button(root,text="Start Game",font=("Arial", 11),command=start_game).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center", state="disabled")
entry.pack(pady=10)

tk.Button(root,text="Check Guess",font=("Arial", 12),command=check_guess).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()

import tkinter as tk
from tkinter import messagebox


def reset():
    global current_player, winner
    current_player = "X"
    winner = False
    label.config(text=f"Player {current_player}'s Turn", fg="black")
    for button in buttons:
        button.config(text="", bg="white", state="normal")

def winning_animation(combo):
    def toggle_color(count=0):
        if count < 6: 
            color = "lightblue" if count % 2 == 0 else "white"
            for i in combo:
                buttons[i].config(bg=color)
            root.after(300, toggle_color, count + 1)
    toggle_color()

def check_winner():
    global winner
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            winner = True
            winning_animation(combo) 
            messagebox.showinfo("Tic-Tac-Toe", f"Hurray! Player {buttons[combo[0]]['text']} Wins!")
            root.after(1000, reset) 
            return
    
    
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "Oh! It's a Tie!")
        root.after(500, reset)


def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        buttons[index].config(bg="lightgrey") 
        check_winner()
        if not winner:
            toggle_player()


def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s Turn")


root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="#f5f5f5")

label = tk.Label(root, text="Player X's Turn", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="black")
label.grid(row=0, column=0, columnspan=3, pady=10)

buttons = [tk.Button(root, text="", font=("Arial", 20, "bold"), width=8, height=3, bg="white",
                     command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=(i//3) + 1, column=i%3, padx=5, pady=5)

restart_btn = tk.Button(root, text="Restart", font=("Arial", 16, "bold"), bg="gray", fg="white", command=reset)
restart_btn.grid(row=4, column=0, columnspan=3, pady=10)

current_player = "X"
winner = False

root.mainloop()

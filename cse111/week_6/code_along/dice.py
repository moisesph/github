import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import random


def main():
    root = tk.Tk()
    frm_window = tk.Frame(root)
    frm_window.master.title("Dice")
    frm_window.pack(padx=3, pady=3, fill=tk.BOTH,expand=True)
    set_main(frm_window)
    frm_window.mainloop()

 
def set_main(content):
    lbl_sides = tk.Label(content, text="The number of sides on the dice (2-10)")
    lbl_sides.grid(row=0, column=0)
    sides_entry = IntEntry(content, width=2, lower_bound=2, upper_bound=20)
    sides_entry.grid(row=0, column=1)

    lbl_times = tk.Label(content, text="Enter the number of dice to roll (1-10)")
    lbl_times.grid(row=1, column=0)
    times_entry = IntEntry(content, width=2, lower_bound=1, upper_bound=20)
    times_entry.grid(row=1, column=1)

    btn = tk.Button(content, text="Roll!")
    btn.grid(row=2, column=0)
 
    lbl_button = Label(content, text="")
    lbl_button.grid(row=3, column=0)

    def compute_dice(sides, quantity):
        sum = 0
        roll_total = ""

        for roll in range(quantity):
            die_roll = random.randint(1,sides)
            sum+=die_roll
            roll_total += f"{die_roll} "
        
        roll_total+=f"Total: {sum}"
        return roll_total




    def action_btn():
        try:
            sides = sides_entry.get()
        except ValueError:
            lbl_button.config(text="Enter a valid number of sides")
            return
        
        try: quantity = times_entry.get()
        except ValueError:
            lbl_button.config(text="The number of dice is incorrect")
            return
    

        compute = compute_dice(sides, quantity)

        lbl_button.config(text=compute)

    btn.config(command=action_btn)






if __name__ == "__main__":
    main()
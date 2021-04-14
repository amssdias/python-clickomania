import tkinter as tk

global lbl_lost
global lbl_won

buttons = []
score = 25
matched_btn = []
guesses = 0

window = tk.Tk()
window.geometry("500x500")

frm_nav = tk.Frame(master=window, pady=5, padx=16)
frm_main = tk.Frame(master=window, pady=16, padx=16)
frm_footer = tk.Frame(master=window, pady=16, padx=16)
frm_nav.pack(expand=True)
frm_main.pack(expand=True)
frm_footer.pack(expand=True)

lbl_score = tk.Label(
    master=frm_nav,
    text=f"Score: {score}",
    font=("Courier", 12))

lbl_score.pack()

btn_reset = tk.Button(
    master=frm_footer,
    text="Reset",
    font=("Courier", 14),
    padx=10,
    pady=3)

btn_reset.pack()

import random
from functools import partial
from layout import *


def activate(btn, color):
    global matched_btn
    global score
    global matched_btn
    global lbl_score
    global lbl_lost

    if btn['background'] == color:
        btn['background'] = 'grey'
        matched_btn.pop()

    else:
        btn['background'] = color
        matched_btn.append(btn)

    if len(matched_btn) == 2:
        if matched_btn[0]['background'] == matched_btn[1]['background']:
            matched_btn[0].config(command='')
            matched_btn[1].config(command='')
            matched_btn[0]['text'] = color
            matched_btn[1]['text'] = color
        else:
            matched_btn[0]['background'] = 'grey'
            matched_btn[1]['background'] = 'grey'
            score -= 1
            update_score(score)

            if score == 0:
                for btn in buttons:
                    btn.destroy()

                lbl_lost.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        matched_btn.clear()


def create_game():
    global score
    global lbl_score
    global buttons
    global matched_btn
    global lbl_lost
    global frm_nav

    matched_btn = []
    score = 3
    colors = ['white', 'black', 'red', 'green',
              'blue', 'cyan', 'yellow', 'magenta'] * 2

    update_score(score)

    if len(buttons):
        lbl_lost.destroy()
        for btn in buttons:
            btn.destroy()

    lbl_lost = tk.Label(
        master=frm_main,
        text="You Lost, try again!",
        font=("Courier", 14),
    )

    for i in range(4):
        for j in range(4):
            random_color = random.randint(0, len(colors)-1)
            color = colors[random_color]

            btn_square = tk.Button(
                master=frm_main,
                text=f"????",
                width=10,
                height=3,
                background='grey',
                activebackground=color
            )

            buttons.append(btn_square)
            btn_square.grid(row=i, column=j, padx=10, pady=10)
            buttons[-1]['command'] = partial(activate, btn_square, color)

            colors.pop(random_color)


def update_score(score):
    lbl_score['text'] = f"Score: {score}"


btn_reset['command'] = create_game

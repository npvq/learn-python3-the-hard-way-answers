# This code 'do_you_love_me.py' comes courtesy of Ryan Zhang
# It has been converted to Python 3 using 2to3, refer to documentation below:
# https://docs.python.org/2/library/2to3.html
# And edited to follow the style guidelines of 'pycodestyle'

import tkinter as tk

e = 0


class pOp:
    x = 825
    y = 425


pos = "500x200+" + str(pOp.x) + "+" + str(pOp.y)

loserTxt = ["Are you sure?",
            "Are you really sure?",
            "You really don't love me?",
            "You're kidding, right?",
            "This is not a joke?"]


def doneButton(place):

    brrr = tk.Button(place,
                     text="Just kidding, I LOVE YOU <3",
                     font=("Verdana", 20),
                     padx=10,
                     pady=10,
                     fg="#dba38c",
                     command=quit)

    brrr.pack(anchor="se",
              side="right")


def brokeButton(place):

    brrn = tk.Button(place,
                     text="YES. </3",
                     padx=10,
                     pady=10,
                     fg="#595959",
                     command=runNo)

    brrn.pack(anchor="se", side="right")


def runNo():

    global e

    if e == 4:

        e = 0

    else:

        e += 1

    pOp.x += 25
    pOp.y += 25

    noMessage()


def hateButton(place):

    bryn = tk.Button(place,
                     text="I HATE you.",
                     padx=10,
                     pady=10,
                     fg="#000000",
                     command=breakU)

    bryn.pack(anchor="sw", side="left")


def breakU():

    r = 0
    t = 0

    for i in range(770):

        sad = tk.Tk()
        sad.title("I HATE YOU TOO!!!! :'(")
        sad.geometry("500x200" + "+" + str(r) + "+" + str(t))

        sadtxt = tk.Label(sad,
                          text="NOOOOOOOOOO",
                          font=("Verdana", 24),
                          fg="#ff1e00")

        sadtxt.pack()

        if t > 1200:

            r -= 200
            t = 0

        if r > 5120:

            r -= 5043

        else:

            r += 8
            t += 31

    sad.mainloop()


def yesMessage():

    root.destroy()

    ms = tk.Tk()
    ms.title("Wow, I'm so touched!")
    ms.configure(bg="#ffd5ab")
    ms.geometry("500x200+800+400")

    msgtxt = tk.Label(ms,
                      text="Yay! :)",
                      font=("Verdana", 36),
                      bg="#ffd5ab")

    msgtxt.pack()

    finButton = tk.Button(ms,
                          text="Okay, done here.",
                          padx=10,
                          pady=10,
                          fg="#009e1a",
                          command=quit)
    finButton.pack()

    ms.mainloop()


def noMessage():

    bruh = tk.Tk()
    bruh.title("How COULD THIS HAPPEN TO MEEEEEE")
    bruh.configure(bg="#b8b9ff")
    bruh.geometry("500x200+" + str(pOp.x) + "+" + str(pOp.y))

    bruhtxt = tk.Label(bruh,
                       text=loserTxt[e],
                       font=("Verdana", 24, "bold"),
                       bg="#b8b9ff")
    bruhtxt.pack()

    doneButton(bruh)
    brokeButton(bruh)
    hateButton(bruh)

    bruh.mainloop()


root = tk.Tk()
root.configure(bg="#ffb5fa")
root.title("A Plea For Love")

root.geometry("500x200+800+400")

yes = tk.Button(root,
                text="Yes!",
                font=("Verdana", 26),
                fg="#020087",
                bg="#fabfaa",
                padx=10,
                pady=10,
                command=yesMessage)
yes.pack(anchor="se", side="right")

no = tk.Button(root,
               text="No...",
               bg="#c4c4c4",
               padx=10,
               pady=10,
               command=noMessage)
no.pack(anchor="se", side="right")

w = tk.Label(root,
             text="Do you love me?",
             bg="#ffb5fa",
             font=("Verdana", 36, "bold italic"),
             padx=10,
             pady=10)
w.pack(anchor="n")
w.place(anchor="center",
        x=250,
        y=35)

root.mainloop()

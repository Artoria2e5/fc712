import tkinter


def display():
    name = textVar.get()
    messageLabel.configure(text="Hello " + name)


top = tkinter.Tk()
top.title = "Kitty"
# Nothing "smart" happens when it's too small -- it just clips
top.geometry("400x300-100+100")
top.configure(bg="white")

textVar = tkinter.StringVar("")
textEntry = tkinter.Entry(top, textvariable=textVar, width=12)
textEntry.grid(row=0, column=0)

messageLabel = tkinter.Label(top, text="", width=12, bg="white")
messageLabel.grid(row=1, column=0)

# I don't really see a problem with buttons not being white...
# But I can play with other stuff
showButton = tkinter.Button(top, text="Show", command=display)
showButton.grid(row=1, column=1)

quitButton = tkinter.Button(top, text="Quit", command=top.destroy, bd=5)
quitButton.grid(row=1, column=2)


tkinter.mainloop()

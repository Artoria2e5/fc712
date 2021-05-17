import tkinter

CURRENCY_RATIOS = {
    "USD": 1,
    "GBP": 0.71,
    "DOGE": 2.06,
}


def convert():
    amount = textVar.get()
    from_c = from_currency.get()
    to_c = to_currency.get()
    try:
        amount = float(amount)
        message = str(amount / CURRENCY_RATIOS[from_c] * CURRENCY_RATIOS[to_c])
    except:
        message = "Invalid float amount"

    messageLabel.configure(text=message)


top = tkinter.Tk()

textVar = tkinter.StringVar(top, "1.0")
textEntry = tkinter.Entry(top, textvariable=textVar, width=12)
textEntry.grid(row=0, column=0, columnspan=2)

messageLabel = tkinter.Label(
    top, text="", width=18, justify=tkinter.LEFT, anchor=tkinter.NW
)
messageLabel.grid(row=0, column=2, columnspan=2)

fromLabel = tkinter.Label(
    top, text="From", width=6, justify=tkinter.LEFT, anchor=tkinter.NW
)
fromLabel.grid(row=1, column=0)
toLabel = tkinter.Label(
    top, text="To", width=6, justify=tkinter.LEFT, anchor=tkinter.NW
)
toLabel.grid(row=2, column=0)

from_currency = tkinter.StringVar(top, "USD")
to_currency = tkinter.StringVar(top, "USD")

CURRENCIES = CURRENCY_RATIOS.keys()
for k, v in enumerate(CURRENCIES):
    in_button = tkinter.Radiobutton(
        top, text=v, value=v, variable=from_currency, command=convert, width=7
    )
    in_button.grid(row=1, column=1 + k)
    out_button = tkinter.Radiobutton(
        top, text=v, value=v, variable=to_currency, command=convert, width=7
    )
    out_button.grid(row=2, column=1 + k)

quitButton = tkinter.Button(top, text="Quit", command=top.destroy)
quitButton.grid(row=3, column=3)

tkinter.mainloop()

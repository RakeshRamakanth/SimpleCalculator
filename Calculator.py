from tkinter import *
import parser

root = Tk()
root.title("Calculator")
i = 0


def all_clear():
    field.delete(0, END)


def remove_one():
    entire_string = field.get()
    new_string = entire_string[:-1]
    all_clear()
    field.insert(0, new_string)


def dispay_value(number):
    global i
    field.insert(i, number)
    i += 1


field = Entry(root)
field.grid(row=1, columnspan=6, sticky=W + E)

# Calculator
Button(root, text="1", command=lambda: dispay_value(1)).grid(row=2, column=1)
Button(root, text="2", command=lambda: dispay_value(2)).grid(row=2, column=2)
Button(root, text="3", command=lambda: dispay_value(3)).grid(row=2, column=3)

Button(root, text="4", command=lambda: dispay_value(4)).grid(row=3, column=1)
Button(root, text="5", command=lambda: dispay_value(5)).grid(row=3, column=2)
Button(root, text="6", command=lambda: dispay_value(6)).grid(row=3, column=3)

Button(root, text="7", command=lambda: dispay_value(7)).grid(row=4, column=1)
Button(root, text="8", command=lambda: dispay_value(8)).grid(row=4, column=2)
Button(root, text="9", command=lambda: dispay_value(9)).grid(row=4, column=3)

Button(root, text="AC", command=lambda: all_clear()).grid(row=5, column=1)
Button(root, text="0", command=lambda: dispay_value(0)).grid(row=5, column=2)
Button(root, text="=").grid(row=5, column=3)

Button(root, text="+").grid(row=2, column=4)
Button(root, text="-").grid(row=3, column=4)
Button(root, text="*").grid(row=4, column=4)
Button(root, text="/").grid(row=5, column=4)

Button(root, text="pi").grid(row=2, column=5)
Button(root, text="%").grid(row=3, column=5)
Button(root, text="(").grid(row=4, column=5)
Button(root, text="exp").grid(row=5, column=5)

Button(root, text="<-", command=lambda: remove_one()).grid(row=2, column=4)
Button(root, text="!").grid(row=3, column=4)
Button(root, text=")").grid(row=4, column=4)
Button(root, text="^2").grid(row=5, column=4)

root.mainloop()

from tkinter import *

window = Tk()
window.title("My first converter")
window.minsize(width=500, height=150)
window.config(padx= 100, pady= 30)

def button_clicked():
    result.config(text = round(float(entry.get()) * 1.609344, 2))

entry = Entry()
entry.grid(row = 0, column = 1, )

is_equal_to = Label(text= "is equal to :")
is_equal_to.grid(row= 1 , column= 0)

miles = Label(text= "miles")
miles.grid(row= 0 , column= 2)
miles.config(padx=15)

result = Label(text="0")
result.grid(row= 1 , column= 1)
result.config(padx= 10, pady= 10)

km = Label(text= "km")
km.grid(row= 1 , column= 2)

button = Button(text="calculate", command= button_clicked)
button.grid(row= 2, column= 1)

window.mainloop()
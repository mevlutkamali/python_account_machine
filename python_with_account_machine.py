
import tkinter as tk

def sum():
    if number_1.get().isdigit() and number_2.get().isdigit() :
        number1 = float(number_1.get())
        number2 = float(number_2.get())

        conclusion.configure(text=str(number1 + number2))

def extraction() :
    if number_1.get().isdigit() and number_2.get().isdigit() :
        number1 = float(number_1.get())
        number2 = float(number_2.get())

        conclusion.configure(text=str(number1 - number2))

def impact() :
    if number_1.get().isdigit() and number_2.get().isdigit() :
        number1 = float(number_1.get())
        number2 = float(number_2.get())

        conclusion.configure(text=str(number1 * number2))

def divide() :
    if number_1.get().isdigit() and number_2.get().isdigit() :
        number1 = float(number_1.get())
        number2 = float(number_2.get())

        conclusion.configure(text=str(number1 / number2))


window = tk.Tk()

window.title(' Calculator_Machine ')
window.geometry('320x400')

conclusion = tk.Label(window, text='SONUÇ', font='Courier 16 bold', justify='center', width=30)
conclusion.place(x=-50, y=20)

number_1 = tk.Entry(window, font='Courier 14 bold', justify='right', width=15)
number_1.place(x=70, y=50)

number_2 = tk.Entry(window, font='Courier 14 bold', justify='right', width=15)
number_2.place(x=70, y=80)

key_1 = tk.Button(window, text="+", font='Courier 14 bold', width=10, command=sum)
key_1.place(x=90, y=110)

key_2 = tk.Button(window, text="-", font='Courier 14 bold', width=10, command=extraction)
key_2.place(x=90, y=140)

key_3 = tk.Button(window, text="*", font='Courier 14 bold', width=10, command=impact)
key_3.place(x=90, y=170)

key_4 = tk.Button(window, text="/", font='Courier 14 bold', width=10, command=divide)
key_4.place(x=90, y=200)

number_1.focus()

window.mainloop()


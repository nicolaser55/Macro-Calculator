import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk

NORM_FONT = ('Verdana', 10)

#Popup
def popup_message(message):
    popup = tk.Tk()
    popup.wm_title('Error')
    label = ttk.Label(popup, text = message, font = NORM_FONT)
    label.pack(side = TOP, fill="x", pady= 20)
    B1 = ttk.Button(popup, text='Okay', command = popup.destroy)
    B1.pack()
    popup.mainloop()

#logic
def click():
    try:
        cals = int(calories.get())
    except ValueError:
        popup_message('Please input a number for calories')

    try:
        proteins = int(textentry1.get())
    except ValueError:
        popup_message('Please input a percentage for proteins')

    try:
        carbs = int(textentry2.get())
    except ValueError:
        popup_message('Please input a percentage for carbs')

    try:
        fats = int(textentry3.get())
    except ValueError:
        popup_message('Please input a percentage for fats.')

    output1.delete(0.0, END)
    output2.delete(0.0, END)
    output3.delete(0.0, END)

    grams_p = (cals//4)*(proteins/100)
    grams_c = (cals//4)*(carbs/100)
    grams_f = (cals//9)*(fats/100)

    output1.insert(END, round(grams_p))
    output2.insert(END, round(grams_c))
    output3.insert(END, round(grams_f))

#Start of GUI
window = Tk()
window.title("Macro Split Calculator")
window.configure(background="black")
photo1 = PhotoImage(file="./myfitnesspal.gif")

Label(window, image=photo1, bg="black"). grid(row=0, column=0,columnspan=3, sticky=E)

#Calories
Label(window, text="Input your calories", bg="black", fg="white",font="none 15 bold").grid(row=1,column=0,sticky=W)
calories = Entry(window,width=20, bg="white",fg="black")
calories.grid(row=1,column=1,sticky=W)

#Macros titles
Label(window, text="Macros", bg="black", fg="white",font="none 15 bold").grid(row=2,column=0,sticky=W)
Label(window, text="Protein", bg="black",fg="white",font="none 12 bold").grid(row=3,column=0,sticky=W)
Label(window, text="Carb", bg="black",fg="white",font="none 12 bold").grid(row=4,column=0,sticky=W)
Label(window, text="Fat", bg="black",fg="white",font="none 12 bold").grid(row=5,column=0,sticky=W)

#Percentages
Label(window, text="Percentages %", bg="black", fg="white",font="none 15 bold").grid(row=2,column=1,sticky=W)
textentry1 = Entry(window, width=10, bg="white",fg="black")
textentry2 = Entry(window, width=10, bg="white",fg="black")
textentry3 = Entry(window, width=10, bg="white",fg="black")
textentry1.grid(row=3,column=1,sticky=W)
textentry2.grid(row=4,column=1,sticky=W)
textentry3.grid(row=5,column=1,sticky=W)

#Output
Label(window, text="Grams of each macro", bg="black", fg="white",font="none 15 bold").grid(row=2,column=2,sticky=W)
output1 = Text(window, width=25,height=1,wrap=WORD,bg="black",fg="red")
output1.grid(row=3,column=2,sticky=W)
output2 = Text(window, width=25,height=1,wrap=WORD,bg="black",fg="red")
output2.grid(row=4,column=2,sticky=W)
output3 = Text(window, width=25,height=1,wrap=WORD,bg="black",fg="red")
output3.grid(row=5,column=2,sticky=W)

#Calculate Button
Button(window, text="Calculate", width=9,command=click).grid(row=6,column=1,sticky=W)

#Exit Function
def close_window():
    window.destroy()
    exit()
#Exit Button
Button(window, text="Click to Exit",width=14,command=close_window).grid(row=7, column=0, sticky=W)

#Loop
window.mainloop()

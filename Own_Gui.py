from tkinter import *


master = Tk()
master.title("My First Window")
master.geometry("400x400")
master.configure(background = "deep sky blue")

def dummy_function():
    print("Button Press")

#Four Buttons
Button1 = Button(master, text = "Click", command = dummy_function, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
Button1.grid(row = 1, column = 4)

Button2 = Button(master, text = "These", command = dummy_function, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
Button2.grid(row = 2, column = 4)

Button3 = Button(master, text = "Cool", command = dummy_function, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
Button3.grid(row = 3, column = 4)

Button4 = Button(master, text = "Buttons", command = dummy_function, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
Button4.grid(row = 4, column = 4)

#Two Sliders
Vertical_scale = Scale(master, from_=0, to=100)
Vertical_scale.grid()

Horizontal_slider = Scale(master, from_=0, to=100, orient=HORIZONTAL)
Horizontal_slider.grid()

#Two Text Boxes

#Four Labels


#Four Check Buttons
Check1 = IntVar()
Checkbutton(master, text='Monster', variable=Check1).grid(row=7, column=10)
Check2 = IntVar()
Checkbutton(master, text='Man', variable=Check2).grid(row=8, column=10)
Check3 = IntVar()
Checkbutton(master, text='Mouse', variable=Check3).grid(row=9, column=10)
Check4 = IntVar()
Checkbutton(master, text='Horse', variable=Check4).grid(row=10, column=10)

#One Drop Down Menu

#One Pop Up Window


#Five Radio Buttons Confused
Radiobutton(master, text='Cheese', variable=IntVar(), value=1).grid(row=5, column=5)
Radiobutton(master, text='No Cheese', variable=IntVar(), value=2).grid(row=6, column=5)
Radiobutton(master, text='Pickles', variable=IntVar(), value=3).grid(row=7, column=5)
Radiobutton(master, text='No Pickles', variable=IntVar(), value=4).grid(row=8, column=5)

#One Scrollbar bBox


#One Spin Box
spinner = Spinbox(master, from_ = 0, to = 10)
spinner.grid(row=1, column=100)






String_input_value = StringVar(master, value='')
Total_box = Entry(master,textvariable=String_input_value)
Total_box.grid(row=0, columnspan=4, sticky=W + E)

master.mainloop() #Always put at the end
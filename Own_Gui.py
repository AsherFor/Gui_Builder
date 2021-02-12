'''
Asher Forman
GUI Builder
2/10/2021
'''

from tkinter import *

master = Tk()
master.title("Asher's Own Gui")
master.geometry("700x700")
master.configure(background = "deep sky blue")

def button_function():
    print("Working Button!")

def radio_button_function():
    print("Working Radio Button!")

def check_box_function():
    print("Working Check Box!")

def pop_up_window():
    new_window = Toplevel()
    new_window.title('Button Activated Pop Up Window')
    new_window.configure(background = "deep sky blue")


#Four Buttons
Button1 = Button(master, text = "Click", command = button_function, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
Button1.grid(row = 0, column = 4)

Button2 = Button(master, text = "These", command = button_function, bg="red", fg="blue2", highlightbackground="red", activebackground="dark green")
Button2.grid(row = 1, column = 4)

Button3 = Button(master, text = "Cool", command = button_function, bg="snow3", fg="ivory3", highlightbackground="cyan", activebackground="violet")
Button3.grid(row = 2, column = 4)

Button4 = Button(master, text = "Buttons", command = button_function, bg="seashell4", fg="SeaGreen4", highlightbackground="dodger blue", activebackground="gold")
Button4.grid(row = 3, column = 4)

#Two Sliders
Vertical_slider = Scale(master, from_= 0, to=100, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
Vertical_slider.grid()

Horizontal_slider = Scale(master, from_= 0, to=100, orient=HORIZONTAL, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
Horizontal_slider.grid()

#Two Text Boxes
String_input_value = StringVar(master, value='')
Text_Box_1 = Entry(master,textvariable=String_input_value)
Text_Box_1.grid(row=0, columnspan=4, sticky=W + E)

String_input_value2 = StringVar(master, value='')
Text_Box_2 = Entry(master,textvariable=String_input_value2)
Text_Box_2.grid(row=1, columnspan=4, sticky=W + E)


#Four Labels
label_1 = Label(master, text='Asher is Cool', bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
label_1.grid(row = 7, column = 0)

label_2 = Label(master, text='They are among us...', bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
label_2.grid(row = 8, column = 0)

label_3 = Label(master, text='New apple iPhone', bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
label_3.grid(row = 9, column = 0)

label_4 = Label(master, text='How to not age', bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
label_4.grid(row = 10, column = 0)

#Four Check Boxes
Check1 = IntVar()
Checkbutton(master, command = check_box_function, text='Married', variable=Check1, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=7, column=3)
Check2 = IntVar()
Checkbutton(master, command = check_box_function, text='Single', variable=Check2, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=8, column=3)
Check3 = IntVar()
Checkbutton(master, command = check_box_function, text='Blue Eyes', variable=Check3, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=9, column=3)
Check4 = IntVar()
Checkbutton(master, command = check_box_function, text='Brown Eyes', variable=Check4, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=10, column=3)


#One Drop Down Menu
top_value = StringVar(master)
top_value.set("Menu")
drop_down_menu = OptionMenu(master, top_value, "Help", "About Me", "Link to Library")
drop_down_menu.grid(row = 0, column = 6)


#One Pop Up Window
pop_up = Toplevel()
pop_up.title('Pop Up Window')
pop_up.configure(background = "deep sky blue")

    #Button that creates pop up window
Button_window = Button(master, text = "Click for Pop Up Window", command = pop_up_window, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
Button_window.grid(row = 5, column = 4)


#Five Radio Buttons
Radiobutton(master, command = radio_button_function, text='Spotify', variable=IntVar(), value=1, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=7, column=4)
Radiobutton(master, command = radio_button_function, text='Apple Music', variable=IntVar(), value=2, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=8, column=4)
Radiobutton(master, command = radio_button_function, text='Pandora', variable=IntVar(), value=3, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=9, column=4)
Radiobutton(master, command = radio_button_function, text='Youtube', variable=IntVar(), value=4, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=10, column=4)
Radiobutton(master, command = radio_button_function, text='Radio', variable=IntVar(), value=5, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=11, column=4)

#One Scrollbar Box
new_scrollbar = Scrollbar(master)
new_scrollbar.grid(row = 25, column = 1)
scroll_list = Listbox(master, yscrollcommand=new_scrollbar.set)
for line in range(101):
    scroll_list.insert(END, "This is number " + str(line))
scroll_list.grid(row = 25, column = 0)
new_scrollbar.config(command=scroll_list.yview)


#One Spin Box
spinner = Spinbox(master, from_ = 0, to = 10, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue")
spinner.grid(row=22, column=6)

master.mainloop()
import tkinter
from tkinter import ttk
from tkinter import *
import random
import customtkinter  # <- import the CustomTkinter module

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("800x440")
root_tk.title("Sorting Algorithm Visualizer")
root_tk.configure(background='#7faceb')



main_heading = customtkinter.CTkLabel(master=root_tk,
                               text="S O R T I N G\nV I S U A L I Z E R",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",20))
main_heading.place(x=27, y=30)

dark_mode_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Dark Mode ",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",12))
dark_mode_lb.place(x=5, y=90)

def switch_event():
    print(dark_mode_switch_var.get())
    if dark_mode_switch_var.get() == "on":
        customtkinter.set_appearance_mode("Light")
    else:
        customtkinter.set_appearance_mode("Dark")

dark_mode_switch_var = customtkinter.StringVar(value="on")
dark_mode_switch = customtkinter.CTkSwitch(root_tk, text="", command=switch_event,
                                 variable=dark_mode_switch_var, onvalue="on", offvalue="off")
dark_mode_switch.place(x=90,y=92)


input_size_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Input Size ",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",12))
input_size_lb.place(x=5, y=120)


input_size_entry = customtkinter.CTkEntry(master=root_tk,
                               width=200,
                               height=18,
                               corner_radius=5)
input_size_entry.place(x=10, y=145)

text = input_size_entry.get()

min_value_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Min Value ",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",12))
min_value_lb.place(x=5, y=180)

max_value_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Max Value ",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",12))
max_value_lb.place(x=110, y=180)

min_size_entry = customtkinter.CTkEntry(master=root_tk,
                               width=100,
                               height=18,
                               corner_radius=5)
min_size_entry.place(x=10, y=205)

min_value = min_size_entry.get()

max_size_entry = customtkinter.CTkEntry(master=root_tk,
                               width=100,
                               height=18,
                               corner_radius=5)
max_size_entry.place(x=110, y=205)

max_value = max_size_entry.get()


sorting_algo_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Sorting Algorithm",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",12))
sorting_algo_lb.place(x=5, y=240)

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

sorting_algo_combobox = customtkinter.CTkComboBox(root_tk, values=["Bubble Sort", "Insertion Sort","Quick Sort","Marge Sort"],width=200,height=25,
                                     command=combobox_callback)
sorting_algo_combobox.set("Bubble Sort")

sorting_algo_combobox.place(x=10,y=265)

speed_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Speed",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("TypoGraphica",12))
speed_lb.place(x=5, y=300)

def slider_event(value):
    print(int(value*100))

speed_slider = customtkinter.CTkSlider(master=root_tk,
                                 width=210,
                                 height=16,
                                 border_width=5.5,
                                 command=slider_event)
speed_slider.place(x=5,y=325)


def generat_button_event():
    print("button pressed")

generat_button = customtkinter.CTkButton(master=root_tk,
                                 text="Generat",
                                 command=generat_button_event,
                                 width=95,
                                 height=28,
                                 border_width=0,
                                 corner_radius=8)
generat_button.place(x=10,y=350)

def start_button_event():
    print("button pressed")

start_button = customtkinter.CTkButton(master=root_tk,
                                 text="Start",
                                 command=start_button_event,
                                 width=95,
                                 height=28,
                                 border_width=0,
                                 corner_radius=8)
start_button.place(x=115,y=350)

canvas = Canvas(root_tk,width=560, height=440,bg="gray")#e6f0f7
canvas.place(x=240,y=0)


root_tk.mainloop()
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
                               font=("helvetica",20))
main_heading.place(x=27, y=30)

dark_mode_lb = customtkinter.CTkLabel(master=root_tk,
                               text="Dark Mode ",
                               width=50,
                               height=25,
                               corner_radius=8,
                               font=("helvetica",12))
dark_mode_lb.place(x=5, y=90)

def switch_event():
    if dark_mode_switch_var.get() == "on":
        customtkinter.set_appearance_mode("Light")
    else:
        customtkinter.set_appearance_mode("Dark")

dark_mode_switch_var = customtkinter.StringVar(value="on")
dark_mode_switch = customtkinter.CTkSwitch(root_tk, text="", command=switch_event,
                                 variable=dark_mode_switch_var, onvalue="on", offvalue="off")
dark_mode_switch.place(x=90,y=92)


canvas = Canvas(root_tk,width=560, height=440,bg="#e6f0f7")
canvas.place(x=240,y=0)






root_tk.mainloop()